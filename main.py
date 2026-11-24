"""One Letter for Your Day — entry letter: "C".

The word behind the letter is "caffeinated": a day run entirely on
coffee — jittery, bright-eyed, slightly trembling, but somehow getting
everything done. It is vivid (you can see the mug, the shaking hand),
funny (self-aware, the kind of thing you tell a friend), and true
(an ordinary day, honestly reported). "C" is the word's own initial.

This program writes exactly that one letter to /output/entry.txt:
one byte, no newline, nothing else.
"""

LETTER = "C"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    import os

    # The gate allows exactly one character, A-Z, and one byte on disk.
    # Check the encoded form, not just the character count.
    encoded = LETTER.encode("utf-8")
    if len(encoded) != 1 or not (b"A" <= encoded <= b"Z"):
        raise SystemExit("entry must be exactly one letter A-Z")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)

    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != LETTER.encode("utf-8"):
        raise SystemExit("output mismatch: entry.txt is not the letter")


if __name__ == "__main__":
    main()
