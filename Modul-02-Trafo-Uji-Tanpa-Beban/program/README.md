# Program P02 — Transformator Tanpa Beban

## File yang Dijalankan

### 1. Analisis Utama
```bash
python trafo_no_load.py
```

Script ini menjalankan:
- sweep rasio tegangan ideal dan model sederhana;
- perhitungan `S0`, `PF0`, `Ic`, `Im`, `Rc`, dan `Xm`;
- beberapa dataset contoh;
- penyimpanan grafik `trafo_no_load_ratio.png` bila Matplotlib tersedia.

### 2. Sweep Ringkas
```bash
python trafo_no_load_sweep.py
```

Script kedua memakai fungsi dari program utama dan menampilkan tabel sweep dalam format yang mudah disalin ke spreadsheet.

## VS Code
Buka terminal pada folder modul atau folder `program/`, lalu jalankan script di atas.

## Google Colab
Upload kedua `.py`, kemudian:

```python
!python trafo_no_load.py
!python trafo_no_load_sweep.py
```

## Eksperimen Mahasiswa
1. ubah rasio transformasi model;
2. ubah beberapa nilai dataset contoh;
3. jalankan ulang;
4. bandingkan hasil sebelum dan sesudah perubahan;
5. validasi bahwa nilai faktor daya berada pada rentang yang masuk akal;
6. verifikasi minimal satu baris dengan hitungan manual.

## Output untuk Laporan
- tabel terminal;
- grafik;
- tabel hasil modifikasi;
- satu contoh hitung manual;
- interpretasi perubahan parameter.

Parameter di script adalah data/model pembelajaran dan harus diganti dengan dataset praktikum bila analisis menggunakan hasil sesi laboratorium.