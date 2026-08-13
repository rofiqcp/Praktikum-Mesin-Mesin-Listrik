# Modul 02 — Transformator 1 Fasa: Rasio, Polaritas, dan Uji Tanpa Beban

## Batas Materi
Modul ini hanya membahas **identitas trafo dan kondisi tanpa beban**. Regulasi, efisiensi beban, dan uji hubung-singkat dibahas pada P3 agar tidak overlap.

## Tujuan
- Menentukan rasio lilitan dari pengukuran V1 dan V2.
- Memahami polaritas terminal dan prinsip induksi.
- Mengukur arus tanpa beban serta menghitung rugi inti secara sederhana.

## Teori
Trafo ideal memenuhi `a=N1/N2=V1/V2=I2/I1`. Pada kondisi nyata terdapat rugi tembaga, rugi histeresis, eddy current, fluks bocor, dan arus magnetisasi.

Pada uji tanpa beban, sekunder terbuka. Sisi primer diberi tegangan nominal/rendah sesuai trainer. Daya masukan terutama merepresentasikan rugi inti dan rugi kecil pada primer.

`P0 = V0 I0 cos(phi0)`

Komponen arus: `Iw = I0 cos(phi0)` dan `Im = I0 sin(phi0)`. Jika wattmeter tidak tersedia, fokuskan eksperimen pada V1, V2, I0 dan rasio.

## Polaritas
Penandaan H1-H2/X1-X2 atau titik polaritas menentukan fase relatif. Kesalahan menggabungkan lilitan seri dapat menyebabkan tegangan saling menambah atau mengurangi.

## Pengukuran
- Voltmeter dipasang paralel.
- Clamp meter menghindari membuka rangkaian arus bila sesuai rentang.
- Mulai dari tegangan rendah/variac pada trainer dan naikkan bertahap.
- Sekunder harus benar-benar tanpa beban untuk uji ini.

## Analisis Wajib
Bandingkan rasio nameplate, rasio teori, dan rasio hasil ukur. Hitung error persentase. Plot V2 terhadap V1; kemiringan mendekati `N2/N1` sebelum saturasi/rugi dominan.