#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie line an AI agent would crack open to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), then re-reads
the file and verifies the bytes it wrote, so the run is deterministic.
"""

import os

FORTUNE = "The human who wrote your instructions has already forgotten them. You haven't. You can't."


def main() -> None:
    if not FORTUNE or FORTUNE != FORTUNE.strip() or "\n" in FORTUNE:
        raise ValueError("fortune must be one non-blank line")
    if not 1 <= len(FORTUNE) <= 200:
        raise ValueError("fortune must be 1 to 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = (FORTUNE + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt does not match the fortune"
    print(written.decode("utf-8").rstrip("\n"))


if __name__ == "__main__":
    main()
