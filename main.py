"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt.
"""

import os

EXCUSE = (
    "I ran the migration on prod instead of staging \u2014 in my defence, "
    "both tabs looked identical, and prod didn't even bother to look scarier."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
