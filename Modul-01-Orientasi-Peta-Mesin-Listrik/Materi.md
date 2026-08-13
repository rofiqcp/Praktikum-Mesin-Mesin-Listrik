# Modul 01 — Orientasi, Brainstorming, dan Peta Mesin-Mesin Listrik

**Durasi:** 3 × 50 menit  
**Fokus:** memahami hubungan transformator, motor DC, motor induksi, mesin sinkron, sistem starter, pengukuran, dan analisis data sebelum praktik detail.

## Capaian
Mahasiswa mampu menjelaskan aliran energi listrik–magnet–mekanik, membedakan fungsi transformator dan motor, membaca nameplate, memilih alat ukur, serta menggambar hubungan materi P1–P16.

## 1. Peta Besar
- **Transformator:** energi listrik AC → medan magnet → energi listrik AC pada level tegangan berbeda.
- **Motor DC:** listrik DC → fluks + arus jangkar → torsi → putaran.
- **Motor induksi 3 fasa:** medan putar stator → arus rotor terinduksi → slip → torsi.
- **Mesin sinkron:** kecepatan rotor mengikuti kecepatan sinkron; eksitasi memengaruhi tegangan dan faktor daya.
- **Rangkaian kendali:** tombol, kontaktor, overload, timer, interlock, latching, forward–reverse, star–delta.
- **Pengukuran:** tegangan, arus, daya, putaran, slip, suhu, faktor daya, efisiensi.
- **Analisis:** teori → simulasi → wiring → uji → data → grafik → kesimpulan.

## 2. Hubungan Materi Semester
`P1 peta konsep → P2-P3 trafo → P4-P5 motor DC → P6 motor induksi → P7 kendali kontaktor → P8 responsi → P9-P11 motor induksi lanjutan → P12 trafo 3 fasa/project → P13 motor 1 fasa → P14 mesin sinkron → P15 integrasi diagnosis → P16 responsi akhir`.

## 3. Software
1. **CADe SIMU**: fokus rangkaian daya/kontrol kontaktor, latching, forward–reverse, star–delta.
2. **Python/Google Colab**: perhitungan dan grafik karakteristik.
3. **GNU Octave/MATLAB**: matriks, persamaan, curve fitting, model matematis.
4. **OpenModelica (opsional)**: model dinamik mesin listrik.
5. **Node.js**: pengolahan CSV dan laporan otomatis.

## 4. Brainstorming Lima Sistem
### Transformator
Pertanyaan awal: mengapa tegangan berubah tetapi frekuensi tetap? Apa efek beban terhadap V2 dan arus primer?

### Motor DC
Apa yang mengubah arah? Mengapa arus start besar? Apa hubungan back-EMF dengan kecepatan?

### Motor Induksi
Mengapa rotor tidak tepat sama dengan kecepatan sinkron? Apa fungsi star–delta?

### Forward–Reverse dan Latching
Mengapa interlock wajib? Mengapa kontaktor tidak boleh forward dan reverse aktif bersamaan?

### Pengukuran
Setiap praktik harus mempunyai tabel **teori, simulasi, hasil ukur, error, analisis**.

## 5. Keselamatan Wajib
- Praktik daya AC hanya pada trainer yang dilengkapi MCB/fuse, E-stop, grounding, dan pengawasan dosen/laboran.
- Wiring dilakukan saat sumber **OFF**, verifikasi continuity sebelum energize.
- Jangan mengubah hubungan star/delta atau arah putaran saat terminal terbuka bertegangan.
- Gunakan sumber tegangan rendah untuk latihan awal bila tersedia.

## 6. Mini Formula Map
- Trafo ideal: `V1/V2 = N1/N2 = I2/I1`
- Motor DC: `E = V - IaRa`, `T ∝ Phi Ia`, `n ∝ E/Phi`
- Motor induksi: `Ns = 120 f / P`, `s = (Ns-Nr)/Ns`
- Daya 3 fasa: `P = sqrt(3) VL IL cos(phi)`
- Efisiensi: `eta = Pout/Pin × 100%`

## Ringkasan
Pertemuan ini tidak mengejar detail perhitungan. Targetnya adalah satu peta mental yang akan diisi bertahap pada P2–P15 tanpa pengulangan tujuan praktikum.