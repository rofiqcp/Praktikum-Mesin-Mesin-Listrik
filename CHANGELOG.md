# Changelog

## v1 — 13–14 Agustus 2026
- Menyusun 16 pertemuan Praktikum Mesin-Mesin Listrik.
- Menambahkan `Materi.md` dan `Jobsheet.md` pada setiap pertemuan.
- Menambahkan `TugasVideo.md` pada P1–P7, P9–P11, P13–P15.
- Menggunakan `Project.md` pada P8, P12, dan P16.
- Menambahkan contoh program Python pada semua modul, Octave/MATLAB pada modul terpilih, dan Node.js untuk peta konsep serta analisis laporan.
- Menambahkan panduan CADe SIMU, Google Colab, dan aktivitas Scratch konseptual.
- Memisahkan ruang lingkup materi untuk mencegah overlap antarpertemuan.
- Menambahkan validator struktur dan workflow GitHub Actions.

### Pendalaman P1–P4
- Memperluas teori, jobsheet, tugas, contoh hitung, analisis data, dan program P1–P4.
- Menambahkan contoh kalkulasi dasar, sweep transformator tanpa beban, serta analisis model motor DC.

### Pendalaman P5–P8
- P5 diperluas menjadi karakterisasi motor DC berbasis data: speed–torque, current–load, daya, rugi, efisiensi, PWM model, validasi data, `Analisis-Data.md`, `Worksheet-Grafik.md`, dan panduan program.
- P6 diperluas menjadi dasar motor induksi tiga fasa: rotating magnetic field, `Ns`, slip, frekuensi rotor, nameplate, line–phase, star/delta, analisis data, dan worksheet.
- P7 diperluas khusus logika kendali/simulasi: latching, truth table, mutual exclusion, state machine, permissive, timer event, invariant, fault injection, CADe SIMU, dan Python.
- P8 diperdalam sebagai responsi integratif melalui formula ringkas, bank soal, project simulasi, dan program latihan numerik.

### Pendalaman P9–P12
- P9 diperluas menjadi model elektromagnetik motor induksi: rangkaian ekivalen, `R2'/s`, air-gap power, frekuensi rotor, Thevenin, starting torque, breakdown torque, parameter sweep, dan validasi model.
- P10 diperluas menjadi analisis load performance: daya tiga fasa, slip, torsi, `Pin/Pout`, rugi total, PF, efisiensi, quality check, sensitivity study, grafik, serta `load_sweep_summary.py`.
- P11 diperluas khusus evaluasi starting DOL/star-delta/VFD: per-unit, `T∝V²`, V/f, ramp frequency, torque margin, model beban, decision matrix, dan tiga program analisis.
- P12 diperdalam sebagai project transformator tiga fasa melalui `Pendalaman-P12.md`, Project yang lebih lengkap, `three_phase_transformer.py`, serta `vector_group_analysis.py` untuk clock notation, rasio line, dan pemeriksaan dataset tiga-line.

### Pendalaman P13–P16
- P13 diperluas signifikan: medan pulsasi/double-revolving-field, winding utama dan bantu, jenis motor satu fasa, `Xc`, slip, daya, efisiensi, validasi data, jobsheet analisis, tugas video, dataset `data_single_phase.csv`, dan `single_phase_performance.py`.
- P14 diperluas menjadi modul mesin sinkron yang lengkap: rpm–frequency–pole, generator/motor, eksitasi, OCC, saturasi, V-curve, daya tiga fasa, power-angle konseptual, validasi data, `Jobsheet-Lengkap.md`, dataset OCC/V-curve, dan `synchronous_analysis.py`.
- P15 diperluas menjadi workflow integrasi data lintas mesin: baseline, data dictionary, quality check bertingkat, outlier, hipotesis, data pembeda, confidence level, `Jobsheet-Lengkap.md`, `TugasVideo-Lengkap.md`, `multi_machine_cases.csv`, dan `multi_machine_diagnostics.py`.
- P16 diperdalam melalui `Materi-Lengkap.md`, `Jobsheet-Lengkap.md`, jobsheet station yang diperbarui, `final_bank.py`, serta bank soal interaktif yang lebih luas pada `final_responsi.py`.

### Audit dan Perbaikan Teknis
- Mengoreksi `KURIKULUM.md` menjadi peta P1–P16 lengkap dengan fokus, analisis, deliverable, batas anti-overlay, dan program penting.
- Menambahkan `parameter_sweep.py` P9 dan `decision_matrix.py` P11 yang sebelumnya disebut sebagai program wajib tetapi belum tersedia.
- Mengoreksi dataset baseline P5 agar efisiensi contoh tidak melebihi 100%.
- Memperbaiki pelaporan respons start P4: sekarang membedakan arus pada `t=0`, arus puncak model, kondisi akhir, dan batas sederhana `V/R`.
- Memperjelas output simulasi P7 agar urutan FWD, STOP, dan REV tidak menimbulkan salah tafsir.
- Memperbaiki `vfd_ramp.py` P11 agar titik akhir ramp tidak dicetak dua kali dan input dasar tervalidasi.
- Memperluas TugasVideo P10 dan menambahkan panduan lengkap TugasVideo P11.
- Menjaga P8/P12/P16 sebagai pertemuan Project/Responsi tanpa `TugasVideo.md`.
- Semua perubahan pada tahap ini diterapkan langsung ke branch `v1`; status final diverifikasi melalui GitHub Actions setelah commit terakhir.