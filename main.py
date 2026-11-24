"""Ridiculous startup pitch runner: writes the locked line to entry.txt.
Verified by running: 177 characters, 179 bytes, 1 period, byte-identical
across runs (output sha256 0b485422eb0a1efb5857433bc55f3a786d64f40305d0a661739933587d2ae439)."""
import os
from pathlib import Path

LINE = "We rent 10-minute naps inside parked hearses for $9 \u2014 the darkest, quietest sleep pods in the city, and funeral homes finally earn rent on vehicles that sit idle 22 hours a day."

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
