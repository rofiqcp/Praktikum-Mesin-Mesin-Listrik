# Modul 05 — Motor DC: Karakteristik Beban, Speed–Torque, PWM, Daya, dan Efisiensi

**Mata Kuliah:** Praktikum Mesin-Mesin Listrik  
**Pertemuan:** 5 dari 16  
**Durasi:** 3 × 50 menit  
**Prasyarat:** Modul 04 — back-EMF, arus jangkar, torsi elektromagnetik, arah putaran  
**Fokus:** mengubah pemahaman dasar motor DC menjadi analisis **steady-state berbeban** berbasis data.

---

## 1. Posisi Modul dan Batas Anti-Overlay

P4 membahas **mengapa motor DC dapat berputar**, bagaimana back-EMF muncul, respons awal, dan prinsip arah putaran. P5 tidak mengulang fokus tersebut. P5 menjawab pertanyaan berikut:

- apa yang terjadi pada arus ketika beban mekanik naik?
- mengapa kecepatan turun ketika torsi beban naik?
- bagaimana bentuk kurva speed–torque?
- bagaimana daya masuk, daya mekanik, rugi, dan efisiensi berubah terhadap beban?
- bagaimana PWM memengaruhi tegangan rata-rata dan operating point?
- operating point mana yang masuk akal secara teknis?

P5 **tidak** membahas kendali PID motor; topik tersebut berada di mata kuliah sistem kontrol.

---

## 2. Capaian Pembelajaran

Setelah menyelesaikan P5, mahasiswa mampu:

1. menggunakan persamaan steady-state motor DC untuk menghitung arus, back-EMF, kecepatan, torsi, dan daya;
2. menjelaskan karakteristik `speed–torque`, `current–torque`, `power–torque`, dan `efficiency–load`;
3. membedakan no-load, beban ringan, beban nominal, dan overload secara konseptual;
4. menghitung daya listrik masuk dan daya mekanik poros;
5. menghitung efisiensi dan mengidentifikasi sumber rugi;
6. menjelaskan pengaruh duty cycle PWM terhadap tegangan rata-rata;
7. mengolah CSV menggunakan Python dan membangun grafik yang dapat dipakai dalam laporan;
8. membandingkan hasil model sederhana dengan dataset praktikum.

---

## 3. Persamaan Dasar Steady-State

Untuk motor DC dengan fluks dianggap konstan:

```text
V = E + Ia Ra
E = Ke ω
T = Kt Ia
ω = 2πn/60
```

Sehingga:

```text
Ia = (V - E)/Ra
ω = (V - Ia Ra)/Ke
```

Karena `T = Kt Ia`, maka secara ideal kecepatan berkurang hampir linier ketika torsi naik.

Dengan mengganti `Ia = T/Kt`:

```text
ω = V/Ke - (Ra/(Ke Kt)) T
```

Bentuk ini adalah persamaan garis:

```text
ω = ω0 - mT
```

- `ω0 = V/Ke` adalah kecepatan ideal pada arus mendekati nol;
- `m = Ra/(Ke Kt)` adalah kemiringan karakteristik speed–torque.

---

## 4. No-Load Speed dan Stall Current

### 4.1 No-load ideal

Pada pendekatan paling sederhana:

```text
T ≈ 0
Ia ≈ 0
ω0 ≈ V/Ke
```

Motor nyata tetap membutuhkan arus untuk mengatasi friction, windage, rugi besi, brush loss, dan rugi mekanik lain.

### 4.2 Stall

Jika rotor tidak berputar:

```text
ω = 0
E = 0
Istall = V/Ra
Tstall = Kt Istall
```

Nilai stall adalah batas matematis model, **bukan titik operasi kontinu**. Pada mesin nyata, arus tinggi meningkatkan rugi tembaga `Ia²Ra` dengan cepat.

---

## 5. Karakteristik Speed–Torque

Untuk fluks konstan, bentuk ideal mendekati garis lurus:

```text
speed
  ^
  |\
  | \
  |  \
  |   \
  |    \
  +----------> torque
```

Ketika beban mekanik naik:

1. kecepatan cenderung turun;
2. back-EMF turun;
3. selisih `V-E` meningkat;
4. arus jangkar meningkat;
5. torsi elektromagnetik meningkat hingga seimbang dengan torsi beban + rugi.

Rantai sebab-akibat ini wajib dijelaskan mahasiswa, bukan hanya dihafalkan.

---

## 6. Karakteristik Current–Torque

Karena:

```text
T = Kt Ia
```

maka untuk fluks tetap:

```text
Ia = T/Kt
```

Hubungan ideal arus–torsi linier. Pada motor nyata terdapat arus no-load sehingga kurva pengukuran tidak selalu melalui titik nol.

---

## 7. Daya Motor DC

### 7.1 Daya listrik masuk

```text
Pin = V Ia
```

### 7.2 Daya elektromagnetik yang dikonversikan

```text
Pconv = E Ia
```

### 7.3 Rugi tembaga jangkar

```text
Pcu = Ia² Ra
```

Dari persamaan `V=E+IaRa`:

```text
V Ia = E Ia + Ia² Ra
Pin = Pconv + Pcu
```

### 7.4 Daya mekanik poros

Jika torsi poros diketahui:

```text
Pout = Tshaft ω
```

### 7.5 Efisiensi

```text
η = Pout / Pin × 100%
```

Pada beban sangat ringan, efisiensi dapat rendah karena rugi tetap menjadi bagian besar dari daya masuk. Pada beban sangat berat, rugi tembaga meningkat tajam.

---

## 8. Model Rugi

Model sederhana dapat membagi rugi menjadi:

```text
Ploss = Pcu + Pbrush + Pcore + Pmech + Pstray
```

Untuk praktikum dasar, komponen dapat dikelompokkan menjadi:

```text
Ploss ≈ Ia²Ra + Pconstant
```

`Pconstant` mewakili gabungan friction, windage, rugi inti, dan rugi lain yang dianggap relatif tetap pada rentang pengujian terbatas.

---

## 9. PWM pada Motor DC

PWM mengatur waktu ON/OFF sumber secara cepat. Duty cycle:

```text
D = ton / T
```

Pada model rata-rata ideal:

```text
Vavg ≈ D Vdc
```

Contoh sumber 24 V:

| Duty | Vavg ideal |
|---:|---:|
| 25% | 6 V |
| 50% | 12 V |
| 75% | 18 V |
| 100% | 24 V |

Motor tidak selalu mengikuti `Vavg` secara statik sempurna karena terdapat induktansi jangkar, switching device, rugi, ripple arus, dan dinamika mekanik.

---

## 10. Pengaruh Duty Cycle terhadap Operating Point

Pada fluks dan beban yang sama, menaikkan duty cycle umumnya menaikkan tegangan rata-rata sehingga kecepatan steady-state meningkat. Akan tetapi operating point final selalu merupakan hasil keseimbangan:

```text
torsi motor = torsi beban + torsi rugi
```

Karena itu hubungan `duty → rpm` tidak boleh dianggap universal tanpa memperhatikan beban.

---

## 11. Parameter yang Dicatat pada P5

Dataset minimum:

| Variabel | Satuan | Makna |
|---|---|---|
| duty | % | duty cycle/perintah tegangan |
| V | V | tegangan rata-rata/terminal sesuai data trainer |
| Ia | A | arus jangkar |
| n | rpm | kecepatan poros |
| T | N·m | torsi poros jika tersedia |
| Pin | W | daya listrik masuk |
| Pout | W | daya mekanik poros |
| eta | % | efisiensi |
| load_pct | % | tingkat beban relatif |

Jika trainer tidak menyediakan sensor torsi, analisis utama menggunakan `V`, `I`, `rpm`, dan data beban yang disediakan dosen/laboran.

---

## 12. Grafik Wajib

Minimal buat:

1. `rpm vs torque` atau `rpm vs load_pct`;
2. `Ia vs torque/load`;
3. `Pin dan Pout vs load`;
4. `efficiency vs load`;
5. untuk eksperimen PWM: `rpm vs duty`.

Setiap grafik wajib mempunyai:

- judul yang informatif;
- nama sumbu dan satuan;
- legenda bila lebih dari satu kurva;
- data point yang terlihat;
- interpretasi 2–4 kalimat.

---

## 13. Contoh Perhitungan

Misal:

```text
V = 24 V
Ia = 2.0 A
Ra = 1.2 ohm
Ke = 0.08 V/(rad/s)
Kt = 0.08 N.m/A
```

Back-EMF:

```text
E = 24 - 2(1.2) = 21.6 V
```

Kecepatan:

```text
ω = E/Ke = 270 rad/s
n = 270 × 60/(2π) ≈ 2578 rpm
```

Torsi elektromagnetik:

```text
T = Kt Ia = 0.16 N.m
```

Daya masuk:

```text
Pin = 24 × 2 = 48 W
```

Daya konversi elektromagnetik:

```text
Pconv = 21.6 × 2 = 43.2 W
```

Rugi tembaga:

```text
Pcu = 2² × 1.2 = 4.8 W
```

Terlihat bahwa `Pin = Pconv + Pcu` pada model ini.

---

## 14. Analisis Data dengan Python

Folder `program/` menyediakan dataset contoh dan script analisis.

```bash
cd Modul-05-Motor-DC-Karakteristik-Beban/program
python dc_characteristic.py
```

Program membaca `data_dc.csv`, menghitung daya/efisiensi turunan, menampilkan tabel, dan membuat grafik jika `matplotlib` tersedia.

Untuk eksperimen model PWM dapat menggunakan script Python tambahan pada folder yang sama dan contoh GNU Octave/MATLAB `dc_pwm.m`.

---

## 15. Eksperimen Numerik yang Harus Dicoba

Mahasiswa melakukan minimal tiga modifikasi model:

### A. Ubah resistansi jangkar

Bandingkan `Ra` kecil dan besar. Jelaskan perubahan slope speed–torque dan rugi tembaga.

### B. Ubah tegangan/duty

Bandingkan karakteristik untuk beberapa tegangan efektif.

### C. Ubah rugi tetap

Amati perubahan kurva efisiensi pada beban ringan.

Semua modifikasi dicatat dalam tabel sebelum menarik kesimpulan.

---

## 16. Validasi Data

Sebelum menghitung efisiensi, cek:

```text
Pin >= 0
Pout >= 0
eta <= 100% untuk dataset normal
rpm masuk akal terhadap kondisi eksperimen
arus naik ketika beban meningkat pada kondisi tegangan sebanding
```

Jika data menghasilkan efisiensi di atas 100%, jangan langsung menghapusnya. Tandai sebagai data yang perlu ditinjau: bisa terjadi karena salah satuan, salah pembacaan, sinkronisasi pengukuran yang buruk, atau salah definisi torsi.

---

## 17. Pertanyaan Analisis Utama

1. Mengapa kenaikan torsi beban menyebabkan arus naik?
2. Mengapa speed–torque mendekati garis lurus pada model fluks konstan?
3. Mengapa efisiensi rendah pada beban sangat ringan?
4. Mengapa rugi tembaga meningkat cepat pada arus besar?
5. Apakah duty 50% selalu menghasilkan rpm 50% dari rpm duty 100%? Jelaskan.
6. Apa perbedaan `Pconv` dan `Pout`?
7. Mengapa stall current bukan operating point kontinu yang baik?
8. Parameter mana yang paling memengaruhi slope speed–torque pada model sederhana?

---

## 18. Kesalahan Konsep yang Sering Terjadi

- menganggap `T = V` secara langsung;
- menganggap rpm hanya ditentukan tegangan tanpa pengaruh beban;
- menyamakan back-EMF dengan tegangan sumber;
- menggunakan rpm langsung pada `P=Tω` tanpa konversi ke rad/s;
- menghitung efisiensi menggunakan `Pconv` sebagai `Pout` tanpa menyatakan asumsi;
- menganggap PWM sama dengan resistor seri;
- menganggap data yang tidak sesuai teori pasti salah tanpa mengecek model dan instrumen.

---

## 19. Hubungan ke P6

Setelah P5, mahasiswa sudah memahami hubungan **beban → arus → torsi → kecepatan → daya** pada motor DC. P6 berpindah ke motor induksi tiga fasa dan memperkenalkan medan putar, kecepatan sinkron, slip, terminal star/delta, serta hubungan line–phase. Jadi objek dan fenomena utamanya berbeda.

---

## 20. Ringkasan

P5 adalah modul karakterisasi. Tujuan utamanya bukan sekadar membuat motor berputar, tetapi membaca perilaku motor dari data. Mahasiswa harus mampu menjelaskan operating point, membangun grafik, menghubungkan `V`, `I`, `E`, `T`, `rpm`, `Pin`, `Pout`, rugi, dan efisiensi dalam satu cerita teknik yang konsisten.