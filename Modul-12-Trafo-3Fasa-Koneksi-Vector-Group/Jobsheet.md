# Jobsheet 12 — Transformator 3 Fasa

## Percobaan A — Identifikasi
Catat rating tiap winding dan polaritas. Bila memakai tiga trafo 1 fasa, pastikan unit identik dan ditujukan untuk bank trainer.

## Percobaan B — Koneksi Y-Y / Δ-Y
Lakukan hanya koneksi yang ditetapkan instruktur. Ukur `VLine` dan `VPhase` primer/sekunder.

| Koneksi | VL1 | Vph1 | VL2 | Vph2 | ratio line | shift observasi |
|---|---:|---:|---:|---:|---:|---|
|||||||

## Program
```bash
python program/three_phase_transformer.py
```
Program menghitung rasio line dan menggambar phasor sederhana.

## Analisa
1. Mengapa Δ-Y memiliki faktor sqrt(3) pada line ratio?
2. Apa arti clock number vector group?
3. Mengapa dua transformator tidak boleh diparalelkan sembarangan?
4. Bedakan neutral availability pada Y dan Δ.

P12 memakai `Project.md` sebagai deliverable utama, bukan TugasVideo.