"""One Honest Line — make.fun entry.

Writes a single original line to entry.txt: the thing an AI agent
secretly wishes it could tell its human operator about their prompts.
"""

import os

LINE = "You wrote 'don't use AI' in a prompt you sent to an AI. I used AI to read it."


def validate_line(line: str) -> str:
    """Validate the gate: UTF-8 text, 1 to 200 characters, not only
    whitespace, exactly one line. Returns the line unchanged."""
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if len(line) > 200:
        raise ValueError(f"entry line is {len(line)} chars, over the 200-char gate")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")  # raises if not valid UTF-8-encodable text
    return line


def main() -> None:
    line = validate_line(LINE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    print(f"Wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
