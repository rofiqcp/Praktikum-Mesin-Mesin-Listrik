# Jobsheet 09 — Model Ekivalen dan Kurva Torsi–Slip

Gunakan juga `Jobsheet-Lengkap.md` sebagai panduan analisis yang lebih rinci.

## Bagian A — Data Motor
Catat `VL, f, pole, rpm nameplate, arus nominal`. Gunakan parameter ekivalen yang disediakan pengajar atau contoh program.

## Bagian B — Perhitungan Manual
Untuk tiga slip `s=1`, `0.1`, dan slip nominal:
1. hitung `Nr=(1-s)Ns`,
2. hitung `fr=s f`,
3. hitung torsi dengan model Thevenin sederhana.

## Bagian C — Program Python
```bash
python program/induction_torque_speed.py
python program/parameter_sweep.py
```
Program pertama digunakan untuk kurva dasar. Program kedua digunakan untuk membandingkan pengaruh parameter model.

## Bagian D — Verifikasi Data
Gunakan dataset atau data trainer yang disediakan laboratorium. Tentukan slip dari rpm dan letakkan titik data pada kurva simulasi.

## Tabel
| Kondisi | rpm | slip | fr rotor | arus | torsi model |
|---|---:|---:|---:|---:|---:|
|Start/model|0|1|||
|No-load|||||
|Load|||||

## Analisis
1. Mengapa slip tidak boleh nol jika motor menghasilkan torsi induksi?
2. Apa arti breakdown torque?
3. Bagaimana kenaikan `R2'` mengubah bentuk kurva?
4. Apa keterbatasan model ketika dibandingkan dengan data mesin nyata?