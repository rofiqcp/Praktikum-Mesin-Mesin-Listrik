# Modul 02 — Transformator 1 Fasa: Dasar dan Uji Tanpa Beban

**Pertemuan:** 2 dari 16  
**Durasi:** 3 × 50 menit  
**Fokus:** prinsip transformator, model ideal vs nyata, arus tanpa beban, rugi inti, faktor daya tanpa beban, dan ekstraksi cabang magnetisasi.

---

## 1. Capaian Pembelajaran

Mahasiswa mampu:

1. menjelaskan kerja transformator berdasarkan Hukum Faraday;
2. menghitung rasio lilitan, rasio tegangan, dan hubungan arus ideal;
3. membedakan transformator ideal dan nyata;
4. menjelaskan arus magnetisasi, rugi histeresis, dan rugi arus eddy;
5. mengolah data uji tanpa beban menjadi `Rc` dan `Xm`;
6. membandingkan teori, data trainer, dan hasil program Python;
7. menyajikan hasil dalam tabel dan grafik yang dapat ditelusuri kembali.

---

## 2. Prinsip Kerja

Transformator memindahkan energi listrik antar kumparan melalui fluks magnet bersama pada inti. Sumber AC pada kumparan primer menghasilkan fluks berubah terhadap waktu. Fluks tersebut menginduksikan tegangan pada primer maupun sekunder.

Persamaan dasar tegangan induksi sinusoidal:

```text
E = 4.44 f N Phi_max
```

Untuk transformator ideal:

```text
V1/V2 = N1/N2 = a
I1/I2 = N2/N1 = 1/a
P1 = P2
```

`a` disebut rasio transformasi.

---

## 3. Transformator Ideal dan Nyata

Transformator ideal mengasumsikan:

- resistansi kumparan nol;
- tidak ada leakage flux;
- tidak ada rugi inti;
- permeabilitas inti sangat besar;
- efisiensi 100%.

Transformator nyata mempunyai:

- `R1` dan `R2`: resistansi kumparan;
- `X1` dan `X2`: reaktansi bocor;
- `Rc`: representasi rugi inti;
- `Xm`: reaktansi magnetisasi.

Pada P2 fokus berada pada **cabang paralel `Rc || jXm`**. Parameter seri akan dibahas lebih lanjut pada P3.

---

## 4. Mengapa Tetap Ada Arus Saat Sekunder Tidak Dibebani?

Walaupun sekunder terbuka, primer tetap menarik arus kecil `I0`. Arus ini mempunyai dua komponen utama:

- `Ic`: komponen yang berkaitan dengan daya rugi inti;
- `Im`: komponen magnetisasi untuk membentuk fluks utama.

Secara fasor:

```text
I0^2 = Ic^2 + Im^2
```

Biasanya faktor daya tanpa beban rendah karena `Im` cukup dominan.

---

## 5. Daya pada Kondisi Tanpa Beban

Jika data uji memberikan `V0`, `I0`, dan `P0`:

```text
cos(phi0) = P0 / (V0 I0)
Ic = I0 cos(phi0)
Im = I0 sin(phi0)
Rc = V0 / Ic = V0^2 / P0
Xm = V0 / Im
```

Untuk transformator kecil, `P0` dianggap mendekati rugi inti ditambah sebagian kecil rugi tembaga akibat `I0`.

---

## 6. Rugi Inti

### 6.1 Histeresis

Energi hilang karena proses magnetisasi dan demagnetisasi inti setiap siklus.

### 6.2 Arus Eddy

Tegangan yang terinduksi di dalam inti menghasilkan arus sirkulasi lokal. Laminasi inti membantu mengurangi arus eddy.

### 6.3 Hubungan dengan frekuensi dan tegangan

Pada frekuensi tetap, peningkatan tegangan meningkatkan fluks. Jika fluks mendekati daerah saturasi, arus magnetisasi dapat meningkat tajam. Karena itu analisis uji tanpa beban harus selalu menyertakan nilai tegangan dan frekuensi pengujian.

---

## 7. Fasor Tanpa Beban

Gunakan `V1` sebagai referensi. `Ic` sefasa dengan `V1`, sedangkan `Im` secara ideal tertinggal 90°. `I0` merupakan penjumlahan vektor keduanya.

Mahasiswa tidak hanya menggambar fasor, tetapi harus dapat menjelaskan mengapa `P0` terutama berasal dari komponen `Ic`.

---

## 8. Besaran yang Dicatat

Dataset minimum P2:

| Variabel | Satuan | Makna |
|---|---|---|
| V1 | V | tegangan primer |
| V2_0 | V | tegangan sekunder tanpa beban |
| I0 | A | arus primer tanpa beban |
| P0 | W | daya aktif tanpa beban |
| f | Hz | frekuensi |
| cosφ0 | - | faktor daya tanpa beban |
| Rc | ohm | resistansi rugi inti |
| Xm | ohm | reaktansi magnetisasi |

---

## 9. Perbandingan Teori, Simulasi, dan Eksperimen

Setiap laporan P2 harus mempunyai tiga lapis hasil:

1. **teori**: rasio ideal dari data lilitan/nameplate;
2. **simulasi/perhitungan**: hasil model numerik;
3. **data trainer**: hasil pengukuran yang disediakan saat praktikum.

Perbedaan ketiganya dibahas menggunakan error relatif:

```text
error(%) = |ukur - acuan| / |acuan| × 100%
```

---

## 10. Contoh Perhitungan

Misal data contoh:

```text
V0 = 220 V
I0 = 0.40 A
P0 = 35 W
```

Maka:

```text
S0 = 220 × 0.40 = 88 VA
PF0 = 35/88 = 0.3977
Ic = 0.40 × 0.3977 = 0.159 A
Im = sqrt(0.40^2 - 0.159^2) = 0.367 A
Rc = 220/0.159 ≈ 1384 ohm
Xm = 220/0.367 ≈ 599 ohm
```

Program di folder `program/` mengotomatisasi perhitungan yang sama.

---

## 11. Program Wajib

```bash
python trafo_no_load.py
python trafo_no_load_sweep.py
```

Program pertama menghitung parameter dari satu titik uji. Program kedua melakukan sweep beberapa kondisi contoh agar mahasiswa melihat perubahan `I0`, `PF0`, dan parameter estimasi.

Di Google Colab file dapat diunggah dan dijalankan dengan:

```python
!python trafo_no_load.py
```

---

## 12. Sumber Error Eksperimen

- toleransi alat ukur;
- pembacaan daya yang sangat kecil;
- fluktuasi sumber;
- suhu kumparan;
- data nameplate yang dibulatkan;
- asumsi bahwa seluruh `P0` adalah rugi inti;
- variasi frekuensi.

Mahasiswa harus membedakan **error alat**, **ketidakpastian model**, dan **kesalahan prosedural**.

---

## 13. Hubungan ke P3

P2 menghasilkan pemahaman cabang magnetisasi. P3 akan menambahkan kondisi berbeban, jatuh tegangan, regulasi, rugi tembaga, efisiensi, dan pengaruh faktor daya. Dengan demikian P2 dan P3 saling melanjutkan tetapi tidak mengulang tujuan.

---

## 14. Ringkasan

Uji tanpa beban bukan sekadar mencatat tegangan. Tujuan utamanya adalah menghubungkan fenomena magnetisasi dengan besaran terukur dan membentuk parameter model `Rc` serta `Xm` yang dapat dipakai pada analisis transformator nyata.