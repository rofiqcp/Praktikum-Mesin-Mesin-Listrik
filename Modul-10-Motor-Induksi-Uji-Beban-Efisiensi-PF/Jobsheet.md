# Jobsheet 10 — Load Test Motor Induksi

## Persiapan
Verifikasi coupling, guard, grounding, overload setting sesuai SOP, dan area shaft bebas.

## Uji
Ambil 5–6 titik dari no-load sampai beban aman yang ditentukan laboratorium.

| Load | VL | IA | IB | IC | Pin | PF | rpm | T | Pout | slip | eta |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
||||||||||||

## Program
Edit `program/data_induction_load.csv` lalu:
```bash
python program/induction_load_analysis.py
```

## Grafik Wajib
1. arus vs load,
2. rpm/slip vs load,
3. PF vs load,
4. efficiency vs load.

## Analisa
- Bandingkan tren dengan kurva P9.
- Cari titik efisiensi terbaik dari data.
- Jelaskan penyebab PF no-load rendah.
- Evaluasi unbalance arus tiga fasa.

## Catatan
Jika torsi/power analyzer tidak tersedia, gunakan dataset instruktur untuk bagian efisiensi, tetapi tetap lakukan pengukuran V/I/rpm pada trainer.