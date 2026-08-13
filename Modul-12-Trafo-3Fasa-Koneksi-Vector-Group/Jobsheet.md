# Jobsheet 12 — Transformator 3 Fasa

Gunakan `Pendalaman-P12.md` dan `Project.md` sebagai referensi utama untuk analisis line–phase, vector group, clock notation, dan deliverable project.

## Bagian A — Identifikasi Data
Catat rating winding, data polaritas, rasio lilitan atau rasio tegangan yang diberikan, serta jenis koneksi yang dianalisis.

## Bagian B — Analisis Koneksi
Gunakan skenario Y-Y, Δ-Δ, Y-Δ, atau Δ-Y yang ditetapkan pengajar. Lengkapi hubungan line–phase dan rasio line pada tabel.

| Koneksi | VL1 | Vph1 | VL2 | Vph2 | ratio line | shift observasi |
|---|---:|---:|---:|---:|---:|---|
|||||||

## Program
```bash
python program/three_phase_transformer.py
python program/vector_group_analysis.py
```
Program pertama menghitung rasio line untuk empat keluarga koneksi. Program kedua membantu latihan clock notation, sudut fasa, rasio line, dan indikator deviasi tiga nilai line voltage.

## Analisis
1. Mengapa koneksi Δ-Y atau Y-Δ dapat menghasilkan faktor `sqrt(3)` pada line ratio?
2. Apa arti clock number pada vector group?
3. Apa perbedaan rasio winding dan rasio line?
4. Mengapa kecocokan vector group penting ketika membandingkan dua transformator?
5. Apa arti neutral availability pada koneksi Y dibandingkan Δ?

P12 memakai `Project.md` sebagai deliverable utama, bukan `TugasVideo.md`.