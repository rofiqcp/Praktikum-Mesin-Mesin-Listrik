# Jobsheet 01 — Brainstorming Semua Materi dan Hubungannya

## Tujuan
1. Membuat peta konsep mesin listrik selama 16 pertemuan.
2. Mengenali terminal, nameplate, alat ukur, proteksi, dan software.
3. Menjalankan simulasi awal transformator, motor DC, motor induksi, latching, forward–reverse, dan star–delta tanpa masuk ke pengujian detail.

## Alat dan Bahan
Trainer transformator, motor DC tegangan rendah, motor induksi trainer, kontaktor/tombol/overload/timer, multimeter, clamp meter, tachometer, PC.

## Bagian A — Identifikasi Hardware
Buat tabel berisi: nama alat, rating, terminal, fungsi, risiko, alat ukur yang dipakai. Foto nameplate hanya jika diizinkan laboratorium.

## Bagian B — Simulasi CADe SIMU
Buat 4 rangkaian awal:
1. **Latching**: STOP NC, START NO, coil K1, kontak bantu K1 NO.
2. **Forward–Reverse**: K1/K2 dengan interlock listrik NC silang.
3. **Star–Delta**: main, star, delta, timer; star dan delta harus saling interlock.
4. **Motor 3 fasa DOL**: MCB/fuse → contactor → overload → motor.

Untuk trafo dan motor DC, gunakan program Python modul ini sebagai analisis konsep awal. Detail eksperimen baru dilakukan pada modul berikutnya.

## Bagian C — Hardware Demonstrasi
Dosen/laboran memperlihatkan terminal trafo, motor DC, dan motor induksi. Mahasiswa hanya melakukan continuity/identifikasi terminal saat sumber OFF.

## Bagian D — Pengukuran Awal
Dengan trainer yang aman, catat satu contoh pengukuran tiap kategori:
- tegangan AC,
- tegangan DC,
- arus beban,
- kecepatan rpm.

## Tabel Analisis
| Sistem | Input | Output | Besaran utama | Kontrol/Proteksi | Modul lanjutan |
|---|---|---|---|---|---|
| Trafo | AC | AC | V, I, P | Fuse/MCB | P2-P3, P12 |
| Motor DC | DC | Mekanik | V, I, rpm, T | Fuse/driver | P4-P5 |
| Motor induksi | 3φ AC | Mekanik | VL, IL, rpm, slip | Contactor/OLR | P6-P11 |
| Mesin sinkron | AC/DC exc. | Listrik/mekanik | f, V, I, rpm | Proteksi | P14 |

## Pertanyaan Analisa
1. Mengapa latching memakai kontak bantu?
2. Apa risiko jika K-forward dan K-reverse aktif bersamaan?
3. Mengapa pengukuran tegangan dilakukan paralel dan arus seri/clamp?
4. Hubungkan formula `Ns=120f/P` dengan kebutuhan pengukuran rpm.

## Deliverable
- 1 peta konsep A3/digital.
- Screenshot 4 rangkaian CADe SIMU.
- Hasil `python program/peta_mesin.py`.
- Kesimpulan maksimal 1 halaman.