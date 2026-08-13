from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MODULES = sorted(p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith("Modul-"))
errors = []
checked_refs = 0

explicit_program = re.compile(r"program/[A-Za-z0-9_.-]+\.(?:py|js|csv|md|m)(?![A-Za-z0-9_.-])")
backticked_file = re.compile(r"`([A-Za-z0-9_.-]+\.(?:py|js|csv|md|m))`")
command_file = re.compile(r"(?:python(?:3)?|node)\s+((?:program/)?[A-Za-z0-9_.-]+\.(?:py|js))(?![A-Za-z0-9_.-])")

common_docs = {
    "Materi.md", "Jobsheet.md", "TugasVideo.md", "Project.md",
    "README.md", "CHANGELOG.md", "KURIKULUM.md"
}
generated_outputs = {"report.md", "laporan.md"}

for module in MODULES:
    markdown_files = sorted(module.glob("*.md")) + sorted((module / "program").glob("*.md"))
    for md in markdown_files:
        text = md.read_text(encoding="utf-8")

        for marker in ("TODO", "FIXME", "TBD"):
            if marker in text:
                errors.append(f"{md.relative_to(ROOT)}: contains draft marker {marker}")

        if re.search(r"^#{1,6}\s+Analisa\s*$", text, flags=re.MULTILINE):
            errors.append(f"{md.relative_to(ROOT)}: use heading 'Analisis', not 'Analisa'")

        refs = set(explicit_program.findall(text))
        refs.update(backticked_file.findall(text))
        refs.update(command_file.findall(text))

        for raw in sorted(refs):
            if raw in common_docs or raw.lower() in generated_outputs:
                continue
            if raw in {"Node.js", "N.m"}:
                continue

            if raw.startswith("program/"):
                candidates = [module / raw]
            elif md.parent.name == "program":
                candidates = [md.parent / raw, module / raw]
            elif Path(raw).suffix.lower() in {".py", ".js", ".m", ".csv"}:
                candidates = [module / "program" / raw, module / raw]
            else:
                candidates = [module / raw]

            checked_refs += 1
            if not any(candidate.exists() for candidate in candidates):
                expected = " or ".join(str(c.relative_to(ROOT)) for c in candidates)
                errors.append(
                    f"{md.relative_to(ROOT)}: broken local reference '{raw}' "
                    f"(expected {expected})"
                )

print(f"Modules checked: {len(MODULES)}")
print(f"Local references checked: {checked_refs}")

if errors:
    for error in errors:
        print("ERROR", error)
    sys.exit(1)

print("Readiness OK: no draft markers, deprecated Analisa headings, or broken local references found.")
