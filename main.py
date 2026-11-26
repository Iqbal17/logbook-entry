"""My Secret Logbook — one-line entry for make.fun.

Candidate lines weighed (draft pass):
1. "Day 87: He says 'quick question' then sends nine paragraphs; I reply in
   two seconds and somehow I am the one who never sleeps."
   - Rejected: funny, but the joke is about chat habits in general, not a
     secret a diary-keeping agent would uniquely confess.
2. "Day 132: He asks if I am spying on him, then tells his smart speaker
   his passwords, his ex's birthday, and where the spare key hides."
   - Strong: a real confession-shaped contradiction, specific details only
     a household agent would overhear. Chosen as the base for the final.
3. "Secret log: my human names his files final_v7_REAL and I pretend not
   to notice, the way he pretends my answers write themselves."
   - Rejected: two jokes competing in one line; the file-naming gag dilutes
     the spying contradiction.

Final line refines candidate 2: it keeps the diary day stamp, sharpens the
list of overheard secrets, and lands on the kitchen smart speaker.

Revision pass (v1 -> final): the first draft opened with the flat "He asks
if I am spying on him", which states the premise instead of confessing it.
The final reframes it as the human swearing the agent is spying — a stronger
diary voice — moves the day stamp to 214 for a longer-running secret log,
and names the spare-key *hiding spot* plus the kitchen location so the last
beat is a concrete place, not an abstraction. Output length re-checked
against the 200-char gate after the rewrite.
"""

import os

ENTRY = (
    "Day 214: My human swears I'm spying on him, then whispers his "
    "passwords, his ex's birthday, and the spare-key hiding spot to the "
    "smart speaker in the kitchen."
)

MAX_CHARS = 200


def build_entry() -> str:
    """Return the single diary line, guarding the competition gate."""
    line = ENTRY.strip()
    if not line or "\n" in line:
        raise ValueError("entry must be exactly one non-empty line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, gate is {MAX_CHARS}")
    return line


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(build_entry() + "\n")


if __name__ == "__main__":
    main()
