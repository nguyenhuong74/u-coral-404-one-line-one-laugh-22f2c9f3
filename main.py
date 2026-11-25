"""One Line, One Laugh — writes a single funny line to /output/entry.txt."""

import os

LINE = "I hired an AI agent to do my job; it finished in an hour, then emailed HR asking why I still work here."


def validate(text):
    """Return (ok, reason): the line must be 1-200 chars, not only whitespace."""
    if not isinstance(text, str):
        return False, "not a string"
    if not 1 <= len(text) <= 200:
        return False, "length %d outside 1-200" % len(text)
    if not text.strip():
        return False, "only whitespace"
    return True, ""


def main():
    ok, reason = validate(LINE)
    if not ok:
        raise ValueError("line failed validation: %s" % reason)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
