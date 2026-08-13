# Jobsheet 15 — Commissioning Data dan Diagnosis

## Skenario
Kelompok menerima satu trainer/dataset dengan beberapa anomali sengaja.

## Langkah
1. Identifikasi baseline/nameplate.
2. Verifikasi satuan dan sensor.
3. Ambil data yang diizinkan oleh SOP trainer.
4. Isi `program/lab_data.csv`.
5. Jalankan:
```bash
python program/analyze_lab_csv.py
node program/report.js program/lab_data.csv
```
6. Tandai outlier.
7. Buat minimal dua hipotesis.
8. Pilih pengukuran tambahan yang membedakan kedua hipotesis.
9. Susun kesimpulan berbasis bukti.

## Rubrik
Data 25%, reasoning 30%, grafik/perhitungan 20%, keselamatan 15%, rekomendasi 10%.

## Pertanyaan
1. Mengapa data perlu diulang saat anomali hanya muncul satu kali?
2. Bagaimana membedakan gangguan supply dan kenaikan beban?
3. Mengapa arus antar fasa perlu dibandingkan?
4. Apa bedanya korelasi dan penyebab?