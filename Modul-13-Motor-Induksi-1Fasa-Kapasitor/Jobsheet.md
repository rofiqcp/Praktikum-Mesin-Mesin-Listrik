# Jobsheet 13 — Analisis Motor Induksi 1 Fasa

## Tujuan
Mahasiswa menghubungkan teori motor satu fasa dengan data nameplate, dataset, perhitungan manual, dan program Python.

## A. Persiapan
Jawab sebelum praktikum:
1. Mengapa motor satu fasa memerlukan mekanisme pembentukan torsi awal?
2. Apa fungsi winding utama dan winding bantu?
3. Tuliskan rumus `Xc`, `Ns`, slip, `Pin`, `Pout`, dan efisiensi.
4. Apa perbedaan capacitor-start dan PSC?
5. Data apa yang wajib tersedia sebelum efisiensi dapat dihitung?

## B. Identifikasi Dataset
Isi tabel dari data yang diberikan pengajar atau file contoh.

| Item | Nilai | Satuan/Catatan |
|---|---:|---|
| Tegangan | | V |
| Frekuensi | | Hz |
| Jumlah kutub | | pole |
| Daya nominal | | W/kW |
| Arus nominal | | A |
| Kecepatan nominal | | rpm |
| Kapasitansi | | uF |
| Jenis motor | | |

## C. Perhitungan Awal
Hitung:

```text
Ns = 120 f / P
Xc = 1 / (2 pi f C)
s = (Ns - Nr) / Ns
```

Tuliskan satuan dan asumsi yang digunakan.

## D. Sweep Kapasitor
Jalankan:

```bash
python program/single_phase_capacitor.py
```

Isi tabel hasil:

| C (uF) | Xc @ 50 Hz | Xc @ 60 Hz | Interpretasi |
|---:|---:|---:|---|
||||

Jelaskan tren `C`, `f`, dan `Xc` dengan kalimat sendiri.

## E. Analisis Data Performa
Gunakan `program/data_single_phase.csv`, kemudian jalankan:

```bash
python program/single_phase_performance.py
```

Catat:
- arus maksimum;
- rpm minimum;
- slip maksimum;
- efisiensi terbaik bila data lengkap;
- quality flag yang muncul.

## F. Perhitungan Turunan
Untuk setiap baris dengan data lengkap:

```text
Pin   = V I PF
omega = 2 pi rpm / 60
Pout  = torque omega
eta   = Pout / Pin × 100%
slip  = (Ns-rpm) / Ns × 100%
```

Jika suatu variabel tidak tersedia, tuliskan `N/A`. Jangan membuat angka yang tidak berasal dari data atau asumsi yang dinyatakan jelas.

## G. Grafik Wajib
Buat minimal:
1. `Xc vs C`;
2. `I vs load_pct`;
3. `rpm vs load_pct`;
4. `slip vs load_pct`;
5. `eta vs load_pct` jika data cukup.

Setiap grafik diberi interpretasi 2–4 kalimat.

## H. Bandingkan Teori dan Data

| Aspek | Prediksi | Hasil data | Sesuai? | Penjelasan |
|---|---|---|---|---|
| Xc ketika C naik | | | | |
| rpm ketika beban naik | | | | |
| slip ketika beban naik | | | | |
| arus ketika beban naik | | | | |

## I. Quality Check
Periksa:
- PF berada pada rentang 0–1;
- satuan konsisten;
- rpm masuk akal terhadap `Ns`;
- `Pout <= Pin` pada dataset baseline normal;
- tidak ada pembagian dengan nol;
- nilai kosong tidak dianggap nol tanpa alasan.

## J. Pertanyaan Analisis
1. Mengapa winding bantu diperlukan pada banyak motor satu fasa?
2. Apa fungsi beda fasa arus utama dan bantu?
3. Mengapa kapasitor yang lebih besar tidak otomatis menghasilkan performa lebih baik?
4. Bagaimana kenaikan beban memengaruhi rpm dan slip?
5. Mengapa efisiensi tidak dapat dihitung hanya dari V, I, dan rpm?
6. Bagaimana membedakan anomali data dan perubahan karakteristik akibat beban?
7. Apa perbedaan fokus P13 dan P14?

## K. Struktur Laporan
1. Tujuan.
2. Identifikasi dataset.
3. Teori ringkas.
4. Perhitungan manual.
5. Output program.
6. Grafik.
7. Quality check.
8. Analisis.
9. Kesimpulan.

## Checklist Pengumpulan
- [ ] identifikasi data lengkap;
- [ ] hitungan manual disertakan;
- [ ] dua program dijalankan;
- [ ] minimal empat grafik;
- [ ] quality check dijelaskan;
- [ ] kesimpulan menghubungkan teori, program, dan data.

## Rubrik
Konsep 15%, data dan perhitungan 25%, program dan grafik 25%, analisis 25%, kualitas laporan 10%.