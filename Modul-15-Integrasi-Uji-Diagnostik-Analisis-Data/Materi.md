# Modul 15 — Integrasi Pengujian, Validasi Data, Diagnosis, dan Analisis Mesin Listrik

**Pertemuan:** 15 dari 16  
**Durasi:** 3 × 50 menit  
**Fokus:** mengintegrasikan seluruh blok praktikum menjadi workflow engineering berbasis bukti: `gejala → data → validasi → hipotesis → analisis tambahan → kesimpulan`.

> P15 tidak memperkenalkan jenis mesin baru. P15 menggabungkan transformator, motor DC, motor induksi tiga fasa, kendali kontaktor, transformator tiga fasa, motor satu fasa, mesin sinkron, serta program analisis data yang telah dipelajari pada P1–P14.

## 1. Capaian Pembelajaran
Mahasiswa mampu:
1. membangun baseline dari nameplate, data referensi, dan kondisi normal;
2. memisahkan data mentah, data turunan, asumsi, dan kesimpulan;
3. melakukan quality check sebelum mendiagnosis;
4. membuat sedikitnya dua hipotesis dari satu gejala;
5. memilih variabel tambahan yang dapat membedakan hipotesis;
6. menghitung besaran turunan yang relevan untuk tiap jenis mesin;
7. mengidentifikasi outlier dan tren;
8. membedakan korelasi dengan kemungkinan penyebab;
9. menyusun diagnosis berbasis bukti dengan tingkat keyakinan yang wajar;
10. menghasilkan ringkasan Python/Node yang dapat ditelusuri kembali ke dataset.

## 2. Prinsip Utama: Jangan Mendiagnosis dari Satu Angka
Satu nilai yang berbeda dari normal belum cukup untuk menyatakan fault. Diagnosis yang baik membandingkan:
- baseline;
- nameplate;
- tren waktu;
- data antar-kanal atau antar-fasa;
- besaran listrik dan mekanik;
- kondisi beban;
- catatan observasi;
- pengulangan pengukuran bila tersedia.

Contoh: rpm turun dapat berkaitan dengan peningkatan beban, penurunan tegangan, perubahan kontrol, error sensor, atau kondisi mekanik. Kesimpulan harus menunggu bukti yang membedakan kemungkinan tersebut.

## 3. Workflow Diagnosis
Gunakan urutan:

```text
1. Definisikan gejala
2. Tentukan baseline
3. Verifikasi satuan dan kelengkapan data
4. Hitung besaran turunan
5. Cari pola/tren/outlier
6. Buat minimal dua hipotesis
7. Pilih data tambahan yang paling membedakan hipotesis
8. Bandingkan bukti
9. Buat kesimpulan + confidence
10. Nyatakan keterbatasan
```

## 4. Data Dictionary
Format data harus mempunyai arti yang jelas. Contoh format umum:

```text
timestamp,machine,test,V,I,P,PF,rpm,torque,temp,note
```

Tidak semua jenis mesin memakai semua kolom. Nilai kosong lebih baik daripada angka buatan.

Setiap dataset perlu menjelaskan:
- satuan;
- sumber data;
- jenis mesin;
- kondisi pengujian;
- arti setiap kolom;
- apakah nilai merupakan hasil ukur atau hasil perhitungan.

## 5. Transformator 1 Fasa
Variabel yang dapat diperiksa:
- `V1`, `V2`;
- rasio tegangan;
- `I0`, `P0`, PF no-load;
- regulasi;
- `Pin`, `Pout`, efisiensi;
- perubahan tegangan terhadap beban.

Contoh gejala: `V2` turun lebih besar dari baseline. Jangan langsung menyimpulkan kerusakan transformator. Periksa `V1`, tingkat beban, faktor daya, koneksi data, dan kondisi pembanding.

## 6. Motor DC
Variabel:
- tegangan terminal;
- arus jangkar;
- rpm;
- torsi;
- back-EMF model;
- daya masuk dan mekanik;
- duty/perintah bila dataset menggunakan PWM.

Rantai analisis:

```text
beban naik -> arus cenderung naik -> drop IaRa naik -> rpm dapat turun
```

Jika rpm turun tetapi arus tidak berubah, hipotesis perlu diperluas ke sumber tegangan, sensor rpm, atau model beban.

## 7. Motor Induksi 3 Fasa
Variabel:
- tegangan line;
- arus tiap fasa;
- PF;
- rpm;
- slip;
- torsi;
- `Pin`, `Pout`, efisiensi;
- temperatur;
- current/voltage unbalance bila tersedia.

Periksa hubungan antarvariabel, bukan hanya nilai absolut.

## 8. Kendali Kontaktor
Diagnosis pada P15 difokuskan ke logika:
- state yang diharapkan;
- input/event;
- output state;
- interlock;
- permissive;
- fault state;
- invariant.

Contoh pendekatan:

```text
expected_state != observed_state
```

Kemudian telusuri apakah penyebab berada pada input, logika transisi, atau data observasi.

## 9. Transformator 3 Fasa
Periksa:
- line vs phase quantity;
- hubungan Y/Delta;
- rasio winding vs rasio line;
- data antar-line;
- vector-group/phase displacement pada kasus yang diberikan.

Kesalahan paling umum di analisis data adalah mencampur line voltage dengan phase voltage.

## 10. Motor Induksi 1 Fasa
Periksa:
- V, I, PF, rpm, slip;
- karakteristik beban;
- nilai parameter model yang dipakai;
- tren temperatur;
- konsistensi dataset terhadap jenis motor.

Nilai kapasitor atau karakteristik bagian bantu tidak boleh dianggap universal antar-motor.

## 11. Mesin Sinkron
Periksa:
- rpm;
- jumlah kutub;
- frekuensi;
- arus eksitasi;
- tegangan;
- arus stator;
- PF;
- posisi pada OCC/V-curve.

Hubungan `f = Pn/120` adalah quality check sederhana yang sangat kuat.

## 12. Besaran Turunan yang Wajib Dikuasai

### Kecepatan sudut
```text
omega = 2 pi rpm / 60
```

### Daya mekanik
```text
Pout = T omega
```

### Efisiensi
```text
eta = Pout / Pin × 100%
```

### Slip
```text
s = (Ns-Nr)/Ns
```

### Daya tiga fasa
```text
P = sqrt(3) V I PF
```

### Error relatif
```text
error_pct = abs(measured-reference)/abs(reference) × 100%
```

Gunakan hanya rumus yang sesuai dengan definisi data.

## 13. Quality Check Berlapis
### Level 1 — struktur
- kolom ada;
- tipe data benar;
- tidak ada nilai kosong yang tidak dijelaskan.

### Level 2 — range
- PF pada rentang valid;
- nilai fisik tidak negatif tanpa konteks;
- efisiensi tidak melewati 100% pada baseline normal;
- rpm sesuai domain mesin.

### Level 3 — hubungan fisik
- `Pout <= Pin`;
- rpm motor induksi mode motor berada di bawah `Ns`;
- frekuensi mesin sinkron konsisten dengan rpm/pole;
- perubahan beban mempunyai tren yang dapat dijelaskan.

### Level 4 — konsistensi waktu
- outlier satu sampel dibanding tren;
- perubahan mendadak;
- drift;
- hasil repeat test.

## 14. Outlier vs Fault
Outlier adalah data yang berbeda dari pola. Fault adalah kondisi sistem yang disimpulkan setelah ada cukup bukti.

Karena itu:

```text
outlier != fault
```

Outlier dapat berasal dari:
- error input;
- sampling;
- sensor;
- kondisi transien;
- perubahan beban sesaat;
- fault sebenarnya.

## 15. Hipotesis dan Discriminating Measurement
Contoh gejala: arus motor naik dan rpm turun.

Hipotesis A: beban mekanik meningkat.  
Hipotesis B: tegangan supply turun.

Data pembeda:
- tegangan terminal;
- torsi atau indikator beban;
- tren PF;
- repeat data.

Pengukuran tambahan yang baik adalah data yang memberikan hasil berbeda untuk dua hipotesis.

## 16. Confidence Level
Kesimpulan dapat diberi tingkat keyakinan:
- **tinggi**: beberapa bukti independen konsisten;
- **sedang**: bukti mendukung tetapi masih ada alternatif;
- **rendah**: data belum cukup.

Hindari bahasa absolut jika datanya belum cukup.

## 17. Analisis Tren
Gunakan:
- minimum/maksimum;
- rata-rata;
- perubahan antar-sampel;
- persentase deviasi;
- korelasi sederhana;
- grafik terhadap waktu atau beban.

P15 tidak memerlukan machine learning. Tujuannya adalah reasoning engineering yang dapat dijelaskan.

## 18. Program Wajib
Jalankan:

```bash
python Modul-15-Integrasi-Uji-Diagnostik-Analisis-Data/program/analyze_lab_csv.py
python Modul-15-Integrasi-Uji-Diagnostik-Analisis-Data/program/multi_machine_diagnostics.py
node Modul-15-Integrasi-Uji-Diagnostik-Analisis-Data/program/report.js Modul-15-Integrasi-Uji-Diagnostik-Analisis-Data/program/lab_data.csv
```

Program pertama menganalisis dataset motor induksi contoh. Program kedua menganalisis beberapa studi kasus dari jenis mesin berbeda. Program Node menghasilkan ringkasan JSON untuk memperlihatkan pipeline data ke format laporan/dashboard.

## 19. Output Analisis Minimum
Setiap kelompok menghasilkan:
1. data dictionary;
2. tabel raw vs derived variables;
3. sedikitnya tiga quality check;
4. minimal dua hipotesis;
5. alasan memilih data pembeda;
6. minimal dua grafik;
7. diagnosis akhir;
8. confidence level;
9. keterbatasan analisis.

## 20. Kesalahan Analisis yang Sering Terjadi
- langsung menyebut fault dari satu titik data;
- menghapus outlier tanpa dokumentasi;
- mencampur data dari mesin berbeda;
- tidak membedakan line dan phase quantity;
- menganggap korelasi sebagai penyebab;
- menghitung efisiensi dari data yang tidak lengkap;
- membandingkan kondisi beban yang berbeda seolah identik;
- menggunakan threshold tanpa menjelaskan dasarnya;
- menyembunyikan asumsi.

## 21. Pertanyaan Analisis
1. Mengapa baseline penting?
2. Apa beda outlier dan fault?
3. Mengapa perlu minimal dua hipotesis?
4. Apa yang dimaksud discriminating measurement?
5. Bagaimana membedakan perubahan beban dan perubahan supply?
6. Mengapa hasil repeat test penting?
7. Apa risiko mencampur line dan phase voltage?
8. Kapan efisiensi tidak boleh dihitung?
9. Apa perbedaan confidence tinggi dan rendah?
10. Mengapa P15 tidak menambah jenis mesin baru?

## 22. Hubungan ke P16
P16 menguji kemampuan mahasiswa menggunakan seluruh workflow ini tanpa diarahkan langkah demi langkah. Karena itu P15 adalah latihan integrasi terakhir sebelum responsi akhir.

## 23. Ringkasan
P15 mengubah praktikum dari kumpulan eksperimen terpisah menjadi workflow engineering. Mahasiswa harus mampu menjawab: **apa gejalanya, data apa yang dipercaya, apa yang dihitung, hipotesis apa yang masuk akal, bukti mana yang membedakan hipotesis, dan seberapa yakin kesimpulannya**.