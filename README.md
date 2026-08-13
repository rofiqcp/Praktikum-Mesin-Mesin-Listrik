# Praktikum Mesin-Mesin Listrik — Branch `v1`

Repositori 16 pertemuan praktikum Mesin-Mesin Listrik dengan pola `Materi.md`, `Jobsheet.md`, tugas video/project, serta program analisis yang dapat dijalankan.

## Struktur Semester

| P | Modul | Fokus utama | Deliverable |
|---|---|---|---|
| 01 | Orientasi & Peta Mesin Listrik | brainstorming, software, hardware, pengukuran | TugasVideo |
| 02 | Trafo Uji Tanpa Beban | rasio, polaritas, I0 | TugasVideo |
| 03 | Trafo Uji Beban | regulasi, efisiensi, rangkaian ekivalen | TugasVideo |
| 04 | Motor DC Dasar | back-EMF, starting, arah putaran | TugasVideo |
| 05 | Motor DC Karakteristik | speed-torque, beban, PWM, efisiensi | TugasVideo |
| 06 | Motor Induksi 3 Fasa Dasar | Ns, slip, star/delta, arah | TugasVideo |
| 07 | Kendali Kontaktor | latching, F/R, star-delta, interlock | TugasVideo |
| 08 | Responsi 1 | tanya jawab dan integrasi kompetensi P1–P7 | **Project/Responsi** |
| 09 | Motor Induksi Model | equivalent circuit, torque-slip | TugasVideo |
| 10 | Motor Induksi Load Test | PF, slip, efisiensi | TugasVideo |
| 11 | Starting Comparison | DOL vs star-delta vs VFD | TugasVideo |
| 12 | Trafo 3 Fasa | Y/Delta, line-phase, vector group | **Project** |
| 13 | Motor 1 Fasa | winding bantu, kapasitor | TugasVideo |
| 14 | Mesin Sinkron | rpm-frequency, OCC, V-curve | TugasVideo |
| 15 | Integrasi & Diagnosis | CSV, Python, Node.js, reasoning berbasis data | TugasVideo |
| 16 | Responsi Akhir | integrasi teori, perhitungan, simulasi, dan data | **Project/Responsi** |

## Prinsip Anti-Overlay
- P2 = trafo tanpa beban; P3 = trafo berbeban/parameter.
- P4 = dasar dinamik dan arah putaran motor DC; P5 = karakteristik steady-state/efisiensi.
- P6 = fisika/koneksi motor induksi; P7 = logika kendali; P9–P11 = model, performa beban, dan evaluasi starting.
- P12 = trafo tiga fasa, bukan pengulangan trafo satu fasa.
- P13 = motor induksi satu fasa dan peran kapasitor.
- P14 = mesin sinkron, OCC, eksitasi, dan V-curve.
- P15 = integrasi/diagnosis berbasis data, bukan jenis mesin baru.
- P8 dan P16 adalah responsi integratif dan tidak menambah teori utama baru.

## Software
- **CADe SIMU**: gambar/simulasi rangkaian kontaktor, latching, forward–reverse, star–delta.
- **Python 3**: model dan analisis data; dapat dijalankan di VS Code maupun Google Colab.
- **GNU Octave/MATLAB**: beberapa contoh alternatif pada P3 dan P5.
- **Node.js**: pipeline laporan data pada P1 dan P15.
- **OpenModelica (opsional)**: pengayaan model dinamik.
- **Scratch**: aktivitas blok konseptual tersedia pada `scratch/README.md` untuk P1.

## Quick Start dan Validasi
```bash
python -m pip install -r requirements.txt
python tools/check_structure.py
python tools/check_readiness.py
python tools/verify_python.py
python tools/run_noninteractive.py
```

Node.js:
```bash
node Modul-01-Orientasi-Peta-Mesin-Listrik/program/peta_mesin.js
node Modul-15-Integrasi-Uji-Diagnostik-Analisis-Data/program/report.js Modul-15-Integrasi-Uji-Diagnostik-Analisis-Data/program/lab_data.csv
```

`check_structure.py` memastikan 16 modul dan file wajib tersedia. `check_readiness.py` memeriksa penanda draft, heading bahasa yang tidak konsisten, serta referensi lokal ke program/dataset yang tidak ditemukan. GitHub Actions menjalankan pemeriksaan yang sama pada setiap push ke `v1`.

## Google Colab
Lihat `colab/README.md`. Script Python sengaja dibuat file `.py` biasa agar satu kode yang sama bisa dijalankan di VS Code, terminal, atau Colab tanpa membuat versi terpisah yang mudah tidak sinkron.

## Keselamatan Laboratorium
Praktik daya dilakukan hanya pada trainer dan fasilitas yang sesuai SOP laboratorium, dengan proteksi dan supervisi. Perubahan wiring dilakukan dalam keadaan sumber terisolasi/OFF. Diagram pada repo adalah bahan pendidikan; rating, terminal, proteksi, dan prosedur hardware harus mengikuti peralatan nyata yang digunakan.