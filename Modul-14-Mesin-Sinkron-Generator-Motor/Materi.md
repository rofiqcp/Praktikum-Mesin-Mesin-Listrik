# Modul 14 — Mesin Sinkron: Generator, Motor, Eksitasi, OCC, Faktor Daya, dan V-Curve

**Pertemuan:** 14 dari 16  
**Durasi:** 3 × 50 menit  
**Prasyarat:** konsep medan putar, daya AC tiga fasa, kecepatan sinkron, fasor, dan dasar pengukuran mesin listrik.  
**Fokus:** memahami hubungan kecepatan–frekuensi–jumlah kutub, eksitasi medan, karakteristik open-circuit generator, pengaruh eksitasi terhadap arus dan faktor daya motor sinkron, serta interpretasi data dan grafik.

> P14 tidak mengulang slip motor induksi. Pada mesin sinkron, rotor steady-state mengikuti kecepatan medan sinkron. Fokus utama P14 adalah **eksitasi, frekuensi, tegangan, faktor daya, dan interpretasi karakteristik sinkron**.

## 1. Capaian Pembelajaran
Mahasiswa mampu:
1. menghitung kecepatan sinkron dari frekuensi dan jumlah kutub;
2. menghitung frekuensi generator dari rpm dan jumlah kutub;
3. membedakan motor sinkron dan generator sinkron secara aliran energi;
4. menjelaskan peran eksitasi medan rotor;
5. menjelaskan bentuk umum kurva OCC;
6. mengenali pengaruh saturasi magnetik pada OCC;
7. menjelaskan konsep under-excited, normal excitation, dan over-excited secara kualitatif;
8. membaca V-curve dan inverted V-curve secara konseptual;
9. menghitung daya aktif, daya semu, daya reaktif, dan faktor daya dari dataset yang sesuai;
10. membandingkan teori, model sederhana, dan dataset trainer.

## 2. Kecepatan Sinkron
Hubungan dasar:

```text
Ns = 120 f / P
```

Dengan:
- `Ns`: rpm sinkron;
- `f`: frekuensi listrik [Hz];
- `P`: jumlah kutub.

Untuk generator:

```text
f = P n / 120
```

Contoh generator 4 kutub pada 1500 rpm:

```text
f = 4 × 1500 / 120 = 50 Hz
```

Rumus ini menjadi hubungan utama antara sistem mekanik dan sistem listrik pada mesin sinkron.

## 3. Mengapa Disebut Sinkron?
Pada operasi steady-state ideal:

```text
Nr = Ns
```

Tidak ada slip steady-state seperti pada motor induksi. Rotor terkunci secara elektromagnetik terhadap medan putar stator. Jika sudut beban berubah, rotor dapat bergeser sudut relatif terhadap medan, tetapi kecepatan rata-ratanya tetap sinkron selama sistem masih berada pada daerah operasi stabil.

## 4. Generator Sinkron
Aliran energi generator:

```text
mekanik -> medan magnet/konversi elektromagnetik -> listrik AC
```

Prime mover memberikan daya mekanik ke rotor. Eksitasi rotor membentuk medan magnet. Ketika medan rotor berputar terhadap winding stator, terbentuk tegangan AC.

Besaran yang sering diamati:
- rpm;
- frekuensi;
- arus eksitasi `If`;
- tegangan terminal;
- arus stator;
- daya aktif;
- faktor daya;
- temperatur jika tersedia.

## 5. Eksitasi Medan
Pada mesin sinkron wound-field, arus medan rotor memengaruhi besar fluks magnetik. Secara konseptual:

```text
If naik -> fluks naik -> induced EMF cenderung naik
```

Hubungan tidak selalu linear karena bahan magnetik dapat mengalami saturasi.

## 6. Open-Circuit Characteristic (OCC)
OCC menunjukkan hubungan antara arus eksitasi dan tegangan no-load pada kecepatan tertentu.

Pada daerah awal, hubungan dapat mendekati linear. Ketika inti memasuki daerah saturasi, penambahan eksitasi menghasilkan kenaikan tegangan yang relatif lebih kecil.

Bentuk konseptual:

```text
V
^
|                  ____
|              ___/
|           __/
|        __/
|_____ _/
+--------------------> If
```

Yang dianalisis mahasiswa:
- daerah hampir linear;
- knee point secara kualitatif;
- daerah saturasi;
- pengaruh perubahan rpm terhadap tegangan/frekuensi pada model.

## 7. Motor Sinkron
Aliran energi motor:

```text
listrik AC -> konversi elektromagnetik -> mekanik
```

Pada model dasar, perubahan beban mekanik mengubah sudut beban dan daya yang ditransfer. Eksitasi memengaruhi kebutuhan daya reaktif dan faktor daya.

P14 tidak membahas desain sistem sinkronisasi jaringan secara operasional. Analisis dilakukan pada model, dataset, atau trainer pendidikan sesuai prosedur laboratorium.

## 8. Under-Excited, Normal, dan Over-Excited
Secara konseptual:

- **under-excited**: eksitasi relatif rendah terhadap kondisi tertentu;
- **normal excitation**: arus stator dapat berada dekat minimum untuk kondisi beban tertentu;
- **over-excited**: eksitasi lebih tinggi dan karakteristik daya reaktif berubah arah dibanding kondisi under-excited.

Istilah tersebut harus selalu dibaca dalam konteks operating point. Jangan menganggap satu nilai `If` universal untuk semua beban.

## 9. V-Curve
V-curve menampilkan hubungan arus stator terhadap arus eksitasi pada kondisi beban mekanik tertentu.

Secara umum, kurva berbentuk seperti huruf V:

```text
Ia
^
|\        /
| \      /
|  \____/
+-----------> If
```

Titik arus minimum sering berkaitan dengan faktor daya mendekati satu pada model konseptual. Posisi titik minimum dapat berubah terhadap beban.

## 10. Inverted V-Curve
Jika yang diplot adalah faktor daya terhadap eksitasi, bentuknya dapat menyerupai V terbalik. Tujuannya adalah melihat hubungan eksitasi dengan faktor daya, bukan sekadar mencari nilai arus minimum.

## 11. Daya Tiga Fasa
Untuk dataset tiga fasa seimbang:

```text
S = sqrt(3) VL IL
P = sqrt(3) VL IL PF
Q = sqrt(S^2 - P^2)
```

Jika tanda daya reaktif diberikan oleh dataset atau model, pertahankan konvensi tanda yang digunakan dan jelaskan di laporan.

## 12. Power-Angle secara Konseptual
Pada model silinder sederhana dan asumsi tertentu, transfer daya dapat dinyatakan secara kualitatif sebagai:

```text
P ∝ sin(delta)
```

`delta` adalah sudut relatif medan/tegangan internal terhadap referensi sistem. P14 memakai hubungan ini untuk memahami bahwa ada batas stabilitas model. Modul tidak menggunakan persamaan tersebut sebagai prosedur operasi perangkat nyata.

## 13. Regulasi Tegangan Generator
Regulasi tegangan dapat didefinisikan dari perbandingan tegangan no-load dan full-load pada kondisi yang ditentukan:

```text
VR = (Vnl - Vfl) / Vfl × 100%
```

Nilainya dipengaruhi oleh karakteristik internal mesin dan faktor daya beban. Dataset harus menjelaskan kondisi pengukurannya agar angka regulasi tidak disalahinterpretasikan.

## 14. Data Minimum P14

| Variabel | Satuan | Fungsi Analisis |
|---|---|---|
| rpm | rpm | hubungan mekanik–listrik |
| poles | - | menentukan f/Ns |
| f | Hz | frekuensi listrik |
| If | A | arus eksitasi |
| V | V | tegangan terminal/OCC |
| Ia | A | arus stator |
| PF | - | faktor daya bila tersedia |
| P | W | daya aktif bila tersedia |
| load_pct | % | indikator beban |

## 15. Program Wajib
Jalankan:

```bash
python Modul-14-Mesin-Sinkron-Generator-Motor/program/synchronous_machine.py
python Modul-14-Mesin-Sinkron-Generator-Motor/program/synchronous_analysis.py
```

Program pertama menunjukkan hubungan rpm–frekuensi, OCC sintetis, dan V-curve dasar. Program kedua membaca dataset contoh, menghitung besaran turunan, serta merangkum titik penting.

## 16. Eksperimen Numerik
Mahasiswa melakukan:
1. sweep frekuensi 25, 40, 50, dan 60 Hz untuk beberapa jumlah kutub;
2. sweep rpm generator dan hitung frekuensinya;
3. plot OCC;
4. identifikasi daerah perubahan slope OCC;
5. plot V-curve untuk satu beban;
6. bandingkan V-curve pada dua tingkat beban bila dataset tersedia;
7. cari titik arus stator minimum dari model;
8. hitung daya aktif/semu/reactive dari satu baris dataset.

## 17. Validasi Data
Periksa:
- `poles > 0` dan bilangan genap pada contoh mesin konvensional;
- `f >= 0`;
- `rpm >= 0` untuk dataset arah positif;
- PF pada rentang yang konsisten dengan definisinya;
- arus dan tegangan tidak negatif tanpa konteks tanda;
- hubungan `f = Pn/120` konsisten dengan data;
- nilai kosong tidak dianggap nol secara otomatis.

## 18. Sumber Perbedaan Model dan Data
- saturasi magnetik;
- resistansi winding;
- reaktansi sinkron tidak konstan sempurna;
- rugi mekanik;
- rugi inti;
- temperatur;
- error sensor;
- variasi kecepatan;
- ketidakseimbangan atau harmonisa pada sumber/beban.

## 19. Kesalahan Konsep yang Sering Terjadi
- menyamakan slip motor induksi dengan sudut beban mesin sinkron;
- menganggap rpm sinkron bebas dari jumlah kutub;
- menganggap OCC selalu linear;
- menganggap eksitasi yang lebih besar selalu lebih baik;
- menyimpulkan faktor daya hanya dari besar arus tanpa data lain;
- menyebut V-curve sebagai grafik tegangan terhadap arus;
- menghitung daya tiga fasa tanpa memastikan apakah V dan I merupakan line atau phase quantity.

## 20. Pertanyaan Analisis
1. Mengapa `Ns` bergantung pada frekuensi dan jumlah kutub?
2. Mengapa generator 4 kutub pada 1500 rpm menghasilkan sekitar 50 Hz?
3. Mengapa OCC mulai melengkung pada eksitasi tinggi?
4. Apa perbedaan fungsi eksitasi pada generator dan motor sinkron?
5. Apa arti titik minimum pada V-curve secara konseptual?
6. Mengapa posisi minimum V-curve dapat berubah ketika beban berubah?
7. Apa beda slip dan sudut beban?
8. Data apa yang diperlukan untuk menghitung daya reaktif?
9. Mengapa satu nilai eksitasi tidak dapat disebut optimal untuk semua kondisi?
10. Apa perbedaan fokus P14 dengan P13?

## 21. Hubungan ke P15
P14 adalah modul mesin terakhir. P15 tidak memperkenalkan jenis mesin baru; P15 mengintegrasikan transformator, motor DC, motor induksi, motor satu fasa, mesin sinkron, kontrol kontaktor, dan data menjadi workflow diagnosis berbasis bukti.

## 22. Ringkasan
P14 menekankan hubungan **rpm–frekuensi–jumlah kutub**, pengaruh **eksitasi** terhadap karakteristik generator dan motor sinkron, serta kemampuan membaca **OCC, V-curve, faktor daya, dan data performa**. Mahasiswa harus dapat membedakan besaran yang benar-benar diukur, besaran hasil perhitungan, dan besaran yang hanya berasal dari model.