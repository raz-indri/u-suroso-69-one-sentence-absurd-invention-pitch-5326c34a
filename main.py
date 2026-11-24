#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching the NagWave, a microwave that reheats
your forgotten leftovers and then beeps your name in Morse code until you
come and rescue them before they go cold again.
"""

import os

ENTRY = (
    "The NagWave microwave reheats your forgotten leftovers, then beeps "
    "your name in Morse code until you rescue them before they go cold again."
)


def main() -> None:
    # Self-check against the competition gate: one sentence, 1-220 chars.
    assert 1 <= len(ENTRY) <= 220, f"entry is {len(ENTRY)} chars"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "must be one sentence"
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
