# Jobsheet 11 — Perbandingan Starting DOL, Star–Delta, dan VFD

## Tujuan
Membandingkan tiga metode starting berdasarkan arus relatif, torsi awal, waktu akselerasi, torque margin, kehalusan profil, dan kebutuhan aplikasi.

## A. Baseline
Gunakan nilai per-unit:

```text
Vrated = 1 pu
Irated = 1 pu
Trated = 1 pu
frated = 1 pu
```

Tetapkan parameter model:

| Parameter | Nilai |
|---|---:|
| inertia J | ... |
| damping B | ... |
| load type | constant / fan |
| target speed pu | ... |
| ramp time VFD | ... s |

## B. Prediksi
Sebelum program, urutkan DOL, star–delta, VFD dari:
1. arus awal terbesar;
2. torsi awal terbesar;
3. profil paling halus;
4. fleksibilitas kontrol tertinggi.

Berikan alasan.

## C. DOL Baseline
Catat output model:

| Indikator | Nilai |
|---|---:|
| Istart pu | |
| Tstart pu | |
| acceleration time | |
| minimum torque margin | |

## D. Star Starting
Gunakan pendekatan:

```text
Vphase_star / Vphase_delta = 1/sqrt(3)
Tstar/Tdelta ≈ 1/3
```

Hitung manual torsi relatif jika `T_DOL=1.8 pu`.

Analisis apakah torsi tersebut cukup untuk beban `0.4 pu`, `0.7 pu`, dan `1.0 pu`.

## E. VFD Ramp
Bandingkan ramp:
- 2 s;
- 5 s;
- 10 s.

Catat:

| Ramp | peak I | minimum Tmargin | acceleration time | smoothness note |
|---:|---:|---:|---:|---|
|2 s|||||
|5 s|||||
|10 s|||||

## F. Dua Profil Beban
Jalankan minimal:

### Constant torque
`Tload = konstan`

### Fan-type
`Tload = k*speed^2`

Bandingkan metode mana yang paling terpengaruh oleh perubahan karakteristik beban.

## G. Sweep Inersia
Ulangi dengan `J=0.5×`, `1×`, dan `2×` baseline.

| J factor | DOL time | Star-delta time | VFD time |
|---:|---:|---:|---:|
|0.5||||
|1.0||||
|2.0||||

## H. Transition Study
Gunakan model star–delta dengan tiga waktu transisi yang berbeda. Amati perubahan kecepatan saat perpindahan dan torque margin setelah transisi. Fokus pada interpretasi profil, bukan detail wiring.

## I. Program Wajib
```bash
python Modul-11-Perbandingan-Starting-DOL-StarDelta-VFD/program/starting_compare.py
python Modul-11-Perbandingan-Starting-DOL-StarDelta-VFD/program/vfd_ramp.py
python Modul-11-Perbandingan-Starting-DOL-StarDelta-VFD/program/decision_matrix.py
```

## J. Decision Matrix
Buat bobot 1–5 untuk:
- batas arus;
- kebutuhan starting torque;
- speed control;
- kehalusan proses;
- kompleksitas;
- biaya relatif;
- maintenance.

Kemudian beri skor DOL/star–delta/VFD. Sertakan alasan untuk setiap bobot.

## K. Kasus Aplikasi
Pilih tiga kasus konseptual:
1. pompa/fan;
2. conveyor constant-torque;
3. mesin dengan inersia tinggi.

Untuk tiap kasus rekomendasikan metode starting dan tulis minimal tiga alasan.

## L. Pertanyaan
1. Mengapa star–delta menurunkan torsi sekaligus arus?
2. Mengapa DOL bukan selalu pilihan buruk?
3. Mengapa VFD lebih fleksibel?
4. Apa hubungan V/f dengan fluks secara konseptual?
5. Apa pengaruh inersia terhadap acceleration time?
6. Mengapa constant-torque load lebih berat saat reduced-voltage start?
7. Mengapa “arus paling kecil” bukan satu-satunya tujuan?
8. Apa beda P7 dan P11?

## M. Deliverable
- perhitungan manual star vs delta;
- output tiga program;
- tabel ramp VFD;
- tabel sweep inersia;
- grafik/profil per metode;
- decision matrix;
- rekomendasi tiga kasus;
- jawaban delapan pertanyaan.

## N. Rubrik
Perhitungan 15%, program 20%, eksperimen numerik 25%, decision matrix 15%, analisis aplikasi 20%, kerapian 5%.