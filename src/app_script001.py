#!/usr/bin/env python3
# coding: utf-8

import cyclopts # This 3rd-party package should be included in the environment.yml file pip section.
from pathlib import Path # This Python Standard Library package should not be added to environment.yml.

app = cyclopts.App(
    help="Help string for this app.",
    config=cyclopts.config.Json(
        "config_example.json",  # Use this file, if in cwd (or a parent).
        search_parents=True,
        )
    )

@app.default
def main(
    name: str = "Bob",
    age: int = 33,
    outdir: str = "./"
    ):
    """
    Put any lines of code you would normally have in a
    simple Python "script" here.
    """
    outpath = Path(outdir)
    outpath.mkdir(exist_ok=True, parents=True)
    outpath /= "main_output.txt"
    output = f"{name}'s age is {age}.\n"
    print(output)
    with outpath.open("w") as filehandle:
        filehandle.write(output)
    return output


if __name__ == "__main__":
    app()
