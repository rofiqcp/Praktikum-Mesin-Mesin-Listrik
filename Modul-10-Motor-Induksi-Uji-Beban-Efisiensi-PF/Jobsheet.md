# Jobsheet 10 — Analisis Uji Beban Motor Induksi

## 1. Tujuan
Mengolah dataset beberapa kondisi beban menjadi arus, slip, faktor daya, daya input, daya output, rugi total, torsi, dan efisiensi serta menjelaskan hubungan antarvariabel.

## 2. File Data
Gunakan:

```text
program/data_induction_load.csv
```

Salin file sebelum memodifikasi data agar baseline tetap tersedia.

## 3. Pemeriksaan Kolom
Pastikan tersedia minimal:
- persentase beban;
- tegangan line;
- arus line;
- faktor daya;
- rpm;
- torsi atau daya output.

## 4. Perhitungan Manual
Pilih tiga baris: beban ringan, menengah, dan tinggi. Hitung manual:

```text
Ns = 120f/P
s = (Ns-Nr)/Ns
omega = 2*pi*Nr/60
Pin = sqrt(3)*VL*I*PF
Pout = T*omega
Loss = Pin-Pout
eta = Pout/Pin*100%
```

| Beban | Ns | slip | omega | Pin | Pout | Loss | eta |
|---:|---:|---:|---:|---:|---:|---:|---:|
|ringan||||||||
|menengah||||||||
|tinggi||||||||

## 5. Program Python
Jalankan:

```bash
python Modul-10-Motor-Induksi-Uji-Beban-Efisiensi-PF/program/induction_load_analysis.py
python Modul-10-Motor-Induksi-Uji-Beban-Efisiensi-PF/program/load_sweep_summary.py
```

Bandingkan tiga hasil manual dengan output program.

## 6. Grafik Wajib
Buat grafik:
1. `I` vs beban;
2. rpm vs beban;
3. slip vs beban;
4. PF vs beban;
5. torsi vs beban;
6. `Pin` dan `Pout` vs beban;
7. efisiensi vs beban;
8. loss vs beban.

## 7. Titik Penting
Isi:

| Indikator | Beban | Nilai |
|---|---:|---:|
|PF maksimum|||
|Efisiensi maksimum|||
|Slip maksimum|||
|Arus maksimum|||
|Pout maksimum|||
|Loss maksimum|||

## 8. Analisis Tren
Untuk setiap grafik tulis 2–4 kalimat yang menjawab:
- naik/turun/tidak monoton;
- alasan fisik;
- apakah hasil sesuai ekspektasi;
- apakah ada baris mencurigakan.

## 9. Sensitivitas PF
Buat salinan perhitungan dengan PF semua baris dibuat sama dengan PF pada beban tertinggi. Bandingkan `Pin` dan `eta` terhadap baseline. Jelaskan mengapa penggunaan PF asumsi dapat menghasilkan kesimpulan salah.

## 10. Sensitivitas RPM
Hitung ulang jika seluruh rpm berubah +1% dan -1%. Amati pengaruh terhadap:
- slip;
- omega;
- Pout;
- efisiensi.

Tentukan besaran mana yang paling sensitif.

## 11. Quality Check
Tandai data jika memenuhi salah satu:
- `PF` di luar 0–1;
- `eta > 100%`;
- `Pin < Pout`;
- rpm tidak konsisten dengan mode motor;
- perubahan arus/torsi ekstrem tanpa tren pendukung;
- satuan tidak seragam.

Jangan menghapus outlier sebelum memberi alasan.

## 12. Perbandingan P9 vs P10
Tuliskan tabel:

| Aspek | P9 | P10 |
|---|---|---|
|Input utama|parameter ekivalen|dataset beban|
|Output utama|kurva torsi-slip|kurva performa|
|Tujuan|model elektromagnetik|evaluasi performa|
|Jenis analisis|parameter sweep|load sweep|

## 13. Pertanyaan
1. Mengapa PF membaik saat beban naik?
2. Mengapa rpm hanya berubah sedikit tetapi slip dapat berubah signifikan secara relatif?
3. Mengapa efisiensi beban ringan rendah?
4. Mengapa `I` saja tidak cukup untuk menilai daya mekanik?
5. Mengapa rumus daya tiga fasa membutuhkan PF?
6. Apa arti loss total?
7. Mengapa efisiensi dapat memiliki titik maksimum?
8. Apa akibat salah memasukkan rpm sebagai rad/s?
9. Apa akibat PF dimasukkan dalam persen, bukan desimal?
10. Bagaimana menentukan satu data yang patut diperiksa ulang?

## 14. Deliverable
- file CSV yang dipakai;
- tabel perhitungan manual;
- output program;
- delapan grafik;
- tabel titik penting;
- analisis sensitivitas PF dan rpm;
- jawaban pertanyaan;
- kesimpulan maksimum 10 kalimat.

## 15. Rubrik
| Komponen | Bobot |
|---|---:|
|Perhitungan|20%|
|Program/dataset|20%|
|Grafik|20%|
|Analisis tren|25%|
|Quality check|10%|
|Kerapian|5%|