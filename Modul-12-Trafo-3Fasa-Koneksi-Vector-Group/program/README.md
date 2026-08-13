# Program P12

## Program Utama
```bash
python three_phase_transformer.py
```

Program utama membandingkan besar line sisi 2 untuk empat keluarga koneksi berdasarkan `N1`, `N2`, dan nilai line referensi sisi 1. Program juga menampilkan contoh fasor tiga fasa.

## Parameter yang Dipelajari
- `N1` dan `N2` → rasio winding `a`;
- line reference;
- koneksi Y-Y, Delta-Delta, Delta-Y, Y-Delta;
- sudut fasor 0°, -120°, +120°.

## Eksperimen
1. Baseline `N1=1000`, `N2=200`.
2. Ubah `N2` menjadi 250.
3. Ubah nilai line referensi dan bandingkan semua koneksi.
4. Verifikasi manual faktor `sqrt(3)` pada koneksi campuran.
5. Gambar fasor dan cek selisih sudut 120°.

## VS Code
Buka terminal di folder program, lalu:
```bash
python three_phase_transformer.py
```

## Google Colab
Upload file lalu:
```python
!python three_phase_transformer.py
```

## Output untuk Project
Catat:
- rasio winding;
- hasil empat koneksi;
- satu contoh hitung manual;
- screenshot output;
- sketsa/plot fasor;
- penjelasan perbedaan rasio winding dan rasio line.