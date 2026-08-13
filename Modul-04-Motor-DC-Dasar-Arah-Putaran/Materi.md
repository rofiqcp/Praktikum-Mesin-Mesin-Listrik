# Modul 04 — Motor DC: Prinsip, Back-EMF, Torsi, Kecepatan, dan Arah Putaran

**Pertemuan:** 4 dari 16  
**Durasi:** 3 × 50 menit  
**Fokus:** konversi listrik-mekanik pada motor DC dan model steady-state dasar.

## 1. Capaian
Mahasiswa mampu menjelaskan konstruksi motor DC, back-EMF, hubungan torsi-arus, pengaruh tegangan terhadap kecepatan, prinsip perubahan arah, arus awal, daya mekanik, dan efisiensi.

## 2. Bagian Utama
- stator/medan: menghasilkan fluks magnet;
- rotor/jangkar: membawa arus dan menghasilkan torsi;
- komutator: membalik hubungan kumparan rotor secara mekanis;
- brush/sikat: antarmuka listrik ke komutator;
- poros dan bearing: menyalurkan daya mekanik.

## 3. Persamaan Tegangan Jangkar
Model steady-state sederhana:

```text
V = E + Ia Ra
E = V - Ia Ra
```

`E` adalah back electromotive force (back-EMF), `Ia` arus jangkar, dan `Ra` resistansi jangkar.

## 4. Back-EMF
Saat rotor berputar di dalam medan magnet, timbul tegangan induksi yang arahnya menentang sumber. Secara konseptual:

```text
E = ke Phi omega
```

Jika fluks relatif tetap, back-EMF meningkat saat kecepatan meningkat.

## 5. Torsi Elektromagnetik

```text
T = kt Phi Ia
```

Untuk fluks tetap, torsi berbanding lurus dengan arus jangkar. Karena itu arus merupakan indikator penting beban motor, walaupun tidak sama langsung dengan torsi pada semua kondisi nyata.

## 6. Kecepatan
Dari hubungan back-EMF:

```text
omega ≈ (V - Ia Ra) / (ke Phi)
```

Konsep penting:
- tegangan lebih tinggi cenderung menaikkan kecepatan untuk kondisi lain serupa;
- kenaikan beban menaikkan arus dan jatuh tegangan `IaRa`, sehingga kecepatan dapat turun;
- perubahan fluks juga mengubah kecepatan dan torsi.

## 7. Mengapa Arus Awal Besar?
Saat kecepatan mendekati nol, back-EMF juga mendekati nol. Model awal:

```text
I_start ≈ V / Ra
```

Karena `Ra` biasanya kecil, model memprediksi arus awal jauh lebih besar dari arus steady-state. Pada trainer, fenomena ini diamati sesuai batas dan prosedur laboratorium.

## 8. Arah Putaran
Arah torsi ditentukan oleh hubungan arah fluks dan arah arus jangkar. Secara konseptual, membalik salah satu di antara fluks atau arus jangkar membalik arah torsi. Jika keduanya dibalik bersamaan, arah torsi tetap.

Pada P4 pembahasan dibatasi pada prinsip fisika dan pengamatan trainer/simulasi. Logika kontaktor forward-reverse untuk motor AC dibahas terpisah pada P7.

## 9. Jenis Motor DC

### Shunt
Medan terhubung paralel terhadap jangkar. Kecepatan relatif stabil terhadap perubahan beban.

### Series
Arus medan mengikuti arus jangkar. Torsi awal dapat tinggi dan karakteristik kecepatannya berbeda dari shunt.

### Separately excited
Medan mendapat sumber terpisah sehingga fluks dapat dikendalikan independen.

### Permanent magnet DC
Fluks utama berasal dari magnet permanen dan banyak digunakan pada sistem daya kecil-menengah.

## 10. Daya dan Efisiensi

```text
Pin = V Ia
omega = 2 pi n / 60
Pmech = T omega
eta = Pmech / Pin × 100%
```

Model rugi dapat dikelompokkan menjadi rugi tembaga, brush/contact loss, rugi mekanik, dan rugi magnetik.

## 11. Data Minimum P4

| Variabel | Satuan | Keterangan |
|---|---|---|
| V | V | tegangan jangkar |
| Ia | A | arus jangkar |
| n | rpm | kecepatan |
| Ra | ohm | resistansi model |
| E | V | estimasi back-EMF |
| T | N.m | torsi bila tersedia |
| Pin | W | daya listrik |
| Pmech | W | daya mekanik |
| eta | % | efisiensi |
| arah | - | CW/CCW sesuai konvensi pengamatan |

## 12. Contoh Hitung
Diketahui `V=24 V`, `Ia=2 A`, `Ra=1.2 ohm`, `n=1200 rpm`, dan `T=0.25 N.m`.

```text
E = 24 - 2(1.2) = 21.6 V
omega = 2 pi (1200)/60 = 125.66 rad/s
Pin = 48 W
Pmech = 31.42 W
eta = 65.46%
```

Nilai contoh dipakai untuk melatih alur hitung, bukan sebagai rating universal motor.

## 13. Program Wajib

```bash
python motor_dc_start.py
python motor_dc_sweep.py
```

Program digunakan untuk mengamati pengaruh `V`, `Ia`, `Ra`, dan rpm terhadap back-EMF serta besaran mekanik. Mahasiswa mengubah parameter contoh dan mencatat pola perubahan.

## 14. Grafik yang Dipersiapkan
P4 mengenalkan grafik dasar:
- tegangan terhadap estimasi kecepatan;
- arus terhadap estimasi torsi;
- kecepatan terhadap back-EMF.

Analisis berbeban yang lebih lengkap diteruskan pada P5 agar tidak terjadi overlay.

## 15. Pertanyaan Konseptual
1. Mengapa motor belum mempunyai back-EMF besar saat diam?
2. Mengapa arus awal dapat tinggi?
3. Mengapa beban mekanik memengaruhi arus?
4. Apa beda daya listrik dan daya mekanik?
5. Apa yang menentukan arah torsi?
6. Mengapa P4 dan P5 dipisahkan?

## 16. Ringkasan
Motor DC adalah contoh langsung konversi listrik-mekanik. P4 membangun fondasi `V → Ia → fluks/back-EMF → torsi → kecepatan → daya`, sedangkan P5 akan mempelajari karakteristik berbeban secara lebih sistematis.