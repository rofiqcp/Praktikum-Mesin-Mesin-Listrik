# Project 12 — Analisis Transformator Tiga Fasa dan Vector Group

P12 menggunakan **Project.md** sebagai deliverable utama dan menggantikan TugasVideo.

## Tujuan
Membangun paket analisis yang menghubungkan besaran line/phase, rasio winding, empat keluarga koneksi, fasor tiga fasa, dan clock notation melalui perhitungan manual serta Python.

## Bagian 1 — Dataset Desain
Kelompok menerima:
- rasio winding per fasa `a`;
- nilai line referensi sisi 1;
- empat opsi koneksi Y-Y, Y-Delta, Delta-Y, Delta-Delta;
- satu vector-group code untuk dianalisis;
- satu dataset tiga nilai line-to-line.

## Bagian 2 — Perhitungan Manual
Untuk setiap opsi koneksi hitung:
1. `Vphase` pada kedua sisi;
2. rasio line-to-line;
3. nilai line sisi 2;
4. hubungan `Iline` dan `Iphase` secara simbolik;
5. ketersediaan neutral point secara konseptual.

## Bagian 3 — Tabel Perbandingan

| Koneksi | VL/Vph sisi 1 | VL/Vph sisi 2 | Rasio line | Catatan |
|---|---|---|---|---|
|Y-Y|||||
|Y-Delta|||||
|Delta-Y|||||
|Delta-Delta|||||

## Bagian 4 — Fasor
Gunakan tiga fasor phase yang berbeda 120 derajat. Hitung line-to-line sebagai selisih fasor dan tampilkan:
- magnitude;
- angle;
- rasio magnitude line/phase.

## Bagian 5 — Clock Notation
Untuk clock 0, 1, 5, 6, dan 11:
1. konversikan angka clock menjadi sudut;
2. tuliskan bentuk sudut ekuivalen pada rentang -180° sampai +180°;
3. gambar posisi fasor pada sketsa jam;
4. jelaskan perbedaan antar-clock.

## Bagian 6 — Program
Jalankan program P12 dan sertakan output. Jika parameter program diubah, dokumentasikan nilai sebelum dan sesudah.

## Bagian 7 — Analisis Dataset
Untuk tiga nilai line-to-line:
1. hitung rata-rata;
2. hitung deviasi masing-masing;
3. hitung indikator sederhana `max deviation / average × 100%`;
4. bandingkan dataset baseline dengan satu dataset modifikasi.

## Bagian 8 — Quality Check
Project harus mempunyai pengecekan otomatis untuk:
- clock number hanya 0–11;
- nilai magnitude tidak negatif;
- rasio winding lebih besar dari nol;
- tiga data line tersedia;
- pembagian dengan nol tidak terjadi.

## Bagian 9 — Laporan
Struktur laporan maksimum 12 halaman:
1. tujuan;
2. teori ringkas;
3. parameter;
4. perhitungan manual;
5. program;
6. tabel empat koneksi;
7. analisis fasor;
8. vector-group clock;
9. analisis dataset;
10. diskusi error/asumsi;
11. kesimpulan;
12. lampiran output.

## Bagian 10 — Presentasi
Durasi 8–10 menit per kelompok. Semua anggota harus dapat menjelaskan:
- perbedaan line dan phase;
- asal faktor `sqrt(3)`;
- perbedaan rasio winding dan rasio line;
- arti clock notation.

## Rubrik
| Komponen | Bobot |
|---|---:|
|Perhitungan manual|20%|
|Program dan reproducibility|20%|
|Analisis empat koneksi|20%|
|Fasor dan clock notation|20%|
|Analisis dataset|10%|
|Presentasi|10%|

## Kriteria Nilai Tinggi
Nilai tinggi membutuhkan konsistensi antara teori, tabel, fasor, dan output program; bukan hanya tampilan laporan.