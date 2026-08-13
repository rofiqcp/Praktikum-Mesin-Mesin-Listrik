# Modul 05 — Motor DC: Karakteristik Beban, Kecepatan–Torsi, PWM, dan Efisiensi

## Batas Materi
P4 sudah membahas starting, back-EMF, dan reversal. P5 fokus **performa steady-state terhadap beban** dan pengaturan kecepatan pada motor DC tegangan rendah.

## Capaian
Mahasiswa mampu membuat kurva `rpm vs arus`, `torsi vs arus`, `rpm vs torsi`, menghitung daya masuk/keluar dan efisiensi, serta membandingkan kontrol tegangan/PWM secara konseptual.

## Dasar
Untuk fluks hampir konstan:
- `T ≈ kT Ia`
- `n ≈ (V-IaRa)/(kE Phi)`
- `Pin = V I`
- `Pmech = T omega`
- `eta = Pmech/Pin × 100%`

Beban bertambah → arus jangkar naik → torsi naik → drop `IaRa` naik → rpm cenderung turun.

## PWM
PWM mengubah tegangan rata-rata efektif pada motor melalui duty cycle. Praktikum memakai driver PWM yang sesuai rating; jangan menghubungkan PWM logic langsung ke motor besar. Catat duty, V rata-rata, I, rpm.

## Uji Beban
Gunakan dynamometer/trainer, rem mekanik resmi, atau beban terukur yang tersedia. Jangan menahan shaft dengan tangan. Jika torsi tidak dapat diukur langsung, gunakan data trainer atau estimasi yang disediakan.

## Analisis
Kurva utama modul ini adalah karakteristik motor DC. Parameter starting tidak diuji ulang kecuali sebagai konteks keselamatan.