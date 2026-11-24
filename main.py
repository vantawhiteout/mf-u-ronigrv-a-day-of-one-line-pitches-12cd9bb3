"""make.fun entry: one sentence aimed at a friend who has never coded.

The whole entry is PITCH below. The grader runs this program and reads
/output/entry.txt, so this file's only job is to write that sentence as UTF-8
text with no trailing newline, safely inside the 240-character gate.

The pitch is written for the judge's first criterion: make the case in one
read. It names the friend's exact problem (an idea, no way to build it), gives
the easy action (one sentence on make.fun), and closes with plain, low-risk
reasons to say yes (no coding, no cost, a prize if it wins).
"""

from pathlib import Path

PITCH = (
    "You've got an app idea stuck in your head and no clue how to build it? On "
    "make.fun, just describe it in one sentence and an AI agent builds your first "
    "app for you—no coding, no cost, and even a cash prize if it wins."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 240


def validate(text: str) -> str:
    """Keep the entry inside the scorer's gate: 1-240 chars, not blank."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"pitch must be 1-{MAX_CHARS} characters")
    if not text.strip():
        raise ValueError("pitch must not be only whitespace")
    return text


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the validated pitch to the grader-facing output path as UTF-8."""
    text = validate(PITCH)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
