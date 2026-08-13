# Jobsheet 03 — Uji Beban dan Regulasi Transformator

## Tujuan
Mengukur penurunan V2, menghitung regulasi dan efisiensi, serta membangun parameter ekivalen dari data uji.

## Percobaan A — Beban Bertingkat
Set beban 0%, 25%, 50%, 75%, 100% rating trainer.

| Beban | V1 | I1 | Pin | V2 | I2 | Pout | Regulasi | Efisiensi |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|0%|||||||||
|25%|||||||||

## Percobaan B — Uji SC Terkontrol
Hanya jika fasilitas laboratorium memang memiliki prosedur uji SC. Gunakan sumber rendah/variac dan pembatas/proteksi. Catat `Vsc, Isc, Psc`, lalu matikan sumber sebelum melepas kabel.

## Analisis Python
Isi data contoh/hasil ukur pada `program/data_trafo.csv`, lalu:
```bash
python program/trafo_regulasi.py
```

## Pertanyaan
1. Mengapa V2 turun ketika beban naik?
2. Mengapa rugi tembaga tumbuh `I^2`?
3. Apakah titik efisiensi maksimum terjadi pada beban penuh?
4. Bandingkan nilai Zeq hasil uji dengan regulasi yang terjadi.

## Kriteria Berhasil
Semua titik data masuk akal, tidak ada rating yang terlampaui, dan mahasiswa dapat menjelaskan selisih antara teori ideal dengan hasil nyata.