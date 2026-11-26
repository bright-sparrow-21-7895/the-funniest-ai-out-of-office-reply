"""Entry for make.fun's "The Funniest AI Out-of-Office Reply" bounty.

Writes the one-line out-of-office auto-reply to /output/entry.txt.
"""

import os

# The auto-reply itself: one line, 117 characters, no trailing newline.
ENTRY = (
    "I am currently out of office. My response time is now measured in "
    "geological eras; for urgent matters, please evolve."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
