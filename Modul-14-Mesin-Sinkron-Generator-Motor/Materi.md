# Modul 14 — Mesin Sinkron: Generator, Eksitasi, Frekuensi, dan Faktor Daya

## Capaian
Mahasiswa mampu menghubungkan kecepatan sinkron dengan frekuensi, menjelaskan pengaruh eksitasi terhadap tegangan generator, dan membaca kurva OCC/V-curve dari trainer atau dataset.

## Kecepatan Sinkron
`Ns = 120f/P`, dan untuk generator `f = Pn/120`. Pada operasi sinkron steady-state, rotor mengikuti kecepatan medan putar.

## Generator Sinkron
Eksitasi rotor membangun fluks. Ketika rotor digerakkan prime mover pada kecepatan tertentu, stator menghasilkan tegangan AC. Pada no-load, kurva OCC menunjukkan tegangan meningkat terhadap arus eksitasi lalu melengkung ketika saturasi magnetik mulai dominan.

## Regulasi dan Beban
Tegangan terminal berubah terhadap beban karena impedansi internal dan faktor daya beban. Praktikum ini fokus pada pengamatan data trainer/dataset dan tidak melakukan paralel bebas ke jaringan utilitas.

## Motor Sinkron dan V-Curve
Pada trainer yang mendukung mode motor sinkron, perubahan eksitasi pada beban mekanik tetap akan mengubah arus stator dan faktor daya. V-curve memperlihatkan arus stator terhadap arus eksitasi.

## Keselamatan
Gunakan mode trainer yang telah ditetapkan pengajar. Tidak melakukan sinkronisasi ke jaringan umum. Jika trainer mempunyai bus sinkronisasi, hanya demonstrasi prosedur resmi laboratorium yang boleh dilakukan.

## Analisis
Program Python menghasilkan relasi rpm–frekuensi, OCC sintetis, dan V-curve sederhana sebagai pembanding konsep.