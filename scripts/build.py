"""Validate local page references and produce only public website files."""
from html.parser import HTMLParser
from pathlib import Path
import shutil
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_FILES = ('index.html', 'styles.css', 'favicon.svg')


class PageValidator(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.fragments = []
        self.has_title = False
        self.has_language = False
        self.has_viewport = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            if attrs['id'] in self.ids:
                raise ValueError(f"Duplicate ID: {attrs['id']}")
            self.ids.add(attrs['id'])
        if tag == 'html':
            self.has_language = bool(attrs.get('lang'))
        if tag == 'title':
            self.has_title = True
        if tag == 'meta' and attrs.get('name') == 'viewport':
            self.has_viewport = bool(attrs.get('content'))
        if tag == 'img' and 'alt' not in attrs:
            raise ValueError('Images must declare alt text')
        for name in ('href', 'src'):
            value = attrs.get(name)
            if not value:
                continue
            url = urlsplit(value)
            if url.scheme or url.netloc:
                continue
            if url.path:
                path = unquote(url.path).removeprefix('./')
                if path not in PUBLIC_FILES or not (ROOT / path).is_file():
                    raise ValueError(f'Unpublished local asset: {value}')
            elif url.fragment:
                self.fragments.append(unquote(url.fragment))


def main():
    validator = PageValidator()
    validator.feed((ROOT / 'index.html').read_text(encoding='utf-8'))
    validator.close()
    if not all((validator.has_title, validator.has_language, validator.has_viewport)):
        raise ValueError('Page must declare a title, language, and viewport')
    missing = set(validator.fragments) - validator.ids
    if missing:
        raise ValueError(f'Broken page anchors: {sorted(missing)}')
    ET.parse(ROOT / 'favicon.svg')
    output = ROOT / 'dist'
    if output.exists():
        shutil.rmtree(output)
    output.mkdir()
    for filename in PUBLIC_FILES:
        shutil.copy2(ROOT / filename, output / filename)
    print('Validation passed. Website built in dist/ (3 public files).')


if __name__ == '__main__':
    main()
