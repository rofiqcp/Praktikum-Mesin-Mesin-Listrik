# P11 — Lembar Analisis Perbandingan

Gunakan bersama `Jobsheet.md`.

## Tabel Ringkasan
| Metode | Peak current pu | Starting torque rel. | Waktu target | Kelebihan | Keterbatasan |
|---|---:|---:|---:|---|---|
|DOL||||||
|Star–Delta||||||
|VFD model||||||

## Ramp Study
Isi hasil `vfd_ramp.py`:

| Ramp | f pada 25% waktu | f pada 50% | f pada 75% | f akhir |
|---:|---:|---:|---:|---:|
|2 s|||||
|5 s|||||
|10 s|||||

## Inertia Study
Gunakan hasil model/analisis kelas untuk membandingkan faktor inersia 0.5×, 1×, dan 2×. Tulis apakah acceleration time berubah sesuai prediksi.

## Beban
Bandingkan dua profil:
- constant torque;
- torque yang meningkat terhadap kuadrat kecepatan.

Jelaskan metode mana yang lebih sensitif terhadap kebutuhan torque awal.

## Decision Matrix Manual
Berikan bobot 1–5 untuk:
- current limit;
- starting torque;
- speed control;
- smoothness;
- simplicity;
- relative cost.

Jangan hanya menjumlah skor. Jelaskan mengapa bobot dipilih.

## Kesimpulan
Buat tiga rekomendasi terpisah untuk:
1. aplikasi yang mengutamakan kesederhanaan;
2. aplikasi dengan batas arus ketat;
3. aplikasi yang membutuhkan pengaturan kecepatan.