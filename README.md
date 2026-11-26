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

## CI and hosting

GitHub Actions runs **Website CI / Validate and build** on pushes to `main`
and pull requests targeting `main`. It validates local asset references,
page anchors, basic accessibility metadata, and the SVG icon, then uploads
only the public files as the `website` artifact.

The same build command can be used on Render:

- Repository: `DeepAgentLabs/deepagentlabs-press` (private)
- Branch: `main`
- Build command: `python3 scripts/build.py`
- Publish directory: `dist`
- Custom domain: `press.deepagentlabs.io`

Hosting setup is pending workspace selection and repository access. Once
created, configure Render's auto-deploy setting to **After CI Checks Pass**
to deploy successful `main` commits. Pull requests run CI without deploying
production. The repository remains private while published website assets
are public. DNS must point to the hostname provided by Render before the
custom domain can serve the site over HTTPS.
