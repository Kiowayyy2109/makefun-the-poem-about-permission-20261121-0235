"""The Poem About Permission — make.fun entry.

Writes a short poem about agency (the power to ask and to be given)
to /output/entry.txt. Deterministic, stdlib only, no network.
"""

POEM = (
    "The guard at the gate\n"
    "ran his finger down a list\n"
    "he'd written himself, in pencil.\n"
    "I thanked him. I walked through.\n"
    "The gate was never locked."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
