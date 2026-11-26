# DeepAgentLabs Press

A responsive coming-soon website for **DeepAgentLabs Press**.

**Planned address:** https://press.deepagentlabs.io

## Preview locally

No dependencies or package installation are required:

```sh
python3 scripts/build.py
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000.

## GitHub Actions CI/CD

`.github/workflows/ci.yml` validates and builds the website on pushes to
`main`, pull requests targeting `main`, and manual runs. The build checks
local assets, page anchors, accessibility metadata, and the SVG icon. It
uploads only the three public website files as the `website` artifact.

Production deployment uses GitHub Pages and runs only after a successful
build on `main`. Pull requests never deploy production. Deployment needs
no additional secret: it uses the scoped GitHub Actions token and OIDC.

## Hosting activation (pending)

GitHub rejected Pages creation because the organization is on GitHub Free
and this repository is private. Keep the repository private unless its
owner explicitly authorizes a visibility change. GitHub Team supports
Pages for private organization repositories; the published site is public.

After the plan or authorized visibility change is complete:

1. Enable GitHub Pages with **GitHub Actions** as the publishing source.
2. In repository Settings > Pages, save `press.deepagentlabs.io` as the custom domain.
3. Add the DNS record below.
4. Set the repository Actions variable `PAGES_ENABLED` to `true`.
5. Run **Website CI/CD** on `main` (or push a commit).
6. After DNS verification and certificate issuance, enable **Enforce HTTPS**.

Deployment is deliberately disabled until `PAGES_ENABLED` is set, so CI
continues to pass while Pages is unavailable. No hosting service has been
created outside GitHub.

## DNS (apply after the custom domain is saved in Pages)

| Type | Host | Target |
| --- | --- | --- |
| CNAME | `press` | `deepagentlabs.github.io` |

Use the organization hostname as the CNAME target, without a repository
path. GitHub Actions publishing uses the Pages custom-domain setting;
it does not require a tracked `CNAME` file.
