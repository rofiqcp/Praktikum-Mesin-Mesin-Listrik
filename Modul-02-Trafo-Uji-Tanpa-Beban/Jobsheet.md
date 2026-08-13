# Jobsheet 02 — Uji Tanpa Beban Transformator 1 Fasa

## Keselamatan
Gunakan trainer berisolasi/proteksi. Wiring hanya saat sumber OFF. Verifikasi rating primer sebelum energize.

## Alat
Trafo 1 fasa trainer, sumber AC/variac sesuai SOP, multimeter 2 buah, clamp meter, wattmeter/power meter bila tersedia.

## Percobaan A — Rasio Tegangan
1. Catat nameplate dan terminal.
2. Hubungkan sekunder tanpa beban.
3. Naikkan V1 bertahap: 20%, 40%, 60%, 80%, 100% rating trainer.
4. Catat V1, V2, I0.

| No | V1 | V2 | I0 | V1/V2 | Error rasio |
|---|---:|---:|---:|---:|---:|
|1||||||
|2||||||

## Percobaan B — Polaritas
Dengan prosedur laboratorium yang disetujui, verifikasi apakah dua lilitan bantu tersusun additive atau subtractive. Jangan melakukan perubahan koneksi ketika sumber ON.

## Percobaan C — Simulasi Python
```bash
python program/trafo_no_load.py
```
Ubah parameter `ratio` dan `loss_factor`, lalu bandingkan kurva ideal vs model sederhana.

## Analisa
1. Apakah V2/V1 konstan?
2. Mengapa I0 tetap ada walaupun sekunder terbuka?
3. Apa akibat salah memilih terminal primer?
4. Hitung deviasi rasio terbesar.

## Laporan
Masukkan grafik V1-V2, tabel ukur, screenshot terminal, dan kesimpulan hubungan rasio lilitan terhadap tegangan.