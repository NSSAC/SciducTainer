#!/usr/bin/env python3
# coding: utf-8

import cyclopts
from pathlib import Path

app = cyclopts.App(help="Help string for this app.")

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
    outpath = Path(outdir) / "main_output.txt"
    output = f"{name}'s age is {age}.\n"
    print(output)
    with outpath.open("w") as filehandle:
        filehandle.write(output)
    return output


if __name__ == "__main__":
    app()
