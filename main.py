"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt and prints it:
a To: line naming who the message was meant for, and the unsent message
itself, exactly as it was typed. Deterministic: no input, no randomness,
no network, no clock.
"""

import os

TO_LINE = "To: Leo, my old roommate"
MESSAGE = (
    "I never told you I broke your favourite mug; I bought an identical "
    "one and let you think you'd misremembered it."
)

ENTRY = TO_LINE + "\n" + MESSAGE


def check_gate(entry: str) -> None:
    """Self-check the competition gate before writing anything."""
    assert entry, "entry must not be empty"
    assert entry.strip(), "entry must not be only whitespace"
    assert 1 <= len(entry) <= 260, "entry must be 1-260 characters"
    lines = entry.split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert lines[0].startswith("To: "), "first line must be the To: line"
    assert lines[0][4:].strip(), "To: line must name someone"
    assert 1 <= len(lines[1]) <= 200, "message must be 1-200 characters"
    assert lines[1].strip(), "message must not be only whitespace"


def main() -> int:
    check_gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    # Read back what was written and confirm it is byte-for-byte the entry.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "written entry does not round-trip"
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
