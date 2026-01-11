#!/usr/bin/env python3
"""Parse speaker notes from Quarto presentation."""

import re
from pathlib import Path


def parse_speaker_notes(qmd_path: str) -> list[str]:
    """Extract speaker notes from .qmd file."""
    content = Path(qmd_path).read_text(encoding="utf-8")
    pattern = r"::: \{\.notes\}\n(.*?)\n:::"
    matches = re.findall(pattern, content, re.DOTALL)
    return [note.strip() for note in matches if note.strip()]


def main():
    notes = parse_speaker_notes("index.qmd")

    with open("speaker_note.txt", "w", encoding="utf-8") as f:
        for i, note in enumerate(notes, 1):
            f.write(f"PAGE {i}:\n{note}\n\n")

    print(f"Extracted {len(notes)} speaker notes to speaker_note.txt")


if __name__ == "__main__":
    main()
