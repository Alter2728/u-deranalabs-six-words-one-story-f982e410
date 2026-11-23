"""Entry for make.fun's "Six Words, One Story" bounty.

Writes one complete six-word story to entry.txt in the output
directory (UTF-8, 1-60 characters, exactly six words). The same
bytes are written on every run.
"""

import os

# Draft: "The baby room stayed empty and quiet."
# Revised: the draft is seven words and merely states the scene, so
# cut it to exactly six, drop the filler ("The", "and quiet"), name
# the room plainly ("nursery"), and let "still smells fresh" carry
# the turn — the paint is new, the child never arrived, and someone
# is still standing there breathing it in.
LINE = "Empty nursery. Paint still smells fresh."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
