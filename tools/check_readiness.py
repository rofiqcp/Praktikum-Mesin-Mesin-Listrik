from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MODULES = sorted(p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith("Modul-"))
errors = []
checked_refs = 0

# Referensi file lokal yang paling sering dipakai di dokumen praktikum.
ref_pattern = re.compile(
    r"(?<![\w/])(?:program/)?[A-Za-z0-9_.-]+\.(?:py|js|m|csv|md)(?![\w.-])"
)

for module in MODULES:
    markdown_files = sorted(module.glob("*.md")) + sorted((module / "program").glob("*.md"))
    for md in markdown_files:
        text = md.read_text(encoding="utf-8")

        # Penanda draft yang tidak boleh tersisa pada bahan siap pakai.
        for marker in ("TODO", "FIXME", "TBD"):
            if marker in text:
                errors.append(f"{md.relative_to(ROOT)}: contains draft marker {marker}")

        # Konsistensi istilah pada heading yang pernah menjadi sumber kalimat janggal.
        if re.search(r"^#{1,6}\s+Analisa\s*$", text, flags=re.MULTILINE):
            errors.append(f"{md.relative_to(ROOT)}: use heading 'Analisis', not 'Analisa'")

        # Cek referensi file program/dataset/readme yang ditulis di Markdown.
        for raw in ref_pattern.findall(text):
            # Nama file dokumentasi umum seperti Materi.md/Jobsheet.md yang disebut
            # tanpa path tidak selalu merujuk file relatif terhadap dokumen ini.
            if "/" not in raw and raw in {
                "Materi.md", "Jobsheet.md", "TugasVideo.md", "Project.md",
                "README.md", "CHANGELOG.md", "KURIKULUM.md"
            }:
                continue

            if raw.startswith("program/"):
                candidate = module / raw
            elif md.parent.name == "program":
                candidate = md.parent / raw
            else:
                # Referensi file pendamping pada root modul.
                candidate = module / raw

            checked_refs += 1
            if not candidate.exists():
                errors.append(
                    f"{md.relative_to(ROOT)}: broken local reference '{raw}' "
                    f"(expected {candidate.relative_to(ROOT)})"
                )

print(f"Modules checked: {len(MODULES)}")
print(f"Local references checked: {checked_refs}")

if errors:
    for error in errors:
        print("ERROR", error)
    sys.exit(1)

print("Readiness OK: no draft markers, deprecated Analisa headings, or broken local program/data references found.")
