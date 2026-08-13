# Jobsheet 11 — DOL vs Star–Delta vs VFD

## Tahap A — Prediksi
Isi tabel prediksi sebelum pengujian: metode mana yang memiliki arus peak terbesar, akselerasi tercepat, transisi paling halus.

## Tahap B — Pengukuran
Untuk setiap metode yang tersedia pada trainer, catat:
| Metode | I_peak | I_steady | t90 rpm | rpm akhir | catatan transien |
|---|---:|---:|---:|---:|---|
|DOL||||||
|Star-Delta||||||
|VFD||||||

Jangan mengubah parameter VFD di luar parameter yang ditetapkan pengajar.

## Tahap C — Program
```bash
python program/starting_compare.py
```
Ubah parameter envelope agar mendekati data lab.

## Analisa
1. Mengapa star mengurangi torsi start?
2. Apa yang menyebabkan current spike saat transisi star→delta?
3. Mengapa VFD dapat memberi ramp lebih halus?
4. Metode mana yang cocok untuk beban dengan starting torque tinggi?

## Deliverable
Satu grafik overlay arus dan rpm, tabel perbandingan, dan rekomendasi metode berdasarkan jenis beban.