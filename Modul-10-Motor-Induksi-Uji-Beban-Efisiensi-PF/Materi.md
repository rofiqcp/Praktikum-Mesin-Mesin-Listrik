# Modul 10 — Motor Induksi: Uji Beban, Faktor Daya, Slip, Torsi, dan Efisiensi

**Pertemuan:** 10 dari 16  
**Durasi:** 3 × 50 menit  
**Fokus:** membaca performa motor dari dataset beban dan menghubungkan arus, faktor daya, slip, daya input, daya output, torsi, rugi, dan efisiensi.

> P9 membangun model torsi–slip dari parameter rangkaian. **P10 tidak mengulang model ekivalen**; P10 berangkat dari data performa pada beberapa kondisi beban.

---

## 1. Capaian Pembelajaran
Mahasiswa mampu:
1. menghitung daya aktif tiga fasa dari `V`, `I`, dan `PF`;
2. menghitung slip dari rpm;
3. mengubah rpm menjadi rad/s;
4. menghitung daya mekanik dari torsi dan kecepatan;
5. menghitung efisiensi;
6. membuat neraca rugi sederhana;
7. membaca perubahan `I`, `PF`, slip, torsi, dan efisiensi terhadap beban;
8. mendeteksi data yang tidak konsisten secara fisik;
9. menyusun grafik performa dan kesimpulan berbasis data.

---

## 2. Daya Tiga Fasa
Untuk sistem tiga fasa seimbang:

```text
Pin = sqrt(3) VL IL cos(phi)
```

Dengan:
- `VL`: tegangan line-to-line;
- `IL`: arus line;
- `PF = cos(phi)`.

Daya semu:

```text
S = sqrt(3) VL IL
```

Daya reaktif:

```text
Q = sqrt(S^2 - Pin^2)
```

atau `Q = sqrt(3) VL IL sin(phi)` jika sudut tersedia.

---

## 3. Kecepatan dan Slip

```text
Ns = 120 f / P
s  = (Ns-Nr)/Ns
```

Pada beban yang meningkat, motor biasanya membutuhkan torsi elektromagnetik lebih besar. Untuk menghasilkan torsi lebih besar, slip umumnya meningkat sehingga rpm turun sedikit.

---

## 4. Kecepatan Sudut dan Daya Mekanik

```text
omega = 2 pi Nr / 60
Pout  = T omega
```

Jika torsi diberikan dalam Nm dan `omega` dalam rad/s, `Pout` diperoleh dalam watt.

---

## 5. Efisiensi

```text
eta = Pout / Pin × 100%
```

Efisiensi tidak boleh dianalisis hanya dari satu titik. Grafik efisiensi terhadap persentase beban jauh lebih informatif.

Pada beban sangat ringan, rugi tetap seperti rugi inti dan mekanik merupakan bagian besar dari daya input sehingga efisiensi cenderung rendah. Ketika beban naik, efisiensi membaik sampai daerah tertentu, lalu dapat menurun jika rugi tembaga meningkat signifikan.

---

## 6. Faktor Daya terhadap Beban
Motor induksi membutuhkan arus magnetisasi walaupun beban mekanik kecil. Akibatnya pada beban ringan:
- komponen reaktif relatif besar;
- faktor daya biasanya rendah.

Ketika beban naik, komponen arus aktif meningkat sehingga faktor daya biasanya membaik.

---

## 7. Arus terhadap Beban
Arus line bukan indikator beban yang berdiri sendiri. Interpretasinya harus bersama:
- tegangan;
- faktor daya;
- rpm/slip;
- torsi;
- temperatur/kondisi sistem jika tersedia.

Kecenderungan umum dataset: arus meningkat seiring beban.

---

## 8. Neraca Rugi Sederhana

```text
Ploss_total = Pin - Pout
```

Secara konseptual rugi total dapat terdiri dari:
- rugi tembaga stator;
- rugi inti;
- rugi tembaga rotor;
- rugi mekanik;
- stray-load loss.

Jika dataset hanya mempunyai `Pin` dan `Pout`, jangan mengklaim pembagian rugi individual secara eksak. Yang sah dihitung adalah **rugi total**.

---

## 9. Torsi dari Daya Output
Jika dataset memberikan `Pout` tetapi tidak memberikan torsi:

```text
T = Pout / omega
```

Sebaliknya jika dataset memberikan torsi dan rpm, hitung `Pout = T omega`.

---

## 10. Data Minimum P10

| Kolom | Satuan | Keterangan |
|---|---|---|
| load_pct | % | persentase beban |
| VL | V | tegangan line |
| I | A | arus line |
| PF | - | faktor daya |
| rpm | rpm | kecepatan rotor |
| torque | Nm | torsi poros atau data referensi |

Kolom turunan:

| Kolom | Rumus |
|---|---|
| Ns | `120f/P` |
| slip | `(Ns-rpm)/Ns` |
| omega | `2πrpm/60` |
| Pin | `√3 VL I PF` |
| Pout | `T omega` |
| loss | `Pin-Pout` |
| eta | `Pout/Pin×100%` |

---

## 11. Grafik Wajib
Setiap laporan menghasilkan minimal:
1. arus vs beban;
2. rpm vs beban;
3. slip vs beban;
4. PF vs beban;
5. torsi vs beban;
6. `Pin` dan `Pout` vs beban;
7. efisiensi vs beban;
8. rugi total vs beban.

Grafik harus mempunyai judul, label sumbu, satuan, dan legenda jika ada lebih dari satu seri.

---

## 12. Membaca Hubungan Antarvariabel
Contoh pertanyaan yang harus dapat dijawab:
- Saat beban naik, apakah arus selalu naik?
- Apakah rpm turun secara linear?
- Apakah slip berubah lebih jelas daripada rpm?
- Pada beban berapa PF mulai membaik signifikan?
- Di mana efisiensi maksimum pada dataset?
- Apakah `Pin-Pout` selalu positif?

---

## 13. Validasi Data
Tandai baris jika:
- `PF < 0` atau `PF > 1`;
- `eta > 100%` tanpa penjelasan ketidakpastian;
- `Pin < Pout`;
- rpm lebih tinggi dari `Ns` untuk dataset mode motor biasa;
- slip sangat berbeda dari tren baris di sekitarnya;
- torsi negatif tanpa konteks;
- satuan tercampur.

Validasi bukan berarti langsung menghapus data. Tandai, telusuri sumber, lalu dokumentasikan keputusan.

---

## 14. Ketidakpastian dan Error
Sumber perbedaan dapat berasal dari:
- resolusi alat ukur;
- pembulatan rpm;
- toleransi sensor torsi;
- variasi tegangan;
- ketidakseimbangan fasa;
- temperatur;
- asumsi sistem seimbang pada rumus daya tiga fasa.

---

## 15. Program Wajib

```bash
python Modul-10-Motor-Induksi-Uji-Beban-Efisiensi-PF/program/induction_load_analysis.py
python Modul-10-Motor-Induksi-Uji-Beban-Efisiensi-PF/program/load_sweep_summary.py
```

Program pertama membaca CSV dan menghitung besaran turunan. Program kedua merangkum titik penting dan perubahan antar-beban.

---

## 16. Eksperimen Data
Mahasiswa wajib melakukan:
1. baseline dataset;
2. analisis ulang jika PF diasumsikan konstan untuk melihat dampaknya pada `Pin`/efisiensi;
3. analisis sensitivitas jika rpm berubah ±1%;
4. identifikasi baris efisiensi maksimum;
5. identifikasi beban dengan PF terbaik;
6. analisis korelasi sederhana antara beban–arus, beban–slip, dan beban–efisiensi.

---

## 17. Contoh Logika Analisis
Jika pada beban 20% PF rendah tetapi pada 80% PF lebih tinggi, jangan hanya menulis “PF naik”. Jelaskan bahwa arus magnetisasi relatif tetap penting, sedangkan komponen arus aktif meningkat bersama kebutuhan daya mekanik.

Jika efisiensi menurun di beban tertinggi, periksa apakah kenaikan rugi total lebih cepat daripada kenaikan `Pout`.

---

## 18. Pertanyaan Analisis
1. Mengapa PF motor induksi rendah pada beban ringan?
2. Mengapa slip meningkat ketika beban bertambah?
3. Mengapa efisiensi rendah pada beban sangat kecil?
4. Apa beda daya semu, aktif, dan reaktif?
5. Mengapa `Pin-Pout` tidak boleh negatif pada dataset konsisten?
6. Apakah arus yang tinggi selalu berarti efisiensi rendah? Jelaskan.
7. Mengapa satu titik efisiensi tidak cukup untuk menilai performa motor?
8. Apa keterbatasan rumus `Pin=√3VLILPF` jika sistem tidak seimbang?

---

## 19. Hubungan ke P11
P10 menghasilkan baseline performa terhadap beban. P11 menggunakan baseline tersebut untuk membandingkan bagaimana **cara starting** memengaruhi arus awal, torsi awal, waktu akselerasi, dan kualitas transien. Dengan demikian P10 fokus steady-state, sedangkan P11 fokus starting/transient comparison.