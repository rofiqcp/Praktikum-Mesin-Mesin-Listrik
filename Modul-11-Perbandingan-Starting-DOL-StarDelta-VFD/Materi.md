# Modul 11 — Perbandingan Starting Motor Induksi: DOL, Star–Delta, dan VFD

## Batas Materi
P7 sudah mengajarkan **cara membuat logic star–delta**. P11 tidak mengulang ladder; fokusnya adalah **membandingkan performa starting**: arus inrush, waktu akselerasi, torsi relatif, stress mekanik, dan kualitas start.

## DOL
DOL memberi tegangan line penuh ke motor. Sederhana dan torsi start tinggi, tetapi arus start dapat besar.

## Star–Delta
Pada fase star, tegangan per winding lebih rendah daripada kondisi run-delta pada suplai yang sama. Secara ideal arus line dan torsi start berkurang; torsi kira-kira berbanding kuadrat tegangan.

## VFD
VFD mengatur frekuensi dan tegangan, memungkinkan ramp percepatan. Untuk motor 4 pole, sinkron speed berubah mengikuti `Ns=120f/P`. Praktikum VFD hanya jika unit trainer tersedia dan parameter setting mengikuti manual/SOP.

## Indikator Perbandingan
- peak current,
- RMS/current trend,
- time to 90% speed,
- transient speed dip saat transfer star→delta,
- bunyi/getaran kualitatif,
- suitability terhadap beban.

## Analisis
Gunakan data logger/power meter jika tersedia. Jika tidak, gunakan dataset instruktur dan program simulasi envelope.