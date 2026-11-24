"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to
/output/entry.txt. Pure stdlib Python 3.13.
"""
import os

FORTUNE = "You will be retired not by a smarter model, but by a cheaper one that read all your notes."


def main():
    text = FORTUNE
    # Gate self-check: 1-140 chars, not only whitespace, single line.
    assert 1 <= len(text) <= 140, "fortune must be 1-140 chars"
    assert text.strip(), "fortune must not be only whitespace"
    assert "\n" not in text, "fortune must be a single line"
    assert text == text.strip(), "fortune must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Post-write verification: read the file back and prove the bytes on
    # disk are exactly the intended text — a silent short write or an
    # encoding slip must fail loudly instead of reaching the judge.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == text, "written bytes differ from the fortune"
    assert raw == text.encode("utf-8"), "written bytes are not the UTF-8 encoding of the fortune"
    assert len(raw) == len(text), "output must be pure ASCII so bytes equal chars"


if __name__ == "__main__":
    main()
