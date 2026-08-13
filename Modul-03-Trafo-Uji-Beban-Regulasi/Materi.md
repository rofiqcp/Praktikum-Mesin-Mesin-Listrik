# Modul 03 — Transformator Berbeban: Regulasi, Rugi, dan Efisiensi

**Pertemuan:** 3 dari 16  
**Durasi:** 3 × 50 menit  
**Fokus:** analisis perubahan tegangan, arus, daya, regulasi, rugi, dan efisiensi ketika kondisi beban berubah.

> Seluruh data hardware diperoleh melalui trainer dan prosedur laboratorium yang ditetapkan dosen/laboran. Materi ini berfokus pada teori, pembacaan dataset, dan analisis hasil.

---

## 1. Capaian Pembelajaran

Mahasiswa mampu:

1. menjelaskan mengapa tegangan sekunder berubah ketika arus beban berubah;
2. menghitung regulasi tegangan;
3. membedakan rugi inti dan rugi tembaga;
4. menghitung daya masuk, daya keluar, rugi total, dan efisiensi;
5. menjelaskan pengaruh faktor daya terhadap karakteristik tegangan;
6. membaca dan mengolah dataset berbeban;
7. membuat kurva `V2-I2`, regulasi, dan efisiensi;
8. memverifikasi hasil Python/Octave dengan perhitungan manual.

---

## 2. Hubungan P2 dan P3

P2 mempelajari kondisi tanpa beban dan cabang magnetisasi. P3 menambahkan pengaruh arus beban. Dengan demikian:

```text
P2: magnetisasi + rugi inti
P3: P2 + impedansi seri + rugi tembaga + perubahan tegangan + efisiensi
```

Tujuan keduanya berbeda sehingga tidak overlay.

---

## 3. Model Ekivalen Sederhana

Bagian seri transformator dapat ditulis:

```text
Zeq = Req + jXeq
```

- `Req`: resistansi ekivalen kumparan;
- `Xeq`: reaktansi bocor ekivalen.

Saat arus meningkat, jatuh tegangan pada impedansi ekivalen juga meningkat. Karena itu tegangan terminal sekunder dapat berbeda dari kondisi tanpa beban.

---

## 4. Regulasi Tegangan

Definisi yang digunakan pada modul ini:

```text
VR(%) = (V2_noload - V2_load) / V2_load × 100%
```

Interpretasi:

- `VR` kecil: tegangan relatif stabil;
- `VR` besar: perubahan tegangan akibat beban lebih signifikan;
- kondisi faktor daya berbeda dapat menghasilkan regulasi berbeda.

Beberapa referensi memakai denominator `V2_noload`. Karena itu laporan harus selalu mencantumkan rumus yang dipakai.

---

## 5. Rugi Transformator

### 5.1 Rugi inti

Dibahas pada P2 dan pada kondisi tegangan/frekuensi yang serupa sering diperlakukan sebagai komponen yang relatif konstan.

### 5.2 Rugi tembaga

```text
Pcu = I^2 R
```

Konsekuensi penting: jika arus naik dua kali dan `R` dianggap tetap, rugi tembaga meningkat sekitar empat kali.

### 5.3 Rugi tambahan

Model dasar tidak memasukkan seluruh fenomena nyata. Selisih antara model dan dataset dapat mencakup stray loss, perubahan temperatur, ketelitian instrumen, dan asumsi parameter konstan.

---

## 6. Daya dan Efisiensi

Untuk sisi keluaran AC:

```text
Pout = V2 I2 cos(phi)
```

Efisiensi:

```text
eta = Pout / Pin × 100%
```

Rugi total dari dataset:

```text
Ploss = Pin - Pout
```

Efisiensi tidak harus maksimum pada beban penuh. Secara umum efisiensi meningkat dari beban ringan menuju titik optimum, lalu dapat menurun ketika rugi tembaga menjadi dominan.

---

## 7. Pengaruh Faktor Daya

Faktor daya memengaruhi daya aktif dan karakter jatuh tegangan. Pendekatan sederhana regulasi:

```text
VR ≈ (I2 Req cos(phi) ± I2 Xeq sin(phi)) / V2 × 100%
```

Tanda bergantung pada konvensi dan jenis faktor daya. Yang paling penting pada P3 adalah memahami bahwa sudut arus memengaruhi kontribusi `Req` dan `Xeq` terhadap perubahan tegangan.

---

## 8. Dataset Minimum

| Variabel | Satuan | Makna |
|---|---|---|
| load_pct | % | tingkat beban |
| V1 | V | tegangan sisi masuk |
| I1 | A | arus sisi masuk |
| Pin | W | daya aktif masuk |
| V2 | V | tegangan sisi keluar |
| I2 | A | arus sisi keluar |
| pf | - | faktor daya beban |
| Pout | W | daya aktif keluar |
| reg | % | regulasi |
| eta | % | efisiensi |
| loss | W | rugi total |

---

## 9. Kurva yang Wajib Dipahami

### 9.1 `V2` terhadap `I2`
Menunjukkan seberapa stabil tegangan ketika beban meningkat.

### 9.2 Regulasi terhadap persentase beban
Menunjukkan perubahan kualitas tegangan relatif terhadap kondisi tanpa beban.

### 9.3 Efisiensi terhadap persentase beban
Menunjukkan titik operasi yang paling efisien pada dataset.

### 9.4 Rugi tembaga relatif terhadap arus
Menunjukkan sifat kuadratik `I²R`.

---

## 10. Contoh Perhitungan

Diketahui:

```text
V2_noload = 110 V
V2_load   = 104 V
I2        = 2.0 A
PF        = 0.8
Pin       = 180 W
```

Maka:

```text
VR = (110-104)/104 × 100% = 5.77%
Pout = 104 × 2 × 0.8 = 166.4 W
eta = 166.4/180 × 100% = 92.44%
Ploss = 180 - 166.4 = 13.6 W
```

---

## 11. Program Wajib

```bash
python trafo_regulasi.py
```

Program membaca `data_trafo.csv`, menghitung besaran turunan, mencari titik efisiensi tertinggi pada dataset, dan menyimpan grafik.

Untuk Octave/MATLAB gunakan:

```text
trafo_load.m
```

Mahasiswa wajib memverifikasi minimal satu baris hasil program secara manual.

---

## 12. Struktur Analisis Data

Setiap titik analisis idealnya mempunyai urutan:

```text
data mentah
→ validasi satuan
→ hitung Pout
→ hitung regulasi
→ hitung efisiensi
→ hitung rugi
→ plot
→ interpretasi
```

Jangan menghapus data yang dianggap aneh sebelum alasan teknisnya dijelaskan.

---

## 13. Analisis Error

```text
error(%) = |hasil_data - hasil_model| / |hasil_model| × 100%
```

Setelah menghitung error, identifikasi kemungkinan sumber:

- pembulatan data;
- variasi parameter;
- temperatur;
- ketelitian instrumen;
- faktor daya;
- rugi tambahan yang tidak masuk model.

---

## 14. Pertanyaan Konseptual

1. Mengapa `V2` dapat turun ketika `I2` naik?
2. Mengapa rugi tembaga bertambah cepat terhadap arus?
3. Mengapa efisiensi tidak selalu maksimum pada beban terbesar?
4. Mengapa faktor daya memengaruhi regulasi?
5. Apa perbedaan rugi inti dan rugi tembaga?
6. Apa keterbatasan model `Zeq` sederhana?
7. Mengapa satu titik data tidak cukup untuk menyimpulkan karakteristik?

---

## 15. Batas Materi

P3 menutup blok transformator 1 fasa dan **tidak** masuk ke motor DC atau kontrol kontaktor. P4 berpindah ke konversi listrik-mekanik dengan motor DC.

---

## 16. Ringkasan

Pertanyaan utama P3 adalah: **apa yang berubah ketika transformator membawa beban?** Jawabannya harus dibangun dari dataset tegangan, arus, daya, faktor daya, regulasi, rugi, dan efisiensi.