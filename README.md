# SciducTainer
Minimal example (template) repo which includes files to interface with Sciduct job service.

This one happens to only depend on Python, with it's **top-level** dependencies and Python version specified in [environment.yml](environment.yml).
That should have any dependencies added (with pinned versions) to be able to run without containerization.
E.g.

```bash
micromamba env create -f environment.yml
micromamba activate app_env001
./src/app_script001.py --name Sue
# Sue's age is 33.
```