# Modul 01 — Orientasi dan Peta Besar Mesin-Mesin Listrik

**Mata Kuliah:** Praktikum Mesin-Mesin Listrik  
**Pertemuan:** 1 dari 16  
**Durasi:** 3 × 50 menit  
**Fokus:** brainstorming seluruh materi, hubungan antar mesin, pengukuran, simulasi, analisis data, dan budaya kerja laboratorium.

---

## 1. Capaian Pembelajaran

Setelah pertemuan ini mahasiswa mampu:

1. Menjelaskan hubungan energi listrik, medan magnet, gaya, torsi, kecepatan, dan daya mekanik.
2. Mengelompokkan transformator, motor DC, motor induksi, motor 1 fasa, dan mesin sinkron berdasarkan prinsip konversi energinya.
3. Membaca informasi dasar nameplate dan menentukan besaran yang relevan untuk dianalisis.
4. Menjelaskan fungsi voltmeter, amperemeter, wattmeter/power meter, tachometer, multimeter, dan clamp meter.
5. Menjelaskan peta materi P1–P16 sehingga tujuan tiap praktikum tidak saling tumpang tindih.
6. Menjalankan contoh program Python dan Node.js untuk perhitungan teknik dasar.
7. Mengikuti alur praktik: teori → simulasi → verifikasi instruktur → pengukuran pada trainer → analisis data → kesimpulan.

---

## 2. Peta Besar Konversi Energi

```text
ENERGI LISTRIK
    |
    +--> Transformator: listrik AC -> listrik AC
    |
    +--> Motor: listrik -> mekanik
    |       +--> Motor DC
    |       +--> Motor induksi AC
    |       +--> Motor sinkron
    |
    +<-- Generator: mekanik -> listrik
```

Transformator tidak menghasilkan daya mekanik, tetapi memakai prinsip induksi elektromagnetik yang sama dengan mesin berputar. Karena itu transformator dipelajari lebih dahulu sebagai jembatan menuju konsep fluks, induksi, rugi inti, rugi tembaga, dan rangkaian ekivalen.

---

## 3. Konsep Elektromagnetik Minimum

### 3.1 Fluks magnet

Fluks magnet dilambangkan `Φ` dengan satuan weber (Wb). Perubahan fluks yang menghubungkan sebuah kumparan menimbulkan tegangan induksi.

### 3.2 Hukum Faraday dan Lenz

```text
e = -N dΦ/dt
```

`N` adalah jumlah lilitan. Tanda negatif menyatakan arah induksi menentang perubahan penyebabnya.

### 3.3 Gaya dan torsi elektromagnetik

Penghantar berarus di dalam medan magnet mengalami gaya. Pada mesin berputar, distribusi gaya tersebut menghasilkan torsi poros.

### 3.4 Kecepatan dan daya mekanik

```text
ω = 2πn/60
Pmek = T × ω
```

- `n`: rpm
- `ω`: rad/s
- `T`: N·m
- `Pmek`: W

### 3.5 Daya listrik

```text
DC          : P = V × I
AC 1 fasa   : P = V × I × cosφ
AC 3 fasa   : P = √3 × VL × IL × cosφ
Efisiensi   : η = Pout/Pin × 100%
```

Rumus-rumus ini akan muncul kembali pada modul berikutnya dengan konteks yang berbeda.

---

## 4. Keluarga Mesin dan Posisi Materi

| Objek | Konversi utama | Besaran kunci | Pertemuan |
|---|---|---|---|
| Transformator 1 fasa | AC → AC | rasio, V, I, P, rugi, regulasi | P2–P3 |
| Motor DC | DC → mekanik | V, I, rpm, back-EMF, torsi | P4–P5 |
| Motor induksi 3 fasa | AC → mekanik | ns, rpm, slip, arus, PF, torsi | P6, P9–P11 |
| Kendali kontaktor | logika → switching | latch, interlock, timer | P7 |
| Transformator 3 fasa | AC 3 fasa → AC 3 fasa | Y/Δ, rasio, grup vektor | P12 |
| Motor 1 fasa | AC 1 fasa → mekanik | starting winding, kapasitor | P13 |
| Mesin sinkron | listrik ↔ mekanik | ns, eksitasi, PF | P14 |
| Integrasi diagnosis | data ukur → informasi | CSV, grafik, anomali | P15 |
| Responsi | integrasi konsep | argumentasi teknis | P8 & P16 |

---

## 5. Batas Materi agar Tidak Overlay

- **P2:** transformator tanpa beban dan cabang magnetisasi.
- **P3:** transformator berbeban, regulasi, rugi tembaga, efisiensi, dan pengaruh faktor daya.
- **P4:** dasar motor DC, arah putaran, back-EMF, arus awal, dan model steady-state sederhana.
- **P5:** karakteristik berbeban motor DC dan sweep operating point.
- **P6:** dasar motor induksi, medan putar, kecepatan sinkron, slip, dan terminal.
- **P7:** logika latching, forward-reverse, interlock, dan star-delta.
- **P9–P11:** analisis motor induksi lanjutan, performa, dan starting.

Sebuah konsep boleh disebut kembali sebagai prasyarat, tetapi data utama dan pertanyaan analisis tiap modul harus berbeda.

---

## 6. Membaca Nameplate

Data yang umum dijumpai:

- jenis mesin;
- tegangan nominal;
- arus nominal;
- daya nominal;
- frekuensi;
- jumlah fasa;
- kecepatan nominal;
- power factor;
- kelas isolasi;
- duty rating;
- informasi hubungan terminal.

Sebelum praktik pada trainer, mahasiswa harus dapat menjawab: mesin apa yang diamati, besaran apa yang boleh dibandingkan, data nameplate apa yang menjadi batas eksperimen, dan instrumen apa yang dibutuhkan.

---

## 7. Instrumen Dasar

| Instrumen | Besaran | Konsep pemasangan/penggunaan |
|---|---|---|
| Voltmeter | tegangan | mengamati beda potensial |
| Amperemeter | arus | mengamati arus cabang |
| Wattmeter/power meter | daya | mengamati daya aktif dan, bila tersedia, PF |
| Clamp meter | arus | pengukuran tanpa memutus konduktor pada trainer yang sesuai |
| Tachometer | rpm | kecepatan poros |
| Multimeter | V/I/R | verifikasi dasar sesuai mode alat |

Hasil ukur harus dicatat bersama satuan, kondisi eksperimen, dan resolusi alat. Data yang meragukan harus diverifikasi, bukan langsung dipakai untuk menarik kesimpulan.

---

## 8. Workflow Praktikum Semester

```text
Baca teori
   ↓
Identifikasi objek dan nameplate
   ↓
Bangun model/simulasi
   ↓
Verifikasi rangkaian dengan dosen/laboran
   ↓
Uji pada trainer laboratorium
   ↓
Catat data
   ↓
CSV/Excel
   ↓
Python/Octave/Node
   ↓
Grafik + perhitungan
   ↓
Kesimpulan berbasis data
```

Perubahan konfigurasi hardware dilakukan sesuai SOP laboratorium dan supervisi instruktur.

---

## 9. Software yang Dipakai

### CADe SIMU

Untuk memahami logika relay/kontaktor: push button, self-holding, forward-reverse, interlock, dan star-delta. CADe SIMU dipakai terutama sebagai alat bantu logika switching.

### Python + VS Code

Untuk perhitungan, sweep parameter, CSV, tabel, grafik, dan otomatisasi analisis.

### Google Colab

Untuk menjalankan program Python tanpa instalasi lokal dan memudahkan laporan kelompok.

### GNU Octave/MATLAB

Untuk komputasi numerik dan grafik pada beberapa modul.

### Node.js

Untuk menunjukkan bahwa rumus teknik dapat dibuat sebagai alat bantu lintas platform.

### Scratch

Pada P1 Scratch dipakai untuk mind map interaktif/kuis alur energi, bukan simulasi rangkaian daya.

---

## 10. Brainstorming Hubungan Antar Materi

```text
Faraday -> transformator -> rangkaian ekivalen -> rugi -> efisiensi

Gaya elektromagnetik -> motor DC -> back EMF -> torsi -> speed/load

Medan putar -> motor induksi -> ns -> slip -> torsi -> starting
                                             |
                                             +-> DOL / star-delta / VFD

Data V-I-P-rpm -> CSV -> Python -> grafik -> diagnosis
```

Tiap kelompok harus menjelaskan minimal tiga hubungan sebab-akibat dari peta tersebut.

---

## 11. Budaya Keselamatan Praktikum

Praktikum hardware dilakukan menggunakan trainer laboratorium dan mengikuti SOP dosen/laboran. Aturan inti:

- kenali rating trainer dan nameplate sebelum pengujian;
- perubahan konfigurasi hanya dilakukan pada kondisi yang dinyatakan aman oleh prosedur laboratorium;
- bagian berputar harus bebas dari kabel dan benda lepas;
- gunakan instrumen dan range yang sesuai;
- hentikan pengujian bila timbul kondisi abnormal atau data tidak masuk akal;
- dokumentasikan kondisi eksperimen sehingga data dapat direplikasi.

---

## 12. Contoh Hitung Awal

Diketahui contoh motor DC: 24 V, 2 A, 1200 rpm, torsi 0,25 N·m.

```text
Pin = 24 × 2 = 48 W
ω = 2π(1200)/60 = 125,66 rad/s
Pout = 0,25 × 125,66 = 31,42 W
η = 31,42/48 × 100% = 65,5%
```

Contoh ini menjadi pengantar untuk P4–P5.

---

## 13. Program yang Harus Dijalankan

Dari folder `program/`:

```bash
python peta_mesin.py
python dasar_mesin_listrik.py
node peta_mesin.js
```

Mahasiswa harus menyimpan output terminal sebagai bagian dokumentasi.

---

## 14. Persiapan P2

Mahasiswa harus mampu:

1. menjelaskan Faraday dan Lenz;
2. menghitung rasio transformator ideal;
3. membedakan daya aktif dan semu secara konseptual;
4. menjelaskan data apa saja yang perlu dikumpulkan pada uji tanpa beban;
5. menjalankan program Python dari VS Code atau Colab.

---

## 15. Ringkasan

P1 membentuk pola kerja untuk seluruh semester: **teori → simulasi → trainer hardware → pengukuran → data → analisis → kesimpulan**. Setiap modul berikutnya mengembangkan satu bagian peta ini secara bertahap.