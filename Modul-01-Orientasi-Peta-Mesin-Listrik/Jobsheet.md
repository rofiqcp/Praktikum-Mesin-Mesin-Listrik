# Jobsheet P01 — Orientasi dan Peta Mesin-Mesin Listrik

**Durasi:** 3 × 50 menit

## Tujuan
Mahasiswa mengidentifikasi keluarga mesin listrik, membaca nameplate, menghubungkan besaran listrik dan mekanik, memahami peta P1–P16, dan menjalankan analisis komputasi dasar.

## Pra-Lab
1. Apa perbedaan transformator dan motor?
2. Apa makna Hukum Faraday?
3. Apa beda rpm dan rad/s?
4. Mengapa mesin nyata mempunyai rugi-rugi?
5. Apa fungsi nameplate?

## Aktivitas 1 — Identifikasi
Amati contoh mesin atau data nameplate yang disediakan pengajar.

| No | Objek | V | I | Daya | f | Fasa | rpm | PF | Catatan |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |

## Aktivitas 2 — Peta Energi
| Objek | Input | Proses | Output | Rugi | Data analisis |
|---|---|---|---|---|---|
| Transformator | | | | | |
| Motor DC | | | | | |
| Motor induksi | | | | | |

## Aktivitas 3 — Simulasi Konseptual
Gunakan software simulasi yang tersedia untuk membuat model input-state-output sederhana. Catat empat state dan jelaskan transisinya. Fokus pada cara membaca diagram dan hubungan sebab-akibat.

## Aktivitas 4 — Python
```bash
python peta_mesin.py
```
Catat keluaran dan kelompokkan mesin berdasarkan konversi energinya.

## Aktivitas 5 — Node.js
```bash
node peta_mesin.js
```
Bandingkan hasilnya dengan program Python.

## Aktivitas 6 — Mind Map Semester
Buat mind map dengan minimal 12 node: Faraday, transformator, rugi inti, rugi tembaga, motor DC, back-EMF, motor induksi, kecepatan sinkron, slip, faktor daya, efisiensi, CSV, dan diagnosis.

## Latihan
1. Sistem DC 24 V dan 2 A: hitung daya listrik.
2. Poros 1200 rpm dengan torsi 0,25 N.m: hitung omega dan daya mekanik.
3. Trafo ideal N1=500, N2=100, V1=220 V: hitung V2.
4. Mesin induksi 4 kutub, 50 Hz, rotor 1440 rpm: hitung kecepatan sinkron dan slip.

## Analisis
1. Mengapa transformator dipelajari lebih dahulu?
2. Apa hubungan fluks dengan tegangan induksi?
3. Mengapa arus saja tidak cukup untuk menentukan efisiensi?
4. Apa beda nameplate dan dataset eksperimen?
5. Apa manfaat simulasi dan Python?
6. Mengapa satuan wajib dicatat?

## Output
Tabel identifikasi, peta energi, screenshot simulasi, output program, mind map, latihan, analisis, dan kesimpulan 150–250 kata.

## Rubrik
Identifikasi/peta 25%, simulasi 15%, program 15%, perhitungan 15%, mind map/analisis 20%, dokumentasi 10%.