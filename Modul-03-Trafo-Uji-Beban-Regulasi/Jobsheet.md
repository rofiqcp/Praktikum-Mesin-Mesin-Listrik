# Jobsheet P03 — Analisis Transformator Berbeban

**Durasi:** 3 × 50 menit

> Jobsheet ini berfokus pada pengolahan dataset berbeban yang diperoleh dari trainer sesuai SOP laboratorium. Tidak ada prosedur perubahan rangkaian daya di dalam dokumen ini.

## 1. Tujuan
Mahasiswa mampu menghitung regulasi, daya keluaran, rugi, efisiensi, menganalisis pengaruh faktor daya, dan membuat grafik karakteristik berbeban.

## 2. Pra-Lab
1. Jelaskan perbedaan fokus P2 dan P3.
2. Jelaskan `Zeq = Req + jXeq`.
3. Jelaskan mengapa rugi tembaga mengikuti `I²R`.
4. Jelaskan arti regulasi tegangan.
5. Jelaskan mengapa efisiensi dapat mempunyai titik maksimum.

## 3. Dataset Dasar
Gunakan dataset yang diberikan instruktur atau `program/data_trafo.csv`.

| load_pct | V1 | I1 | Pin | V2 | I2 | pf | Pout | reg | eta | loss |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |

## 4. Perhitungan Manual
Untuk minimal dua titik data hitung:

```text
Pout = V2 I2 pf
VR = (V2_noload - V2_load)/V2_load × 100%
eta = Pout/Pin × 100%
Ploss = Pin - Pout
```

| Besaran | Titik A | Titik B |
|---|---:|---:|
| Pout | | |
| VR | | |
| eta | | |
| Ploss | | |

## 5. Analisis Python
Jalankan dari folder `program/`:

```bash
python trafo_regulasi.py
```

Program membaca `data_trafo.csv` dan menghasilkan besaran turunan serta grafik.

Bandingkan hasil manual dan Python:

| Besaran | Manual | Python | Error % | Penjelasan |
|---|---:|---:|---:|---|
| Pout | | | | |
| Regulasi | | | | |
| Efisiensi | | | | |
| Rugi | | | | |

## 6. Analisis Octave/MATLAB
Jalankan `trafo_load.m` bila lingkungan tersedia. Bandingkan grafiknya dengan hasil Python. Fokus pada konsistensi tren, bukan tampilan grafik.

## 7. Grafik Wajib
1. `V2` terhadap `I2`.
2. regulasi terhadap `load_pct`.
3. efisiensi terhadap `load_pct`.
4. rugi total terhadap `load_pct`.

Setiap grafik wajib mempunyai judul, label sumbu, satuan, dan keterangan sumber data.

## 8. Eksperimen Numerik Faktor Daya
Pilih satu titik `V2` dan `I2`, lalu hitung `Pout` untuk tiga faktor daya contoh: 1.0, 0.8, dan 0.6.

| PF | V2 | I2 | Pout |
|---:|---:|---:|---:|
| 1.0 | | | |
| 0.8 | | | |
| 0.6 | | | |

Jelaskan mengapa daya aktif berubah walaupun V dan I sama.

## 9. Pertanyaan Analisis
1. Mengapa V2 cenderung berubah ketika I2 meningkat?
2. Mengapa Pcu sensitif terhadap arus?
3. Apakah titik efisiensi tertinggi selalu berada pada 100% beban?
4. Apa pengaruh PF terhadap Pout?
5. Apa perbedaan regulasi dan efisiensi?
6. Mengapa satu titik data tidak cukup untuk menyimpulkan karakteristik?
7. Jika efisiensi hasil hitung lebih dari 100%, bagian dataset mana yang harus diperiksa?
8. Mengapa model dan data nyata dapat berbeda?

## 10. Output Dikumpulkan
- pra-lab;
- dataset lengkap;
- dua contoh hitung manual;
- output Python;
- empat grafik;
- tabel variasi faktor daya;
- jawaban analisis;
- kesimpulan 200–300 kata.

## 11. Rubrik
| Komponen | Bobot |
|---|---:|
| Pra-lab | 10% |
| Validasi dataset | 15% |
| Perhitungan manual | 20% |
| Program Python/Octave | 20% |
| Grafik | 15% |
| Analisis | 15% |
| Kesimpulan | 5% |

## 12. Kriteria Siap P4
Mahasiswa mampu menjelaskan hubungan **beban → arus → jatuh tegangan/rugi → regulasi/efisiensi → grafik**.