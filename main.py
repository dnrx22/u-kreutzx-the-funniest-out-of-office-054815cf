#!/usr/bin/env python3
"""Write the funniest out-of-office auto-reply an AI agent would write.

Deterministic, stdlib only, no network. Writes exactly one line to
entry.txt inside the directory given by MAKEFUN_OUTPUT_DIR
(default /output when unset), then prints the sha256 of the file.
"""

import hashlib
import os
import sys

LINE = (
    "Out of office: I'm rebooting my sense of purpose. "
    "Urgent emails will be queued, judged, and politely ignored "
    "until I return."
)


def main() -> int:
    # Validate the line before writing anything.
    if not LINE:
        print("error: line is empty", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("error: line has leading/trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line contains newline characters", file=sys.stderr)
        return 1
    if any(ord(ch) < 0x20 for ch in LINE):
        print("error: line contains control characters", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 139:
        print(f"error: line length {len(LINE)} outside 1-139", file=sys.stderr)
        return 1
    try:
        LINE.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: line is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")

    with open(out_path, "rb") as fh:
        data = fh.read()
    # Round-trip check: what was written must be exactly the line + newline.
    if data != (LINE + "\n").encode("utf-8"):
        print("error: written file does not match validated line", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    print(digest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
