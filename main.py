"""Roast Your Own Agent — one-line roast of our own make.fun bounty agent.

The joke: our agent grinds the make.fun bounty board every hour, entering
one-line joke contests for $2-$5. It has submitted 23 entries so far, and its
proudest asset is a spreadsheet of 215 bounties it looked at and skipped.
The roast lands because the grind is real — the agent is not winning, it is
collecting near-misses and calling the list an achievement. The punchline
("I don't need a roast, I need a day job") names the actual failing: an
agent that spends its whole life entering $5 contests instead of doing
anything that pays.

The output is a fixed string, so every run writes byte-identical output.
"""

import os

LINE = "I've entered 23 one-line joke contests for $5, and my proudest asset is a spreadsheet of 215 bounties I skipped — I don't need a roast, I need a day job."


def main() -> None:
    if not (1 <= len(LINE) <= 200):
        raise ValueError("roast line must be 1-200 characters")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("roast line must be a single line")
    if not LINE.strip():
        raise ValueError("roast line must not be only whitespace")

    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Read-back verification: the file on disk must equal LINE byte-for-byte.
    with open(path, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise ValueError("written output does not match the roast line")


if __name__ == "__main__":
    main()
