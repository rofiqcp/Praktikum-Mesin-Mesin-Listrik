# Jobsheet 09 — Model Ekivalen dan Kurva Torsi–Slip

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
```
Ubah parameter `Rth, Xth, R2, X2, Vth, f, poles` sesuai data.

## Bagian D — Verifikasi Eksperimen
Jalankan motor pada kondisi aman yang ditetapkan laboratorium. Ukur rpm dan arus. Tentukan slip dan letakkan titik ukur pada kurva simulasi.

## Tabel
| Kondisi | rpm | slip | fr rotor | arus | torsi model |
|---|---:|---:|---:|---:|---:|
|Start/model|0|1||| 
|No-load|||||
|Load|||||

## Analisa
1. Mengapa slip tidak boleh nol jika motor menghasilkan torsi induksi?
2. Apa arti breakdown torque?
3. Bagaimana kenaikan `R2'` mengubah bentuk kurva?
4. Mengapa data locked-rotor harus mengikuti SOP khusus?