"""Write one line of software error copy that says what actually broke.

The line names a real failure -- the server ran out of memory mid-request --
in plain words, tells the user nothing of theirs was lost, and gives the one
thing to do next: refresh and let the server finish its thought. One line,
under 200 characters, written to /output/entry.txt. Runs in a sandbox with
no network.
"""

import os

ENTRY = (
    "Our server ran out of memory and forgot your request mid-sentence. "
    "Nothing of yours was lost \u2014 refresh the page and let it finish "
    "its thought."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200  # the gate: /output/entry.txt must be 1 to 200 characters


def main() -> None:
    line = ENTRY.replace("\n", " ").strip()
    assert 1 <= len(line) <= MAX_CHARS, f"entry is {len(line)} characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
