# SciducTainer
Minimal example (template) repo which includes files to interface with Sciduct job service.

This one happens to only depend on Python, with it's **top-level** (E.g. only things in import statments which are **not** in the Python standard library) dependencies and Python version specified in [environment.yml](environment.yml).
That should have any dependencies added (with pinned versions) to be able to run without containerization.
E.g.

```bash
micromamba env create --file environment.yml
micromamba activate app_env001
./src/app_script001.py --name Sue
# Sue's age is 33.
```

To use this, just click "Use this template". Create new repository with a name relevant for your app(s).
Then change file and app names as appropriate (E.g. [src/app_script001.py](src/app_script001.py) and in [apps.scif](apps.scif)).

This system uses Github Actions to build and publish a container, triggered by a git tag push of the form `v<major>.<minor>.<patch>` (See: [Semantic Versioning](https://semver.org/) for a quick explanation of what those mean).

E.g.
```bash
git add -u
git commit -m "useful commit message"
git pull --rebase && git push
git tag v0.1.1
git push origin v0.1.1
```

To enable Github Actions to build and publish this to the Github Container Resgistry (GHCR), someone will need to create an authentication [token](https://github.com/settings/tokens) with via their Github account having "repo" and "write:packages" permissions.

The token and username needs to be saved as a repository secret (in "https://github.com/user-or-org-name/repo-name/settings/secrets/actions"), with names matching the ones in [.github/workflows/build_docker.yml](.github/workflows/build_docker.yml)