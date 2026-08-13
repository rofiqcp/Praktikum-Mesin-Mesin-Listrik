# Modul 12 — Transformator 3 Fasa: Koneksi Y/Δ, Rasio Line–Phase, dan Vector Group

## Batas Materi
P2-P3 fokus trafo 1 fasa. P12 memperluas ke **sistem tiga fasa dan hubungan vector**, lalu ditutup project. Tidak mengulang uji regulasi 1 fasa.

## Hubungan Dasar
Untuk koneksi Y: `VL=sqrt(3)Vph`. Untuk Δ: `VL=Vph`.
Rasio tegangan line transformator tiga fasa bergantung rasio lilitan per fasa **dan** jenis koneksi sisi primer/sekunder.

## Contoh
Y-Y: rasio line sama dengan rasio lilitan per fasa.
Δ-Δ: rasio line sama dengan rasio lilitan per fasa.
Δ-Y atau Y-Δ: muncul faktor `sqrt(3)` pada perbandingan line.

## Vector Group
Vector group menyatakan koneksi winding, netral, dan pergeseran sudut. Mahasiswa fokus membaca notasi dasar seperti Dyn11/Yyn0 dan memahami bahwa phase shift penting saat paralel/terhubung ke sistem lain.

## Pengukuran
Gunakan trainer transformator 3 fasa/3 unit trafo identik tegangan rendah sesuai SOP. Verifikasi polaritas dan kesamaan rasio sebelum membuat bank. Jangan memparalelkan sekunder tanpa verifikasi rasio, polaritas, dan phase displacement.

## Analisis
Bandingkan Vline/Vphase pada Y dan Δ, hitung rasio line, dan visualisasikan phasor dengan program Python.