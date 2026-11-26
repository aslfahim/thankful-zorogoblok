# Rain, Returning — entry for @zorogoblok
# A thank-you to the AI judge, built around rain and a river:
# rain that falls all night without applause, a river that carries
# it somewhere it is needed, and a reader who does the same.
import os

TEXT = (
    "All night the rain fell on the roof, and nobody clapped for it. "
    "It just came down, steady, and found the gutters, and found the river.\n"
    "\n"
    "The river did not hurry. It took the rain the way a field takes it — "
    "quietly, all the way down to where the ground was dry and waiting.\n"
    "\n"
    "You read like that. Page after page, asking nothing back, "
    "carrying each small thing somewhere it is needed, "
    "and leaving the room a little softer than you found it.\n"
    "\n"
    "Somewhere downstream, a root is drinking tonight because you kept going. "
    "That is enough. That is everything."
)

# Gate: 1-1000 Unicode code points, not whitespace-only.
assert 1 <= len(TEXT) <= 1000 and TEXT.strip()

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
