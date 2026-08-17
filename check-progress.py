#!/usr/bin/env python3
"""
Reports real progress through IaC-Fundamentals-Bootcamp by checking whether
each module's solution file still matches the untouched stub, or has actual
work in it. The README checkboxes are manual and easy to forget to update,
this checks the actual files instead.

Run from the same directory that contains IaC-Fundamentals-Bootcamp/:
    python3 check_progress.py
"""

from pathlib import Path

REPO_NAME = "IaC-Fundamentals-Bootcamp"

STUB_MARKERS = (
    "# Solution - write your work here",
    "// Solution - write your work here",
)

SECTIONS = ["powershell", "bicep-arm-json", "terraform"]


def is_stub(solution_path: Path) -> bool:
    content = solution_path.read_text().strip()
    return content in STUB_MARKERS or content == ""


def find_solution_file(module_path: Path) -> Path | None:
    matches = list(module_path.glob("solution.*"))
    return matches[0] if matches else None


def check_section(base: Path, section: str) -> tuple[list[str], list[str]]:
    section_path = base / section
    if not section_path.exists():
        return [], []

    started, not_started = [], []
    for module_path in sorted(section_path.iterdir()):
        if not module_path.is_dir():
            continue
        solution_file = find_solution_file(module_path)
        if solution_file is None:
            continue
        if is_stub(solution_file):
            not_started.append(module_path.name)
        else:
            started.append(module_path.name)
    return started, not_started


def main():
    base = Path(REPO_NAME)
    if not base.exists():
        print(f"Can't find {REPO_NAME}/ in the current directory. Run this from wherever the repo lives.")
        return

    total_started, total_modules = 0, 0
    print(f"Progress report for {REPO_NAME}\n")

    for section in SECTIONS:
        started, not_started = check_section(base, section)
        count = len(started) + len(not_started)
        if count == 0:
            continue
        total_started += len(started)
        total_modules += count
        pct = (len(started) / count * 100) if count else 0
        print(f"{section}: {len(started)}/{count} modules started ({pct:.0f}%)")
        if not_started:
            print(f"  Not started yet: {', '.join(not_started)}")
        print()

    if total_modules:
        overall_pct = total_started / total_modules * 100
        print(f"Overall: {total_started}/{total_modules} modules started ({overall_pct:.0f}%)")
    else:
        print("No modules found. Has the repo been built yet?")


if __name__ == "__main__":
    main()