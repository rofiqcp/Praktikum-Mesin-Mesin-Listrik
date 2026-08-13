# Kurikulum Praktikum Mesin-Mesin Listrik

Kurikulum terdiri dari 16 pertemuan yang disusun berjenjang. Setiap pertemuan mempunyai fokus yang berbeda agar teori, simulasi, pengolahan data, dan analisis tidak berulang tanpa tujuan.

| P | Fokus Utama | Analisis Utama | Deliverable |
|---:|---|---|---|
| 1 | Orientasi dan peta mesin listrik | energi, daya, nameplate, alat ukur, software | TugasVideo |
| 2 | Transformator tanpa beban | rasio, I0, PF0, Rc, Xm, rugi inti | TugasVideo |
| 3 | Transformator berbeban | regulasi, rugi, daya, efisiensi | TugasVideo |
| 4 | Motor DC dasar | back-EMF, arus, torsi, respons awal, arah | TugasVideo |
| 5 | Motor DC berbeban | speed–torque, arus, daya, rugi, efisiensi, PWM model | TugasVideo |
| 6 | Motor induksi 3 fasa dasar | medan putar, Ns, slip, line/phase, star/delta | TugasVideo |
| 7 | Logika kontaktor | latching, F/R, interlock, permissive, timer, state | TugasVideo |
| 8 | Responsi 1 | integrasi P1–P7 | Project |
| 9 | Model motor induksi | rangkaian ekivalen, R2'/s, torsi–slip, parameter sweep | TugasVideo |
| 10 | Uji beban motor induksi | I, PF, rpm, slip, Pin, Pout, eta | TugasVideo |
| 11 | Perbandingan starting | DOL, star–delta, VFD, V/f, ramp, decision matrix | TugasVideo |
| 12 | Transformator 3 fasa | Y/Delta, line/phase, fasor, vector group, clock notation | Project |
| 13 | Motor induksi 1 fasa | medan pulsasi, bagian bantu, Xc, slip, performa | TugasVideo |
| 14 | Mesin sinkron | rpm–frequency, eksitasi, OCC, V-curve, daya | TugasVideo |
| 15 | Integrasi data | baseline, quality check, hipotesis, analisis lintas mesin | TugasVideo |
| 16 | Responsi akhir | integrasi P1–P15, perhitungan, data, program, reasoning | Project |

## Batas Anti-Overlay
- P2 fokus kondisi tanpa beban; P3 fokus kondisi berbeban.
- P4 fokus prinsip dasar dan respons motor DC; P5 fokus karakteristik steady-state berbeban.
- P6 fokus fisika dan hubungan listrik motor induksi; P7 fokus logika kendali.
- P9 fokus model elektromagnetik; P10 fokus data performa steady-state; P11 fokus evaluasi metode starting.
- P12 membahas transformator tiga fasa dan fasor, bukan pengulangan transformator satu fasa.
- P13 membahas karakteristik khusus motor satu fasa.
- P14 membahas mesin sinkron dan eksitasi.
- P15 tidak menambah jenis mesin baru; fokusnya integrasi analisis data.
- P8 dan P16 adalah responsi, bukan pertemuan teori baru.

## Program dan Dokumen Pendalaman
Beberapa pertemuan mempunyai dokumen tambahan seperti `Jobsheet-Lengkap.md`, `Materi-Lengkap.md`, worksheet, bank soal, atau pendalaman. Dokumen tersebut merupakan bagian dari modul dan digunakan bersama `Materi.md`/`Jobsheet.md`, bukan sebagai materi terpisah.

Program penting yang telah ditambahkan antara lain:
- P9: `parameter_sweep.py`;
- P10: `induction_load_analysis.py`, `load_sweep_summary.py`;
- P11: `starting_compare.py`, `vfd_ramp.py`, `decision_matrix.py`;
- P12: `three_phase_transformer.py`, `vector_group_analysis.py`;
- P13: `single_phase_capacitor.py`, `single_phase_performance.py`;
- P14: `synchronous_machine.py`, `synchronous_analysis.py`;
- P15: `analyze_lab_csv.py`, `multi_machine_diagnostics.py`, `report.js`;
- P16: `final_bank.py`, `final_responsi.py`.

## Prinsip Pelaksanaan
Setiap analisis mengikuti urutan umum:

```text
teori -> prediksi -> data/model -> program -> perhitungan -> grafik -> quality check -> kesimpulan
```

Untuk data laboratorium, mahasiswa harus membedakan hasil ukur, hasil hitung, parameter model, dan asumsi. Penggunaan trainer mengikuti SOP fasilitas dan dokumentasi peralatan yang digunakan.