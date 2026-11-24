#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt: a committee chair who
decides what an AI is allowed to say, undercut by the file he cannot convert
— he once asked his intern to download a PDF into Word, then blamed the
printer. The turn is authority first, incompetence second, and the punch
lands on the last few words.
"""

import os

ENTRY = (
    "The committee chair who decides what your AI is allowed to say "
    "once asked his intern to download a PDF into Word, then blamed "
    "the printer."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate check, mirroring RULES.txt: 1 to 320 characters, not only
    # whitespace, exactly one sentence. Fail loudly instead of writing
    # an invalid entry.
    # Joke structure, three beats (K21): (1) authority set up — the chair
    # decides what your AI may say; (2) the turn — he cannot convert a
    # PDF, so he makes his intern do it; (3) the punch — he blamed the
    # printer. Scene, not saying (K20): a named chair, an intern, a file.
    assert 1 <= len(ENTRY) <= 320, "entry must be 1-320 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), (
        "entry must be exactly one sentence"
    )
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
