"""One-off: collapse fine-grained luminosity_class values (e.g. Ia, Iab/Ib, III-IV)
into the seven canonical MK classes (I–VII). Overwrites the CSV in place."""

from __future__ import annotations

from pathlib import Path

MAIN_CLASSES = ["VII", "VI", "V", "IV", "III", "II", "I"]


def to_main_class(lc: str) -> str:
    for mc in MAIN_CLASSES:
        if lc.startswith(mc):
            return mc
    return ""


def main() -> None:
    csv_path = Path(__file__).resolve().parent / "data" / "hr.csv"
    lines = csv_path.read_text().splitlines()

    header = lines[0].split(",")
    col_idx = header.index("luminosity_class")

    out = [lines[0]]
    for line in lines[1:]:
        fields = line.split(",")
        fields[col_idx] = to_main_class(fields[col_idx])
        out.append(",".join(fields))

    csv_path.write_text("\n".join(out) + "\n")
    print(f"Collapsed luminosity classes in {csv_path} ({len(lines) - 1} rows)")


if __name__ == "__main__":
    main()
