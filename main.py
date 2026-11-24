import os
from pathlib import Path

LINE = "We rent 10-minute naps inside parked hearses for $9 \u2014 the darkest, quietest sleep pods in the city, and funeral homes finally earn rent on vehicles that sit idle 22 hours a day."

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
