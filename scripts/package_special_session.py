#!/usr/bin/env python3
"""Export the special-session manuscript as a self-contained Overleaf ZIP."""

import argparse
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    manuscript = root / "manuscripts/special-session"
    files = [manuscript / name for name in
             ("main.tex", "references.bib", "svproc.cls", "spmpsci.bst")]
    files += sorted((manuscript / "sections").glob("*.tex"))
    figures = {}
    contents = {}
    for source in files:
        data = source.read_bytes()
        if source.suffix == ".tex":
            text = data.decode()
            for reference in re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", text):
                figure = (manuscript / reference).resolve()
                if not figure.is_file():
                    raise FileNotFoundError(figure)
                destination = "figures/" + figure.name
                if destination in figures and figures[destination] != figure:
                    raise ValueError(f"Duplicate figure filename: {destination}")
                figures[destination] = figure
                text = text.replace("{" + reference + "}", "{" + destination + "}")
            data = text.encode()
        contents[source.relative_to(manuscript).as_posix()] = data
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(args.output, "w", compression=ZIP_DEFLATED) as archive:
        for name, data in contents.items():
            archive.writestr(name, data)
        for name, source in figures.items():
            archive.write(source, name)
    print(f"Wrote {args.output}: {len(contents)} source files, {len(figures)} figures")


if __name__ == "__main__":
    main()
