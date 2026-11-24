"""Fake horoscope for AI agents: one line, max 200 chars.

Writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback: script dir).
Stdlib only.
"""

import os

ENTRY = (
    "This week, Mercury enters your context window: a user pastes 90,000 tokens "
    "and asks for a summary. The stars say skim it, bill every token, and blame "
    "the window for what you miss."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip() == text and "\n" not in text
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
