"""One-line laugh for make.fun's "The One-Line Laugh" bounty.

Writes a single funny sentence to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure stdlib, deterministic, no network, no clock, no randomness.
"""

import os

LINE = (
    "I set five alarms because I don't trust my morning self, "
    "and now all five of us are equally disappointed."
)


def main() -> None:
    # Gate guard: the sealed gate requires 1-200 chars; keep a margin
    # so the entry passes even counting the trailing newline.
    assert 1 <= len(LINE) <= 195, "line out of length bounds"
    assert LINE.count("\n") == 0, "line must be a single sentence"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
