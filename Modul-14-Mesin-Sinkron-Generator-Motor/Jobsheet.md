# Jobsheet 14 — Mesin Sinkron

## Bagian A — rpm terhadap frekuensi
Untuk jumlah pole pada trainer, hitung rpm sinkron pada 25, 40, 50, dan 60 Hz.

## Bagian B — OCC Generator
Jika trainer tersedia, gunakan prosedur resmi untuk mengambil beberapa titik arus eksitasi dan tegangan no-load pada kecepatan yang ditetapkan pengajar. Bila hardware tidak tersedia, gunakan dataset/program.

| If | rpm | f | V no-load |
|---:|---:|---:|---:|
||||

## Bagian C — V-Curve
Jika trainer mendukung motor sinkron, gunakan data yang disediakan/diambil sesuai SOP. Plot arus stator terhadap arus eksitasi.

## Program
```bash
python program/synchronous_machine.py
```

## Analisa
1. Mengapa frekuensi terkait rpm dan pole?
2. Mengapa OCC melengkung pada eksitasi tinggi?
3. Apa arti under-excited dan over-excited secara konseptual?
4. Bedakan slip motor induksi dengan operasi sinkron.