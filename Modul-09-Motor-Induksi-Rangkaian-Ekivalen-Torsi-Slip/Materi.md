# Modul 09 — Motor Induksi: Rangkaian Ekivalen, Slip, dan Kurva Torsi–Kecepatan

## Batas Materi
P6 membahas terminal, star/delta, arah, dan slip dasar. P7 membahas kendali kontaktor. P9 kini membahas **model elektromagnetik dan kurva torsi–kecepatan**, bukan mengulang wiring starter.

## Capaian
Mahasiswa mampu:
1. menjelaskan rangkaian ekivalen per fasa,
2. menghubungkan slip dengan frekuensi rotor,
3. menghitung torsi dari parameter model sederhana,
4. mengidentifikasi daerah starting, pull-out/breakdown, dan operasi normal.

## 1. Slip dan Frekuensi Rotor
`Ns = 120 f / P`, `s=(Ns-Nr)/Ns`, `fr=s f`.
Pada rotor diam `s=1`. Saat mendekati Ns, slip kecil dan frekuensi rotor rendah.

## 2. Rangkaian Ekivalen Per Fasa
Model umum berisi `R1, X1, Xm, Rc, R2'/s, X2'`. Bagian `R2'/s` membuat efek beban mekanik muncul di model listrik.

Untuk praktikum komputasi digunakan bentuk Thevenin agar kurva torsi lebih mudah dihitung:
`T = 3 Vth^2 (R2'/s) / [ws ((Rth+R2'/s)^2 + (Xth+X2')^2)]`.

## 3. Interpretasi Kurva
- s=1: starting torque.
- slip turun: torsi naik sampai breakdown torque.
- dekat kecepatan sinkron: slip kecil, daerah operasi normal.
- s<0: mode generator secara teoritis, dibahas hanya sebagai interpretasi kurva.

## 4. Data Praktikum
Gunakan parameter motor trainer/dataset yang diberikan. Jika laboratorium memiliki prosedur no-load/locked-rotor khusus, data hasil uji dapat dipakai; **locked-rotor tidak dilakukan secara improvisasi** karena arus tinggi.

## 5. Analisis
Plot torsi vs rpm dan torsi vs slip, lalu tandai titik operasi berdasarkan rpm aktual P6 atau data baru. Bandingkan torsi model dengan perubahan arus yang diamati.