# Modul 09 — Motor Induksi: Rangkaian Ekivalen, Slip, dan Kurva Torsi–Kecepatan

**Pertemuan:** 9 dari 16  
**Durasi:** 3 × 50 menit  
**Fokus:** model listrik per fasa, aliran daya elektromagnetik, slip, frekuensi rotor, torsi induksi, breakdown torque, dan pengaruh parameter terhadap kurva torsi–kecepatan.

> P6 membahas medan putar, terminal, star/delta, arah dan slip dasar. P7 membahas logika kontaktor. **P9 tidak mengulang wiring starter**; P9 mengubah motor induksi menjadi model matematis yang dapat dihitung dan disimulasikan.

---

## 1. Capaian Pembelajaran
Mahasiswa mampu:
1. menjelaskan makna setiap parameter `R1`, `X1`, `Rc`, `Xm`, `R2'`, dan `X2'`;
2. menghitung `Ns`, slip, kecepatan rotor, dan frekuensi rotor;
3. menjelaskan mengapa `R2'/s` berubah terhadap kondisi mekanik;
4. membangun model Thevenin stator;
5. menghitung torsi elektromagnetik untuk berbagai slip;
6. mengidentifikasi starting torque, breakdown torque, slip breakdown, dan daerah operasi normal;
7. melakukan sweep parameter dan menyimpulkan sensitivitas model;
8. membedakan parameter model, data nameplate, dan data hasil pengukuran.

---

## 2. Review Kecepatan Sinkron dan Slip

```text
Ns = 120 f / P
s  = (Ns - Nr) / Ns
Nr = (1 - s) Ns
fr = s f
```

Dengan:
- `Ns`: kecepatan sinkron [rpm],
- `Nr`: kecepatan rotor [rpm],
- `f`: frekuensi stator [Hz],
- `P`: jumlah kutub,
- `s`: slip,
- `fr`: frekuensi arus rotor [Hz].

Interpretasi:
- rotor diam: `s = 1`;
- operasi motor normal: `0 < s << 1`;
- mendekati sinkron: `s → 0`;
- secara matematis `s < 0` merepresentasikan daerah generator, tetapi P9 hanya menggunakannya untuk membaca karakteristik, bukan sebagai prosedur praktik.

### Contoh
Motor 4 kutub, 50 Hz, berputar 1440 rpm:

```text
Ns = 120(50)/4 = 1500 rpm
s  = (1500-1440)/1500 = 0.04 = 4%
fr = 0.04(50) = 2 Hz
```

---

## 3. Mengapa Motor Induksi Bisa Dimodelkan seperti Transformator?
Stator menghasilkan fluks celah udara yang menginduksikan tegangan pada rotor. Karena energi berpindah melalui induksi elektromagnetik, struktur model per fasa mirip transformator, tetapi rotor memiliki fenomena slip.

Parameter utama:

| Parameter | Makna fisik |
|---|---|
| `R1` | resistansi stator |
| `X1` | reaktansi bocor stator |
| `Rc` | representasi rugi inti |
| `Xm` | reaktansi magnetisasi |
| `R2'` | resistansi rotor direferensikan ke stator |
| `X2'` | reaktansi bocor rotor direferensikan ke stator |
| `R2'/s` | bagian model rotor yang bergantung slip |

---

## 4. Makna `R2'/s`

Secara algebra:

```text
R2'/s = R2' + R2'(1-s)/s
```

Interpretasi model:
- `R2'` berhubungan dengan rugi tembaga rotor;
- komponen `R2'(1-s)/s` merepresentasikan konversi daya elektromagnetik menjadi daya mekanik pada model ekivalen.

Ini adalah salah satu konsep terpenting P9: **beban mekanik muncul di model listrik melalui slip**.

---

## 5. Aliran Daya Motor Induksi

Urutan konseptual:

```text
Pin
 ↓
Rugi stator + rugi inti
 ↓
P_ag  (air-gap power)
 ↓
Rugi tembaga rotor = s P_ag
 ↓
P_conv = (1-s) P_ag
 ↓
Rugi mekanik
 ↓
P_out
```

Hubungan penting:

```text
P_rotor_cu = s P_ag
P_conv     = (1-s) P_ag
```

Karena itu slip bukan hanya angka kecepatan; slip juga berkaitan langsung dengan pembagian daya di rotor.

---

## 6. Model Thevenin
Untuk menghitung torsi secara efisien, bagian stator + cabang magnetisasi dapat direduksi menjadi ekuivalen Thevenin:

```text
Vth, Rth, Xth
```

Kemudian rotor direpresentasikan oleh:

```text
R2'/s + jX2'
```

Bentuk torsi yang digunakan di program:

```text
T(s) = 3 Vth² (R2'/s)
       -------------------------------
       ws [(Rth+R2'/s)² + (Xth+X2')²]
```

`ws` adalah kecepatan sudut sinkron mekanik dalam rad/s.

---

## 7. Membaca Kurva Torsi–Kecepatan
Kurva mempunyai beberapa daerah penting:

### 7.1 Starting
`Nr=0`, `s=1`. Nilai torsi pada titik ini disebut starting torque.

### 7.2 Accelerating region
Ketika motor mempercepat, slip turun dan torsi berubah mengikuti parameter rangkaian.

### 7.3 Breakdown / Pull-out torque
Nilai torsi maksimum yang dapat dibentuk model sebelum karakteristik memasuki sisi tidak stabil terhadap beban statik.

### 7.4 Operating region
Motor industri biasanya bekerja dekat `Ns`, sehingga slip relatif kecil.

### 7.5 No-load
Torsi beban kecil, tetapi motor tetap membutuhkan torsi internal untuk rugi mekanik dan rugi lainnya.

---

## 8. Slip Breakdown
Untuk model Thevenin sederhana, kondisi torsi maksimum mempunyai hubungan dengan `R2'` dan impedansi seri ekuivalen. Secara kualitatif:
- menaikkan `R2'` menggeser slip torsi maksimum;
- besar breakdown torque ideal tertentu dapat relatif tidak banyak berubah jika tegangan tetap;
- tegangan mempunyai pengaruh sangat kuat terhadap torsi.

Mahasiswa wajib memverifikasi kecenderungan ini melalui sweep Python, bukan hanya menghafalnya.

---

## 9. Pengaruh Tegangan
Dari persamaan torsi terlihat kira-kira:

```text
T ∝ V²
```

Jika tegangan turun, kemampuan torsi dapat turun lebih tajam daripada penurunan tegangannya sendiri. Ini menjelaskan mengapa kualitas tegangan penting pada beban dengan tuntutan starting torque tinggi.

---

## 10. Pengaruh Resistansi Rotor
Sweep `R2'` digunakan untuk melihat:
- perubahan starting torque;
- pergeseran slip breakdown;
- perubahan bentuk daerah percepatan.

P9 tidak membahas metode starter eksternal; perbandingan metode starting baru menjadi fokus P11.

---

## 11. Pengaruh Frekuensi
Frekuensi memengaruhi:
- `Ns`;
- reaktansi;
- kecepatan sudut sinkron;
- hubungan tegangan/fluks apabila sistem digerakkan oleh sumber frekuensi variabel.

Analisis V/f secara komprehensif dibahas di P11 pada konteks VFD.

---

## 12. Parameter dari Mana?
Parameter ekivalen dapat berasal dari:
1. data contoh akademik;
2. datasheet/model pabrikan;
3. identifikasi parameter melalui prosedur laboratorium yang telah ditetapkan;
4. estimasi numerik.

Jangan mencampur parameter dari motor berbeda dan menganggap hasilnya mewakili satu motor nyata.

---

## 13. Validasi Model
Model yang bagus bukan model yang menghasilkan grafik indah, tetapi model yang:
- mempunyai satuan konsisten;
- menghasilkan `Ns` benar;
- menghasilkan slip nominal masuk akal;
- menunjukkan torsi nol mendekati kecepatan sinkron pada model sederhana;
- mempunyai daerah starting dan breakdown yang dapat dijelaskan;
- dapat dibandingkan dengan rpm/arus/torsi dari dataset eksperimen.

---

## 14. Program Wajib

```bash
python program/induction_torque_speed.py
python program/parameter_sweep.py
```

Output minimum:
- tabel titik penting;
- starting torque;
- breakdown torque;
- slip dan rpm breakdown;
- torsi pada slip nominal;
- grafik `T-rpm` dan `T-slip`;
- hasil sweep tegangan dan `R2'`.

Script dapat dijalankan di VS Code, terminal, atau Google Colab.

---

## 15. Eksperimen Numerik Wajib
Mahasiswa melakukan sedikitnya empat skenario:
1. baseline;
2. tegangan model diturunkan 10%;
3. `R2'` dinaikkan 50%;
4. jumlah kutub atau frekuensi diubah untuk melihat perubahan `Ns`.

Untuk setiap skenario tuliskan **prediksi sebelum menjalankan program**, kemudian bandingkan dengan hasil aktual.

---

## 16. Pertanyaan Analisis
1. Mengapa torsi induksi membutuhkan slip?
2. Mengapa `fr` jauh lebih kecil dari frekuensi stator saat motor dekat kecepatan nominal?
3. Apa makna fisik `R2'/s`?
4. Mengapa penurunan tegangan kecil dapat berdampak besar pada torsi?
5. Apa perbedaan breakdown torque dengan rated torque?
6. Mengapa parameter model harus direferensikan ke sisi yang sama?
7. Bagaimana `R2'` mengubah posisi puncak kurva?
8. Mengapa kurva model tidak akan identik dengan motor nyata?

---

## 17. Sumber Error Model
- parameter tidak identik dengan motor nyata;
- saturasi diabaikan;
- rugi tambahan tidak dimodelkan;
- temperatur mengubah resistansi;
- tegangan tiga fasa diasumsikan seimbang;
- model steady-state tidak menangkap semua transien starting.

---

## 18. Hubungan ke P10 dan P11
- **P9:** dari parameter → kurva elektromagnetik.
- **P10:** dari data beban → performa aktual `I`, `PF`, slip, daya, torsi, efisiensi.
- **P11:** menggunakan pemahaman P9–P10 untuk membandingkan strategi starting DOL, star–delta, dan VFD.

Dengan pembagian ini, ketiga pertemuan saling menyambung tanpa mengulang tujuan yang sama.