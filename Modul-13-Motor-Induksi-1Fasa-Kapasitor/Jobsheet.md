# Jobsheet 13 — Motor Induksi 1 Fasa dan Kapasitor

## Tujuan
Mengidentifikasi winding utama/bantu pada trainer, memahami fungsi kapasitor, mencatat arus dan rpm, serta menghubungkan hasil ukur dengan model reaktansi kapasitif.

## Praktik Terarah
1. Catat nameplate dan diagram terminal trainer.
2. Dengan sumber terisolasi/OFF, identifikasi terminal sesuai label pabrikan.
3. Pengajar memverifikasi konfigurasi sebelum trainer diaktifkan.
4. Catat V, arus running, rpm, dan arah pada konfigurasi normal.
5. Bila trainer menyediakan mode reversal bawaan, lakukan sesuai prosedur panel tanpa membuka wiring hidup.

| Kondisi | V | I_run | rpm | arah |
|---|---:|---:|---:|---|
|Normal|||||
|Mode 2/reverse trainer|||||

## Program
```bash
python program/single_phase_capacitor.py
```

## Analisa
1. Mengapa winding bantu diperlukan?
2. Apa pengaruh C terhadap Xc?
3. Mengapa komponen kapasitor harus sesuai rating mesin/trainer?
4. Jelaskan hubungan phase shift dengan starting torque secara kualitatif.