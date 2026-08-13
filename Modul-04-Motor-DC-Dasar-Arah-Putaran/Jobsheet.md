# Jobsheet P04 — Motor DC Dasar: Back-EMF, Kecepatan, Arus, dan Arah

**Durasi:** 3 × 50 menit

## 1. Tujuan
Mahasiswa mampu menghubungkan tegangan, arus, back-EMF, kecepatan, torsi, dan arah putaran motor DC melalui perhitungan, simulasi, dan data trainer laboratorium.

## 2. Pra-Lab
1. Jelaskan fungsi komutator dan brush.
2. Turunkan `E = V - IaRa`.
3. Jelaskan mengapa `E` meningkat ketika rpm meningkat.
4. Jelaskan mengapa arus awal dapat lebih tinggi daripada arus steady-state.
5. Jelaskan kondisi konseptual yang dapat membalik arah torsi.

## 3. Data Motor
| Parameter | Nilai | Satuan |
|---|---:|---|
| Tegangan nominal | | V |
| Arus nominal | | A |
| Daya nominal | | W |
| Kecepatan nominal | | rpm |
| Resistansi model jangkar | | ohm |
| Torsi nominal/batas trainer | | N.m |

## 4. Kegiatan A — Model Back-EMF
Gunakan dataset yang diberikan pada sesi dan hitung `E = V - IaRa`.

| Titik | V | Ia | Ra | E | rpm | Catatan |
|---:|---:|---:|---:|---:|---:|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |

Analisis hubungan rpm dan back-EMF.

## 5. Kegiatan B — Arah Putaran
Catat konvensi arah yang digunakan pada trainer, misalnya CW sebagai positif. Gunakan data/observasi yang diberikan instruktur dan jelaskan perubahan arah berdasarkan hubungan fluks dan arus jangkar.

| Kondisi | Polaritas/konvensi A | Polaritas/konvensi B | Arah | Penjelasan |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

## 6. Kegiatan C — Daya Mekanik
Jika torsi tersedia pada dataset:

```text
omega = 2*pi*n/60
Pin = V*Ia
Pmech = T*omega
eta = Pmech/Pin*100%
```

| Titik | rpm | T | omega | Pin | Pmech | eta |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

## 7. Kegiatan D — Python

```bash
python motor_dc_start.py
python motor_dc_sweep.py
```

Lakukan minimal tiga variasi parameter dan catat dampaknya.

| Skenario | Parameter diubah | Nilai awal | Nilai baru | Output utama | Interpretasi |
|---|---|---:|---:|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

## 8. Grafik Wajib
1. `E` terhadap rpm.
2. estimasi torsi terhadap arus.
3. kecepatan terhadap tegangan untuk parameter model yang sama.

## 9. Pertanyaan Analisis
1. Mengapa back-EMF disebut counter-EMF?
2. Apa penyebab arus tinggi pada kondisi kecepatan sangat rendah?
3. Mengapa perubahan beban memengaruhi arus?
4. Jika `Ra` meningkat karena temperatur, bagaimana pengaruhnya terhadap `E` pada V dan Ia yang sama?
5. Mengapa membalik dua besaran sekaligus dapat mempertahankan arah torsi?
6. Apa keterbatasan model steady-state sederhana?
7. Mengapa P5 diperlukan setelah P4?

## 10. Output
Pra-lab, tabel data, satu perhitungan manual, tiga grafik, output program, jawaban analisis, dan kesimpulan 200–300 kata.

## 11. Rubrik
| Komponen | Bobot |
|---|---:|
| Pra-lab | 10% |
| Data/model | 20% |
| Perhitungan | 20% |
| Program | 20% |
| Grafik | 15% |
| Analisis dan kesimpulan | 15% |

## 12. Batas P4
P4 berhenti pada dasar motor DC dan model steady-state. Sweep karakteristik beban dan analisis performa lebih mendalam dilakukan pada P5.