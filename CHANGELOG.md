# Changelog

## v1 — 13 Agustus 2026
- Menyusun 16 pertemuan Praktikum Mesin-Mesin Listrik.
- Menambahkan Materi.md dan Jobsheet.md pada setiap pertemuan.
- Menambahkan TugasVideo.md pada P1–P7, P9–P11, P13–P15.
- Menggunakan Project.md pada P8, P12, dan P16.
- Menambahkan contoh program Python pada semua modul, Octave/MATLAB pada modul terpilih, dan Node.js untuk peta konsep serta analisis laporan.
- Menambahkan panduan CADe SIMU, Google Colab, dan aktivitas Scratch konseptual.
- Memisahkan ruang lingkup materi untuk mencegah overlap antarpertemuan.
- Menambahkan validator struktur dan workflow GitHub Actions.

### Pendalaman P1–P4
- Memperluas teori, jobsheet, tugas, contoh hitung, analisis data, dan program P1–P4.
- Menambahkan contoh kalkulasi dasar, sweep transformator tanpa beban, serta analisis model motor DC.

### Pendalaman P5–P8
- P5 diperluas menjadi karakterisasi motor DC berbasis data: speed–torque, current–load, daya, rugi, efisiensi, PWM model, validasi data, `Analisis-Data.md`, `Worksheet-Grafik.md`, dan panduan program.
- P6 diperluas menjadi dasar motor induksi tiga fasa yang jelas batasnya: rotating magnetic field, `Ns`, slip, frekuensi rotor, nameplate, line–phase, star/delta, `Analisis-Data.md`, `Worksheet-Nameplate-Slip.md`, dan tugas analisis pendamping.
- P7 diperluas khusus logika kendali/simulasi: latching, truth table, mutual exclusion, state machine, permissive, timer event, invariant, fault injection, jobsheet test case, tugas video, dan `Worksheet-TruthTable.md`.
- P8 diperdalam sebagai responsi integratif tanpa teori baru melalui `Formula-Ringkas.md`, bank soal per kelompok materi, `Project-Simulasi.md`, `README.md`, serta program latihan numerik.
- Seluruh pendalaman P5–P8 diterapkan langsung ke branch `v1`.

### Pendalaman P9–P12
- P9 diperluas menjadi model elektromagnetik motor induksi: rangkaian ekivalen, `R2'/s`, aliran air-gap power, frekuensi rotor, Thevenin, starting torque, breakdown torque, pengaruh tegangan dan resistansi rotor, validasi model, serta `Jobsheet-Lengkap.md` dan panduan program.
- P10 diperluas menjadi analisis steady-state load performance: daya tiga fasa, slip, torsi, `Pin/Pout`, rugi total, PF, efisiensi, quality check, sensitivity study, jobsheet delapan grafik, serta `load_sweep_summary.py` dan panduan running.
- P11 diperluas khusus evaluasi starting: DOL/star-delta/VFD sebagai performance comparison, per-unit, `T∝V²`, V/f, ramp frequency, torque margin, model beban, sweep inersia, transition study, decision matrix, `vfd_ramp.py`, `Analisis-Perbandingan.md`, dan README program.
- P12 diperdalam sebagai project transformator tiga fasa melalui `Project.md` yang lebih lengkap dan README program untuk analisis empat koneksi serta fasor; Materi/Jobsheet dasar tetap menjadi fondasi line–phase dan vector group.
- Batas anti-overlay dikunci: P9=model, P10=load performance, P11=starting performance, P12=transformator tiga fasa/vector group.

### Audit P1–P16
- Mengoreksi `KURIKULUM.md` agar peta P9–P15 sesuai struktur aktual repository.
- Menambahkan `parameter_sweep.py` P9 yang sebelumnya sudah disebut sebagai program wajib tetapi belum tersedia.
- Menambahkan `decision_matrix.py` P11 yang sebelumnya sudah disebut sebagai program wajib tetapi belum tersedia.
- Menyinkronkan README program P9 dan P11 dengan script yang benar-benar tersedia.
- Mengoreksi dataset baseline P5 agar perhitungan efisiensi contoh tidak menghasilkan nilai di atas 100%.
- Menjalankan ulang validator struktur, compile seluruh Python, eksekusi program non-interaktif, serta program Node.js melalui GitHub Actions.