# Program P03 — Regulasi dan Efisiensi Transformator

## File
- `data_trafo.csv`: dataset contoh berbeban;
- `trafo_regulasi.py`: analisis Python;
- `trafo_load.m`: contoh analisis GNU Octave/MATLAB.

## Python
```bash
python trafo_regulasi.py
```

Program membaca CSV dan menghitung:
- daya keluaran;
- regulasi;
- efisiensi;
- rugi total;
- indikator rugi tembaga relatif;
- titik efisiensi tertinggi pada dataset.

Grafik disimpan sebagai `trafo_regulasi_efisiensi.png`.

## Octave/MATLAB
Buka folder program lalu jalankan:

```text
trafo_load
```

## Tugas Modifikasi
1. duplikasi dataset contoh;
2. ubah minimal dua titik beban secara konsisten;
3. jalankan Python;
4. bandingkan grafik sebelum dan sesudah perubahan;
5. jelaskan dampak perubahan V2, I2, dan faktor daya terhadap hasil.

Jangan mengubah kolom secara acak tanpa menjaga konsistensi fisik dataset.