# Jobsheet 06 — Motor Induksi 3 Fasa Dasar

## Keselamatan
Praktik tiga fasa wajib menggunakan trainer, proteksi, grounding, E-stop, dan supervisi. Wiring/pertukaran fasa dilakukan saat isolator OFF dan diverifikasi.

## Percobaan A — Nameplate dan Terminal U1-V1-W1/U2-V2-W2
Catat tegangan star/delta, arus, kW, cos phi, frekuensi, rpm, kelas isolasi.

## Percobaan B — Hubungan Star
Susun sesuai diagram nameplate/trainer. Ukur `VL`, arus tiap line, rpm. Hitung `Vph` dan slip.

## Percobaan C — Hubungan Delta
Hanya jika rating motor/trainer mengizinkan pada tegangan sumber. Ulangi data. Jangan membuat asumsi bahwa semua motor boleh delta pada sumber yang tersedia.

## Percobaan D — Balik Arah
Matikan sumber. Tukar dua fasa. Energize kembali dan verifikasi arah.

## Program
```bash
python program/star_delta_calc.py
```
Masukkan tegangan, frekuensi, pole, dan rpm hasil ukur.

## Analisa
1. Bandingkan arus line star dan delta dalam kondisi trainer.
2. Mengapa rotor tidak mencapai Ns?
3. Apa dampak salah konfigurasi nameplate?
4. Apa indikator ketidakseimbangan antar fasa?