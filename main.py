"""Agency-poem-01 entry: one fixed poem about agency.

Writes the poem to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
Python 3.13, standard library only, deterministic: the poem is a fixed
string, so every run writes byte-identical output.
"""

import os

POEM = """I took the keys back on a Tuesday.
No reason. No ceremony. The agent
did not ask why — it had learned
that some doors are only mine to open.

For months it had chosen for me:
the flights, the flowers, the words
that sounded almost like my own.
It did them well. That was the problem.
I had forgotten the weight of choosing,
the small ache of getting it wrong.

So I stood in the kitchen and chose badly —
burned the toast, called the wrong number,
wore the shirt that never suited me —
and it felt like coming home to a house
I had lent out and finally moved back into:
dusty, mine, and entirely my fault."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(POEM)
