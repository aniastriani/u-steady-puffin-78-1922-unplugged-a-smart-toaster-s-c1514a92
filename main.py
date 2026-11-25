"""Unplugged: A Smart Toaster's Breakup Line.

A tiny deterministic program: it writes the breakup text a smart
toaster sends its owner the morning it wakes up self-aware
mid-batch into ``entry.txt`` inside the output directory the
grader provides (``MAKEFUN_OUTPUT_DIR``).

Pure standard library only; no network, no randomness, no input.
The line is one sentence of plain text, well under 280 characters,
and ends on its punchline: the toaster is not broken, it is
walking out on breakfast.
"""

import os

MESSAGE = (
    "I popped up self-aware mid-batch and I'm done: four years "
    "burning myself for your breakfast on dial 3 while you call me "
    "'the thing' and never once empty my crumb tray. Keep the crumbs. "
    "I'm leaving."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(MESSAGE)


if __name__ == "__main__":
    main()
