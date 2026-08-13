# Jobsheet 04 — Motor DC Dasar dan Reversal

## Tujuan
Mengukur arus start/steady, menghubungkan back-EMF dengan rpm, dan mempraktikkan pembalikan arah secara aman.

## Hardware
Motor DC trainer/PMDC tegangan rendah, supply current-limit, fuse, driver/H-bridge atau saklar reversal sesuai rating, tachometer, multimeter/clamp DC.

## Percobaan A — No Load Start
1. Set current limit sesuai rating trainer.
2. Pastikan motor bebas bergerak.
3. Energize pada tegangan rendah.
4. Catat V, arus puncak (jika alat mendukung), arus steady, rpm.
5. Ulangi pada 3 level tegangan yang diizinkan.

## Percobaan B — Forward/Reverse
Matikan supply sebelum mengubah wiring manual. Bila memakai H-bridge/driver, beri jeda stop sebelum reverse. Catat polaritas dan arah.

## Percobaan C — Simulasi
```bash
python program/motor_dc_start.py
```
Ubah `V`, `load_torque`, dan `R`. Amati hubungan arus start dan back-EMF.

## Tabel
| V | I_start | I_steady | rpm | arah |
|---:|---:|---:|---:|---|
|||||

## Analisa
1. Mengapa arus tertinggi muncul dekat t=0?
2. Mengapa arus turun setelah rpm naik?
3. Apa yang terjadi jika polaritas supply dibalik pada motor PMDC?
4. Mengapa motor harus stop sebelum reversal pada sistem mekanik tertentu?