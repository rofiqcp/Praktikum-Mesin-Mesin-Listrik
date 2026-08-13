# Modul 06 — Motor Induksi 3 Fasa: Medan Putar, Kecepatan Sinkron, Slip, Terminal, Star–Delta, dan Arah Putaran

**Mata Kuliah:** Praktikum Mesin-Mesin Listrik  
**Pertemuan:** 6 dari 16  
**Durasi:** 3 × 50 menit  
**Fokus:** memahami fisika dan hubungan listrik dasar motor induksi tiga fasa sebelum masuk ke logika kontaktor pada P7 dan model rangkaian ekivalen pada P9.

---

## 1. Batas Anti-Overlay

P6 membahas **motor induksinya**:

- bagaimana medan putar terbentuk;
- hubungan frekuensi, jumlah kutub, dan kecepatan sinkron;
- mengapa rotor selalu mempunyai slip saat menghasilkan torsi;
- arti enam terminal motor;
- hubungan line–phase pada star dan delta;
- konsekuensi teoritis star vs delta terhadap tegangan fasa, arus, dan torsi;
- prinsip perubahan arah medan putar.

P7 membahas **logika kontaktor dan interlock**. P9 membahas **rangkaian ekivalen dan kurva torsi–slip**. Dengan demikian P6 tidak mengulang keduanya.

---

## 2. Capaian Pembelajaran

Mahasiswa mampu:

1. menjelaskan pembentukan rotating magnetic field tiga fasa;
2. menghitung kecepatan sinkron;
3. menghitung slip dan frekuensi rotor;
4. membedakan kecepatan sinkron dan kecepatan rotor;
5. membaca data nameplate motor induksi;
6. menjelaskan makna terminal `U1 V1 W1 U2 V2 W2`;
7. menghitung hubungan line–phase pada star dan delta;
8. menjelaskan secara teoritis pengaruh star dan delta terhadap tegangan fasa dan torsi awal;
9. menjelaskan prinsip pembalikan arah putaran medan;
10. mengolah parameter motor menggunakan Python.

---

## 3. Medan Putar Tiga Fasa

Sistem tiga fasa seimbang mempunyai tiga gelombang arus sinusoidal yang berbeda fase 120 derajat listrik:

```text
iA = Im sin(wt)
iB = Im sin(wt - 120 deg)
iC = Im sin(wt - 240 deg)
```

Ketiga arus menghasilkan fluks pada belitan stator. Penjumlahan vektor fluks membentuk medan magnet resultan yang berputar dengan besar mendekati konstan.

Konsep penting:

```text
urutan fasa -> arah medan putar
frekuensi + jumlah kutub -> kecepatan medan putar
```

Rotor kemudian berinteraksi dengan medan tersebut melalui induksi elektromagnetik.

---

## 4. Kecepatan Sinkron

Kecepatan medan putar stator:

```text
Ns = 120 f / P
```

- `Ns`: rpm;
- `f`: Hz;
- `P`: jumlah kutub.

Contoh pada 50 Hz:

| Kutub | Ns |
|---:|---:|
| 2 | 3000 rpm |
| 4 | 1500 rpm |
| 6 | 1000 rpm |
| 8 | 750 rpm |

Kecepatan ini milik **medan magnet stator**, bukan selalu kecepatan mekanik rotor.

---

## 5. Mengapa Rotor Tidak Sama dengan Ns?

Motor induksi membutuhkan gerak relatif antara medan putar dan rotor agar terdapat induksi pada rotor. Jika rotor tepat sama dengan `Ns`:

```text
relative speed = 0
induced rotor emf -> 0
rotor current -> 0
torque electromagnetic -> 0
```

Karena itu pada mode motor normal:

```text
Nr < Ns
```

Perbedaannya dinyatakan sebagai slip.

---

## 6. Slip

```text
s = (Ns - Nr) / Ns
s(%) = (Ns - Nr)/Ns * 100%
```

Contoh:

```text
f = 50 Hz
P = 4
Ns = 1500 rpm
Nr = 1440 rpm
```

Maka:

```text
s = (1500-1440)/1500 = 0.04 = 4%
```

Slip 4% berarti rotor 4% lebih lambat dari kecepatan sinkron relatif terhadap basis `Ns`.

---

## 7. Frekuensi Rotor

Frekuensi arus rotor:

```text
fr = s f
```

Untuk contoh sebelumnya:

```text
fr = 0.04 * 50 = 2 Hz
```

Saat awal diam, `s ≈ 1` sehingga frekuensi rotor mendekati frekuensi stator. Saat kecepatan mendekati `Ns`, slip dan frekuensi rotor mengecil.

---

## 8. Konstruksi Motor Induksi

### Stator

Terdiri dari inti laminasi dan belitan tiga fasa yang menghasilkan rotating magnetic field.

### Rotor squirrel-cage

Batang konduktor rotor dihubung-singkat oleh end ring. Tidak memerlukan koneksi listrik eksternal langsung ke rotor.

### Air gap

Celah udara memungkinkan rotor berputar tetapi menambah reluctance magnetik. Desain air gap memengaruhi performa elektromagnetik.

### Bearing dan frame

Menopang rotor dan menyediakan struktur mekanik serta pelepasan panas.

---

## 9. Nameplate Motor Induksi

Data yang biasa ada:

- tegangan;
- arus;
- frekuensi;
- daya;
- rpm nominal;
- power factor;
- efisiensi;
- hubungan terminal;
- kelas isolasi;
- duty;
- IP rating.

Dari `f`, rpm, dan kandidat jumlah kutub, mahasiswa dapat memperkirakan slip nominal.

---

## 10. Enam Terminal

Motor dengan akses enam terminal biasanya menampilkan:

```text
U1 V1 W1
U2 V2 W2
```

Masing-masing pasangan merupakan ujung awal dan akhir tiga belitan stator. Dokumentasi dan nameplate motor nyata menjadi acuan utama untuk interpretasi terminal.

P6 berfokus memahami topologi dan persamaan; konfigurasi fisik pada trainer mengikuti diagram resmi trainer dan supervisi laboratorium.

---

## 11. Hubungan Star

Untuk sistem seimbang:

```text
VL = sqrt(3) Vph
IL = Iph
Vph = VL/sqrt(3)
```

Artinya tiap belitan pada star menerima tegangan fasa sebesar tegangan line dibagi `sqrt(3)`.

---

## 12. Hubungan Delta

Untuk sistem seimbang:

```text
VL = Vph
IL = sqrt(3) Iph
```

Pada delta, tiap belitan menerima tegangan line.

---

## 13. Perbandingan Teoritis Star dan Delta

Untuk motor yang secara desain dapat dibandingkan pada tegangan line yang sama:

```text
Vph_star = VL/sqrt(3)
Vph_delta = VL
```

Jika impedansi fasa disederhanakan konstan:

```text
Iph proportional to Vph
```

Dan pada pendekatan dasar, torsi elektromagnetik awal kira-kira sebanding kuadrat tegangan:

```text
T proportional to V^2
```

Sehingga secara pendekatan:

```text
T_star / T_delta ≈ 1/3
```

Ini menjelaskan alasan star-delta dapat menurunkan tuntutan starting, tetapi juga menurunkan torsi awal. Detail performa starting dibahas kembali pada P11, bukan P6.

---

## 14. Arah Putaran

Arah rotating magnetic field ditentukan urutan fasa. Menukar urutan dua fasa mengubah urutan fasa dan membalik arah medan putar.

P6 hanya membahas prinsip fisik tersebut. Implementasi logika forward–reverse, interlock, dan kontaktor dibahas pada P7 menggunakan simulasi kontrol.

---

## 15. Daya Tiga Fasa

Daya aktif input sistem seimbang:

```text
Pin = sqrt(3) VL IL cos(phi)
```

Daya semu:

```text
S = sqrt(3) VL IL
```

Daya reaktif:

```text
Q = sqrt(S^2 - P^2)
```

Analisis efisiensi motor induksi secara berbeban menjadi fokus P10.

---

## 16. Contoh Perhitungan Lengkap

Diketahui motor 4 kutub, 50 Hz, rotor 1440 rpm, `VL=380 V`, `IL=2.5 A`, `PF=0.82`.

Kecepatan sinkron:

```text
Ns = 120*50/4 = 1500 rpm
```

Slip:

```text
s = (1500-1440)/1500 = 0.04 = 4%
```

Frekuensi rotor:

```text
fr = 0.04*50 = 2 Hz
```

Jika sistem star:

```text
Vph = 380/sqrt(3) ≈ 219.4 V
Iph = 2.5 A
```

Jika sistem delta dengan nilai line hipotetik yang sama:

```text
Vph = 380 V
Iph = IL/sqrt(3)
```

Daya aktif input contoh:

```text
Pin = sqrt(3)*380*2.5*0.82 ≈ 1349 W
```

---

## 17. Program Python

Jalankan:

```bash
cd Modul-06-Motor-Induksi-3Fasa-Dasar-Star-Delta/program
python star_delta_calc.py
```

Program dipakai untuk:

- menghitung `Ns`;
- slip;
- frekuensi rotor;
- hubungan line–phase star dan delta;
- perbandingan numerik beberapa jumlah kutub.

Program adalah alat bantu perhitungan, bukan pengganti pemahaman diagram dan nameplate.

---

## 18. Eksperimen Numerik

### A. Sweep jumlah kutub

Bandingkan `P = 2,4,6,8` pada 50 Hz.

### B. Sweep frekuensi

Bandingkan `f = 25, 40, 50, 60 Hz` untuk jumlah kutub tetap sebagai latihan matematis.

### C. Sweep rpm rotor

Untuk `Ns` tetap, hitung slip pada beberapa `Nr` dan plot `slip vs rpm`.

### D. Line–phase

Bandingkan `Vph` star dan delta untuk beberapa tegangan line hipotetik.

---

## 19. Grafik Wajib

Minimal:

1. `Ns vs jumlah kutub`;
2. `slip vs Nr`;
3. tabel atau grafik perbandingan `Vph star vs delta`.

Setiap grafik harus disertai interpretasi.

---

## 20. Kesalahan Konsep yang Sering Terjadi

- menganggap `Ns = Nr` pada motor induksi berbeban;
- memakai jumlah pole pair langsung sebagai `P` pada rumus tanpa konversi;
- menyatakan slip dalam persen lalu memasukkannya kembali sebagai angka 4, bukan 0.04;
- tertukar antara line voltage dan phase voltage;
- menganggap star selalu “lebih baik” dari delta;
- menganggap star-delta mengubah frekuensi sumber;
- menganggap pembalikan urutan fasa sama dengan mengubah frekuensi.

---

## 21. Hubungan ke P7, P9, dan P10

```text
P6: fisika + terminal + line/phase + slip
        |
        +-> P7: logika kontaktor, latch, F/R, interlock, star-delta
        |
        +-> P9: rangkaian ekivalen + kurva torsi-slip
        |
        +-> P10: uji beban + PF + efisiensi
```

---

## 22. Ringkasan

Motor induksi tiga fasa bekerja karena medan putar stator menginduksikan arus pada rotor. Kecepatan medan ditentukan frekuensi dan jumlah kutub, sedangkan rotor membutuhkan slip untuk menghasilkan torsi. Pemahaman star/delta pada P6 adalah pemahaman hubungan fasa dan tegangan; logika switching-nya baru dibahas pada P7.