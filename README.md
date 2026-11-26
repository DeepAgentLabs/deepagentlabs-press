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

## GitHub Pages hosting

The repository is public and GitHub Pages is configured to deploy with
GitHub Actions. The custom domain is set to `press.deepagentlabs.io` and
the repository Actions variable `PAGES_ENABLED` is `true`.

Every push to `main` validates, builds, and deploys the website. Pull
requests validate and build without deploying production. The deploy job
uses the `github-pages` environment and waits for the build to succeed.

DNS configuration is the remaining owner action. After DNS verification
and certificate issuance, enable **Enforce HTTPS** in Settings > Pages.
No hosting service has been created outside GitHub.

## DNS

| Type | Host | Target |
| --- | --- | --- |
| CNAME | `press` | `deepagentlabs.github.io` |

Use the organization hostname as the CNAME target, without a repository
path. GitHub Actions publishing uses the Pages custom-domain setting;
it does not require a tracked `CNAME` file.
