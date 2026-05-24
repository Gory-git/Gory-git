import random
from pathlib import Path

README_PATH = Path("README.md")
QUOTES_PATH = Path("quotes.txt")

START = "<!-- QUOTE:START -->"
END = "<!-- QUOTE:END -->"

def main():
    readme = README_PATH.read_text(encoding="utf-8")
    quotes = [q.strip() for q in QUOTES_PATH.read_text(encoding="utf-8").splitlines() if q.strip()]

    if not quotes:
        raise SystemExit("No quotes found in quotes.txt")

    if START not in readme or END not in readme:
        raise SystemExit("Markers not found in README.md")

    quote = random.choice(quotes)

    replacement = f"{START}\n> {quote}\n{END}"
    before = readme.split(START)[0]
    after = readme.split(END)[1]

    updated = before + replacement + after
    README_PATH.write_text(updated, encoding="utf-8")

if __name__ == "__main__":
    main()