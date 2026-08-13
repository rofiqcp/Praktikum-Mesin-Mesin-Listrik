# Program P02 — Transformator Tanpa Beban

## Program Utama
```bash
python trafo_no_load.py
```

Satu script ini menjalankan dua kelompok analisis:

1. **sweep rasio tegangan**: membandingkan nilai ideal dengan model sederhana;
2. **parameter tanpa beban**: menghitung `S0`, `PF0`, `Ic`, `Im`, `Rc`, dan `Xm` dari beberapa dataset contoh.

Script juga menyimpan grafik `trafo_no_load_ratio.png` bila Matplotlib tersedia.

## VS Code
Buka terminal pada folder ini dan jalankan perintah di atas.

## Google Colab
Upload `trafo_no_load.py`, lalu:

```python
!python trafo_no_load.py
```

## Eksperimen Mahasiswa
- ubah rasio transformasi contoh;
- ubah tiga dataset `V0, I0, P0`;
- pastikan faktor daya tetap pada rentang valid;
- bandingkan satu hasil program dengan hitungan manual;
- jelaskan variabel mana yang paling berubah.

## Output yang Disimpan
Screenshot terminal, grafik, tabel hasil modifikasi, dan interpretasi singkat.