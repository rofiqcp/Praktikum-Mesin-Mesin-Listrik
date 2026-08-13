# Jobsheet 05 — Karakteristik dan Efisiensi Motor DC

## Percobaan A — Beban Bertingkat
Atur motor pada tegangan nominal trainer. Ambil data no-load sampai beban aman maksimum dalam 5–6 titik.

| Beban | V | I | rpm | T (Nm) | Pin | Pout | eta |
|---|---:|---:|---:|---:|---:|---:|---:|
||||||||

## Percobaan B — Duty PWM
Pada satu beban ringan yang aman, uji duty 20%, 40%, 60%, 80%, 100%. Catat rpm dan arus.

## Program
Edit `program/data_dc.csv`, lalu:
```bash
python program/dc_characteristic.py
```

## Analisa
1. Apakah torsi berbanding lurus dengan arus?
2. Mengapa rpm turun ketika torsi naik?
3. Pada titik mana efisiensi tertinggi?
4. Bandingkan kontrol tegangan/PWM dengan perubahan beban.
5. Jelaskan perbedaan data hasil ukur dan model ideal.

## Deliverable
CSV hasil ukur, tiga grafik utama, perhitungan efisiensi, dan kesimpulan 5 butir.