# Materi Lengkap 16 — Responsi Akhir

P16 tidak menambah teori baru. Dokumen ini menjadi peta review P1–P15.

## Kompetensi Akhir
Mahasiswa harus mampu:
1. membaca nameplate dan satuan;
2. membedakan raw data, derived data, model, dan asumsi;
3. menghitung rasio, regulasi, dan efisiensi transformator;
4. menghitung back-EMF, arus, torsi, daya, dan efisiensi motor DC;
5. menghitung `Ns`, slip, frekuensi rotor, daya tiga fasa, dan efisiensi motor induksi;
6. menjelaskan latching, interlock, permissive, timer, dan state machine;
7. membandingkan DOL, star–delta, dan VFD;
8. membedakan line dan phase quantity serta membaca vector-group dasar;
9. menjelaskan motor satu fasa, bagian bantu, dan fungsi kapasitor;
10. menghitung hubungan rpm–frekuensi mesin sinkron serta membaca OCC dan V-curve;
11. melakukan quality check dataset;
12. membuat minimal dua hipotesis dan kesimpulan berbasis bukti.

## Peta Review
- P1: peta mesin, daya, instrumen, software, satuan.
- P2–P3: transformator 1 fasa.
- P4–P5: motor DC.
- P6–P7: motor induksi dasar dan logika kendali.
- P8: responsi tengah.
- P9–P11: model, load performance, dan starting motor induksi.
- P12: transformator 3 fasa dan vector group.
- P13: motor 1 fasa.
- P14: mesin sinkron.
- P15: integrasi analisis data.

## Kesalahan yang Harus Dapat Dideteksi
- rpm digunakan langsung pada `P=T omega`;
- line dan phase quantity tertukar;
- PF tidak masuk akal;
- efisiensi baseline di atas 100%;
- `Ns` disamakan dengan rpm aktual motor induksi;
- slip disamakan dengan sudut beban;
- satu outlier langsung dianggap kesimpulan akhir;
- data kosong diubah menjadi nol tanpa alasan;
- kesimpulan tidak menyebut bukti atau asumsi.

## Format Responsi
Tanya jawab individual, perhitungan singkat, interpretasi grafik, pembacaan diagram/state table, analisis dataset, demonstrasi program, dan project integrasi.

## Kriteria Jawaban Baik
Jawaban harus menyebut rumus yang tepat, definisi variabel, satuan, arti fisik hasil, asumsi, serta keterbatasan data bila ada.

Gunakan `Formula-Ringkas.md`, `Jobsheet-Lengkap.md`, `program/final_bank.py`, dan `program/final_responsi.py` untuk latihan.