# Jobsheet Lengkap 15 — Integrasi Analisis Data

Dokumen ini melengkapi `Jobsheet.md`.

## 1. Data Dictionary
Tuliskan nama kolom, satuan, jenis data raw/derived, dan maknanya.

## 2. Quality Check
Periksa nilai kosong, satuan, rentang PF, konsistensi rpm, daya, serta hubungan antarvariabel yang relevan.

## 3. Program
```bash
python program/analyze_lab_csv.py
python program/multi_machine_diagnostics.py
node program/report.js program/lab_data.csv
```

## 4. Studi Kasus
Gunakan `multi_machine_cases.csv`. Pilih minimal tiga case dari jenis mesin berbeda. Untuk setiap case tuliskan:
- gejala;
- baseline;
- dua kemungkinan penjelasan;
- data yang dapat membedakan kedua kemungkinan;
- kesimpulan sementara;
- tingkat keyakinan.

## 5. Besaran Turunan
Gunakan hanya rumus yang sesuai dengan dataset: kecepatan sudut, daya mekanik, efisiensi, `Ns`, slip, daya tiga fasa, atau deviasi relatif.

## 6. Grafik
Buat sedikitnya tiga grafik yang membantu analisis. Jelaskan fungsi setiap grafik, bukan hanya tampilannya.

## 7. Repeat Data
Jika tersedia pengulangan, bandingkan apakah penyimpangan muncul kembali dan apakah keyakinan terhadap hipotesis berubah.

## 8. Pertanyaan
1. Mengapa baseline penting?
2. Apa beda outlier dan kesimpulan akhir?
3. Mengapa perlu lebih dari satu hipotesis?
4. Mengapa satuan harus diperiksa lebih dahulu?
5. Mengapa korelasi tidak otomatis berarti penyebab?
6. Apa manfaat repeat data?

## Output
Data dictionary, quality check, tiga studi kasus, derived metrics, tiga grafik, kesimpulan, confidence level, dan keterbatasan analisis.