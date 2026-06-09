#!/usr/bin/env python3

from __future__ import annotations

import re
import shutil
from pathlib import Path


SLIDES_QMD = Path("slides/Plenary_MCQMC2026.qmd")

ARTIFACT_ROOT = Path("notebooks/artifacts")
CACHE_ROOT = Path("notebooks/cache")

ARTIFACT_PATTERN = re.compile(
    r"\.\./notebooks/artifacts/([^\)\}\s\"']+)"
)


def main(dry_run: bool = False) -> None:
    text = SLIDES_QMD.read_text()

    rel_artifact_paths = sorted(set(ARTIFACT_PATTERN.findall(text)))

    if not rel_artifact_paths:
        print(f"No artifact references found in {SLIDES_QMD}")
        return

    print(f"Found {len(rel_artifact_paths)} artifact references in {SLIDES_QMD}\n")

    for rel_path in rel_artifact_paths:
        artifact_path = ARTIFACT_ROOT / rel_path
        cache_path = CACHE_ROOT / rel_path

        if not cache_path.exists():
            print(f"Missing cache file: {cache_path}")
            continue

        artifact_path.parent.mkdir(parents=True, exist_ok=True)

        if dry_run:
            print(f"Would copy: {cache_path} -> {artifact_path}")
        else:
            shutil.copy2(cache_path, artifact_path)
            print(f"Copied: {cache_path} -> {artifact_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Refresh slide artifact files from matching cache files."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be copied without copying.",
    )

    args = parser.parse_args()
    main(dry_run=args.dry_run)
    