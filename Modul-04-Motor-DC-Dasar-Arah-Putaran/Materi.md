# Modul 04 — Motor DC: Back-EMF, Torsi, Starting, dan Arah Putaran

## Batas Materi
P4 membahas **dasar elektromekanik, starting, dan reversal**. P5 nanti fokus kurva karakteristik, PWM/tegangan, efisiensi, dan analisis beban.

## Dasar Teori
Persamaan jangkar: `V = E + IaRa` sehingga `E = V-IaRa`. Back-EMF meningkat ketika motor berputar. Saat start `E≈0`, sehingga arus dapat besar dan perlu pembatas sesuai sistem.

Torsi elektromagnetik: `T = k Phi Ia`. Kecepatan kira-kira `n ∝ (V-IaRa)/Phi`.

## Arah Putaran
Arah torsi berubah jika **salah satu** dari arah arus jangkar atau arah fluks dibalik. Jika keduanya dibalik bersamaan, arah torsi tetap.

Untuk motor PMDC trainer, reversal paling mudah dengan membalik polaritas jangkar menggunakan H-bridge/relay DPDT yang sesuai rating. Untuk mesin DC wound-field, ikuti terminal dan SOP trainer.

## Starting
- Motor kecil PMDC: supply/driver dengan current limit.
- Mesin DC lebih besar: starter/resistor atau drive yang sesuai.
- Jangan menahan rotor untuk pengujian tanpa prosedur dan pembatas arus.

## Pengamatan Utama
V, Ia, rpm, arah, dan transien arus start. P4 tidak mengejar efisiensi detail; itu tugas P5.

## Simulasi
Model sederhana memakai `J dω/dt = Tm - Bω - TL` dan `L di/dt = V - Ri - keω`. Program Python menunjukkan arus start, back-EMF, dan kecepatan.