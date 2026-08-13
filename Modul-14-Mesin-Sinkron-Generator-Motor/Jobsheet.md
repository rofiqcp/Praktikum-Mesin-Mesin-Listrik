# Jobsheet 14 — Mesin Sinkron

Gunakan juga `Jobsheet-Lengkap.md` untuk langkah analisis yang lebih rinci.

## Bagian A — rpm terhadap frekuensi
Untuk jumlah pole pada trainer, hitung rpm sinkron pada 25, 40, 50, dan 60 Hz.

## Bagian B — OCC Generator
Gunakan dataset/program yang tersedia untuk mempelajari hubungan arus eksitasi dan tegangan no-load pada kecepatan yang ditetapkan.

| If | rpm | f | V no-load |
|---:|---:|---:|---:|
||||

## Bagian C — V-Curve
Gunakan data yang tersedia untuk memplot arus stator terhadap arus eksitasi dan menentukan titik arus minimum.

## Program
```bash
python program/synchronous_machine.py
python program/synchronous_analysis.py
```

## Analisis
1. Mengapa frekuensi terkait rpm dan pole?
2. Mengapa OCC melengkung pada eksitasi tinggi?
3. Apa arti under-excited dan over-excited secara konseptual?
4. Bedakan slip motor induksi dengan operasi sinkron.