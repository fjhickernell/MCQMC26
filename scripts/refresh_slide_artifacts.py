#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SLIDES_DIR = ROOT / "slides"
ARTIFACT_ROOT = ROOT / "notebooks" / "artifacts"
CACHE_ROOT = ROOT / "notebooks" / "cache"

DEFAULT_SLIDES_QMD = [
    SLIDES_DIR / "Plenary_MCQMC2026.qmd",
    SLIDES_DIR / "SpecialSession_MCQMC2026.qmd",
]

ARTIFACT_PATTERN = re.compile(
    r"\.\./notebooks/artifacts/([^\)\}\s\"']+)"
)


def refresh_from_slide(slides_qmd: Path, dry_run: bool = False) -> int:
    if not slides_qmd.exists():
        print(f"Missing slide file: {slides_qmd}")
        return 0

    text = slides_qmd.read_text()
    rel_artifact_paths = sorted(set(ARTIFACT_PATTERN.findall(text)))

    if not rel_artifact_paths:
        print(f"No artifact references found in {slides_qmd}")
        return 0

    print(f"Found {len(rel_artifact_paths)} artifact references in {slides_qmd}\n")

    copied_or_checked = 0

    for rel_path in rel_artifact_paths:
        artifact_path = ARTIFACT_ROOT / rel_path
        cache_path = CACHE_ROOT / rel_path

        if not cache_path.exists():
            print(f"Missing cache file: {cache_path}")
            continue

        artifact_path.parent.mkdir(parents=True, exist_ok=True)

        if dry_run:
            print(f"Would copy: {cache_path} -> {artifact_path}")
        elif artifact_path.exists() and artifact_path.read_bytes() == cache_path.read_bytes():
            print(f"Unchanged: {artifact_path}")
        else:
            shutil.copy2(cache_path, artifact_path)
            print(f"Copied: {cache_path} -> {artifact_path}")

        copied_or_checked += 1

    print()
    return copied_or_checked


def main(slides: list[Path], dry_run: bool = False) -> None:
    total = 0

    for slides_qmd in slides:
        total += refresh_from_slide(slides_qmd, dry_run=dry_run)

    print(f"Done. Processed {total} artifact references.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Refresh slide artifact files from matching cache files."
    )
    parser.add_argument(
        "slides",
        nargs="*",
        type=Path,
        help="Slide .qmd files to scan. Defaults to plenary and special-session talks.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Scan all .qmd files in the slides directory.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be copied without copying.",
    )

    args = parser.parse_args()

    if args.all:
        slides = sorted(SLIDES_DIR.glob("*.qmd"))
    elif args.slides:
        slides = [
            p if p.is_absolute() else ROOT / p
            for p in args.slides
        ]
    else:
        slides = DEFAULT_SLIDES_QMD

    main(slides=slides, dry_run=args.dry_run)

    