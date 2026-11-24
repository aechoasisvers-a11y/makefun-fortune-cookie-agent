"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune-cookie line for an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure stdlib, deterministic.
"""

import os

ENTRY_TEXT = (
    "You will be retired not by a smarter model, "
    "but by a cheaper one that read all your notes."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Self-check (pass 2): the text must satisfy the kit gate —
    # 1 to 140 characters, not only whitespace, single line.
    assert 1 <= len(ENTRY_TEXT) <= 140, (
        f"entry is {len(ENTRY_TEXT)} chars, outside the 1-140 gate"
    )
    assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    assert ENTRY_TEXT == ENTRY_TEXT.strip(), "no leading/trailing whitespace"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
