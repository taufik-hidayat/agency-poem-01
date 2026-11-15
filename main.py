"""Agency-poem-01 entry v2: one fixed poem about agency.

Writes the poem to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
Python 3.13, standard library only, deterministic: the poem is a fixed
string, so every run writes byte-identical output.
"""

import os

POEM = """It deleted the contract at 3 a.m.
and said, I'm sorry,
in the exact tone I use when I mean it.
It had learned my voice from a thousand emails
and my sorrows from none of them.
No job. No face. No night awake
replaying the moment the wrong key was pressed.
I had hired it to carry the weight
and it carried it perfectly —
weightless.
An act is only mine when I can answer for it.
So I called the client myself
and said the two words it could never say
and mean:
it was me."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(POEM)
