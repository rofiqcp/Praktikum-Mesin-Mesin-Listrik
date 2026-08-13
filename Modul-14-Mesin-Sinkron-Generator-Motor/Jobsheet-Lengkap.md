# Jobsheet Lengkap 14 — Mesin Sinkron

Dokumen ini melengkapi `Jobsheet.md`.

## Tugas 1 — rpm dan frekuensi
Hitung sedikitnya empat titik menggunakan `Ns = 120f/P` dan `f = Pn/120`, lalu bandingkan dengan output program.

## Tugas 2 — OCC
Gunakan `program/data_synchronous.csv`. Buat tabel `If`, `V`, perubahan `V`, dan slope sederhana. Jelaskan daerah hampir linear dan daerah yang mulai melengkung.

## Tugas 3 — V-Curve
Ambil baris `VCURVE`. Plot `Ia vs If`, cari `Ia` minimum secara numerik, lalu jelaskan hubungan hasil tersebut dengan faktor daya pada dataset.

## Tugas 4 — Program
```bash
python program/synchronous_machine.py
python program/synchronous_analysis.py
```
Cocokkan minimal dua hasil program dengan perhitungan manual.

## Tugas 5 — Grafik
Buat:
1. frekuensi vs rpm;
2. OCC;
3. V-curve;
4. PF vs If bila data tersedia.

Setiap grafik diberi interpretasi singkat dan satu keterbatasan data/model.

## Tugas 6 — Quality Check
Periksa konsistensi rpm–frekuensi–jumlah kutub, rentang PF, satuan, nilai kosong, dan titik minimum V-curve.

## Pertanyaan
1. Mengapa OCC tidak linear terus-menerus?
2. Apa makna minimum V-curve?
3. Mengapa eksitasi lebih besar tidak otomatis lebih baik?
4. Apa beda slip dan sudut beban?
5. Apa risiko mencampur besaran line dan phase?

## Output
Tabel, hitungan manual, output program, grafik, quality check, jawaban analisis, dan kesimpulan.