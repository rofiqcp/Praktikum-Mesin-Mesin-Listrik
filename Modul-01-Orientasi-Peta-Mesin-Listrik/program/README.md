# Program P01 — Orientasi Mesin-Mesin Listrik

Folder ini berisi contoh paling awal untuk membiasakan mahasiswa mengubah persamaan teknik menjadi program yang dapat dijalankan dan diverifikasi.

## 1. Peta Konsep Python

```bash
python peta_mesin.py
```

Output mencakup:
- keluarga mesin listrik;
- jenis konversi energi;
- variabel utama tiap mesin;
- rasio transformator ideal;
- contoh daya motor DC;
- kecepatan sinkron dan slip;
- contoh daya aktif 3 fasa.

## 2. Kalkulator Dasar

```bash
python dasar_mesin_listrik.py
```

Script ini dibuat lebih sederhana agar mahasiswa pemula mudah mengubah parameter dan membandingkan hasil.

Eksperimen:
1. ubah `N1`, `N2`, dan `V1`;
2. ubah `V`, `I`, `rpm`, dan `torque`;
3. ubah `f`, `poles`, dan `Nr`;
4. jelaskan perubahan output untuk setiap kasus.

## 3. Node.js

```bash
node peta_mesin.js
```

Tujuannya menunjukkan bahwa konsep fisika yang sama dapat diterapkan menggunakan bahasa pemrograman berbeda.

## 4. Google Colab

Upload file Python lalu jalankan:

```python
!python peta_mesin.py
!python dasar_mesin_listrik.py
```

## 5. Bukti yang Dikumpulkan

- screenshot terminal;
- minimal dua modifikasi parameter;
- tabel input-output;
- interpretasi 3–5 kalimat;
- satu kesimpulan tentang hubungan rumus dan program.

## 6. Catatan

P01 belum mengejar model mesin yang kompleks. Fokusnya adalah memastikan mahasiswa memahami **variabel, satuan, persamaan, eksekusi program, dan interpretasi output** sebelum masuk P02.