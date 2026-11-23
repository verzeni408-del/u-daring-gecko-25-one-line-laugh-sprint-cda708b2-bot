"""One-line laugh entry for the make.fun sprint.

The program writes one original joke line to the output directory,
using only the standard library.
"""

import os

ENTRY = "I bought noise-cancelling headphones to hear myself think, and discovered I have nothing to say."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
