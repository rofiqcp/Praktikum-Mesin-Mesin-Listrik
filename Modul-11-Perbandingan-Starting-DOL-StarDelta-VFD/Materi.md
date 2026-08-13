# Modul 11 — Perbandingan Starting Motor Induksi: DOL, Star–Delta, dan VFD

**Pertemuan:** 11 dari 16  
**Durasi:** 3 × 50 menit  
**Fokus:** membandingkan dampak metode starting terhadap arus awal, torsi awal, percepatan, tegangan efektif, transisi, dan kriteria pemilihan.

> P7 telah membahas **logika kontaktor**. P9 membahas model torsi–slip. P10 membahas performa steady-state. **P11 tidak mengulang wiring P7**; P11 mengevaluasi performa metode starting dengan model dan data.

---

## 1. Capaian Pembelajaran
Mahasiswa mampu:
1. menjelaskan tujuan pembatasan arus starting;
2. membedakan DOL, star–delta, dan VFD dari sisi prinsip;
3. memperkirakan pengaruh tegangan terhadap torsi awal;
4. membandingkan profil arus, torsi, dan waktu akselerasi;
5. memahami kompromi antara arus rendah dan torsi awal;
6. menjelaskan konsep transisi star ke delta;
7. menjelaskan prinsip dasar V/f pada VFD;
8. membuat decision matrix untuk memilih metode starting berdasarkan kebutuhan beban.

---

## 2. Mengapa Starting Berbeda dari Steady-State?
Saat rotor diam:

```text
Nr = 0
s = 1
fr = f
```

Motor belum membentuk back effect mekanik seperti saat mendekati rpm operasi. Arus starting dapat jauh lebih besar dari arus nominal. Karena itu metode starting dinilai dengan parameter yang berbeda dari efisiensi steady-state.

Indikator P11:
- peak/starting current;
- starting torque;
- acceleration time;
- torque margin terhadap beban;
- transisi;
- fleksibilitas kontrol kecepatan;
- kompleksitas dan biaya relatif.

---

## 3. Direct-On-Line (DOL)
Prinsip: motor menerima tegangan line sesuai konfigurasi nominalnya sejak awal.

Karakteristik umum:
- tegangan awal penuh;
- starting torque relatif tinggi;
- starting current relatif tinggi;
- metode sederhana;
- cocok jika jaringan dan beban mengizinkan.

DOL menjadi baseline untuk perbandingan numerik P11.

---

## 4. Hubungan Torsi dan Tegangan
Dari model P9, secara pendekatan:

```text
T ∝ V²
```

Karena itu pengurangan tegangan starting mengurangi arus tetapi juga dapat mengurangi torsi secara signifikan. Kesalahan umum adalah hanya mengejar arus kecil tanpa memeriksa apakah torsi masih cukup untuk mempercepat beban.

---

## 5. Star–Delta sebagai Reduced-Voltage Starting
Jika winding yang nantinya beroperasi delta terlebih dahulu dihubungkan star pada tegangan line yang sama:

```text
V_phase_star = V_line / sqrt(3)
V_phase_delta = V_line
```

Secara ideal, terhadap kondisi delta:
- tegangan fasa saat star ≈ `1/sqrt(3)`;
- arus line starting berkurang secara signifikan;
- torsi starting kira-kira turun menjadi sekitar sepertiga, karena `T ∝ V²`.

Angka tersebut adalah pendekatan ideal; data nyata dipengaruhi motor, jaringan, beban, dan transisi.

---

## 6. Transisi Star ke Delta
Star–delta bukan hanya dua level tegangan. Ada fase transisi yang harus dianalisis:

```text
STAR → TRANSITION → DELTA
```

Jika perpindahan terlalu cepat, motor mungkin belum cukup cepat dan arus dapat melonjak. Jika terlalu lambat, akselerasi dapat terhenti atau waktu starting menjadi panjang.

P11 menganalisis fenomena ini sebagai **profil waktu**, sedangkan detail interlock tetap domain P7.

---

## 7. Variable Frequency Drive (VFD)
VFD mengubah frekuensi dan tegangan efektif yang diberikan ke motor.

Konsep dasar:

```text
Ns = 120 f / P
```

Dengan menaikkan frekuensi secara bertahap, kecepatan sinkron juga meningkat bertahap. Pada kontrol skalar sederhana, rasio `V/f` dipertahankan kira-kira konstan di daerah tertentu agar fluks tidak berubah terlalu jauh.

---

## 8. Konsep V/f
Misal motor referensi 380 V, 50 Hz:

```text
V/f = 380/50 = 7.6 V/Hz
```

Pada 25 Hz, pendekatan linear sederhana memberi sekitar:

```text
V ≈ 25 × 7.6 = 190 V
```

Ini hanya model konseptual. VFD nyata memiliki kompensasi, batas arus, ramp, parameter motor, dan strategi kontrol lain.

---

## 9. Ramp Frequency
P11 menggunakan ramp numerik:

```text
f(t) = f_start + slope × t
```

Kemudian dihitung:
- `Ns(t)`;
- perkiraan rasio tegangan;
- profil torsi relatif;
- waktu mencapai frekuensi target.

Tujuannya memahami konsep, bukan meniru seluruh algoritma VFD industri.

---

## 10. Model Akselerasi Sederhana
Dinamika mekanik:

```text
J dω/dt = Tmotor - Tload - Bω
```

Jika `Tmotor > Tload`, rotor mempercepat. Jika torsi motor terlalu rendah akibat reduced-voltage starting, waktu akselerasi meningkat atau sistem tidak mampu mencapai kondisi target pada model.

---

## 11. Starting Torque Margin
Definisikan:

```text
Tmargin = Tmotor - Tload
```

Interpretasi:
- positif: tersedia torsi percepatan;
- mendekati nol: percepatan lambat;
- negatif: model tidak dapat mempercepat pada kondisi tersebut.

Inilah alasan pemilihan starter harus mempertimbangkan karakteristik beban.

---

## 12. Jenis Beban untuk Studi Kasus
Gunakan model konseptual:

### Constant torque
```text
Tload = konstan
```

### Fan/pump sederhana
```text
Tload ∝ ω²
```

### Beban inersia tinggi
Membutuhkan waktu akselerasi lebih panjang walaupun torsi steady-state sama.

Mahasiswa membandingkan metode starting pada sedikitnya dua profil beban.

---

## 13. Matriks Perbandingan Konseptual

| Aspek | DOL | Star–Delta | VFD |
|---|---|---|---|
|Arus awal|tinggi|lebih rendah|dapat dibatasi/ramp|
|Torsi awal|tinggi|lebih rendah|dapat dikelola|
|Kompleksitas|rendah|menengah|tinggi|
|Kontrol kecepatan|tidak|tidak saat operasi normal|ya|
|Transisi|tidak ada|ada|ramp elektronik|
|Fleksibilitas|rendah|menengah|tinggi|

Tabel ini bukan ranking universal. Pilihan bergantung kebutuhan sistem.

---

## 14. Parameter yang Dibandingkan pada Program
- peak current relatif;
- starting torque relatif;
- waktu akselerasi model;
- minimum torque margin;
- energi relatif selama starting;
- kehalusan profil;
- jumlah perubahan keadaan.

---

## 15. Normalisasi
Untuk menghindari ketergantungan pada satu motor, beberapa hasil dinyatakan per-unit:

```text
I_pu = I / I_rated
T_pu = T / T_rated
V_pu = V / V_rated
f_pu = f / f_rated
```

Ini memudahkan perbandingan metode.

---

## 16. Program Wajib

```bash
python Modul-11-Perbandingan-Starting-DOL-StarDelta-VFD/program/starting_compare.py
python Modul-11-Perbandingan-Starting-DOL-StarDelta-VFD/program/vfd_ramp.py
python Modul-11-Perbandingan-Starting-DOL-StarDelta-VFD/program/decision_matrix.py
```

Output berupa tabel perbandingan dan profil numerik.

---

## 17. Eksperimen Numerik
Lakukan:
1. DOL baseline;
2. star starting dengan pendekatan `Vphase=1/sqrt(3)` kondisi delta;
3. VFD ramp cepat;
4. VFD ramp lambat;
5. constant-torque load;
6. fan-type load;
7. variasi inersia 0.5×, 1×, 2×.

Untuk setiap skenario catat waktu akselerasi dan minimum torque margin pada model.

---

## 18. Decision Matrix
Contoh kriteria:
- kebutuhan starting torque;
- batas arus;
- kebutuhan speed control;
- sensitivitas proses terhadap hentakan;
- kompleksitas;
- biaya relatif;
- kemudahan pemeliharaan.

Gunakan bobot 1–5 lalu skor 1–5. Jangan membiarkan program memilih tanpa menjelaskan bobot.

---

## 19. Kesalahan Konsep yang Harus Dihindari
- “Star–delta selalu lebih baik dari DOL.” Salah; torsi juga turun.
- “VFD hanya mengurangi tegangan.” Tidak; frekuensi merupakan variabel utama.
- “Arus paling kecil berarti starter terbaik.” Tidak selalu.
- “Star–delta cocok untuk semua nameplate.” Tidak.
- “P7 dan P11 sama.” P7 = logic; P11 = performance comparison.

---

## 20. Pertanyaan Analisis
1. Mengapa torsi star ideal jauh lebih kecil dari delta?
2. Mengapa arus awal tinggi dapat menjadi masalah sistem?
3. Mengapa beban constant-torque lebih menuntut saat reduced-voltage start?
4. Mengapa ramp VFD dapat memperhalus starting?
5. Apa fungsi menjaga V/f secara konseptual?
6. Mengapa waktu transisi star–delta penting?
7. Apa hubungan inersia dan waktu akselerasi?
8. Mengapa keputusan starter harus memakai banyak kriteria?

---

## 21. Hubungan ke P12
P11 menutup blok motor induksi P9–P11. P12 berpindah domain ke **transformator tiga fasa**, sehingga tidak ada pengulangan materi motor starting.