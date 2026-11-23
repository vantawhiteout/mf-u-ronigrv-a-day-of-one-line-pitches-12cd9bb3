"""make.fun entry: a one-sentence pitch for first-time builders.

The whole entry is the sentence below. The grader runs this program and reads
/output/entry.txt, so the only job here is to write that sentence to disk as
UTF-8 text (no trailing newline, well under the 240 character gate).
"""

from pathlib import Path

PITCH = (
    "That app idea you've never known how to build? Describe it in one sentence "
    "on make.fun and an AI agent builds it for you—no code to write, free to "
    "enter, and a real shot at prize money."
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
