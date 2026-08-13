# Jobsheet Lengkap P09 — Model Ekivalen dan Kurva Torsi–Slip

Dokumen ini melengkapi `Jobsheet.md` dengan latihan komputasi dan analisis data yang lebih rinci.

## 1. Parameter Model
Isi `f`, `P`, `Vth`, `Rth`, `Xth`, `R2'`, `X2'`, dan rpm referensi dari parameter contoh atau dataset pengajar.

## 2. Prediksi Awal
Hitung `Ns`, slip, dan `fr`. Prediksi pengaruh penurunan tegangan serta perubahan `R2'` terhadap kurva torsi.

## 3. Hitung Manual
Gunakan `s=1.0`, `0.10`, `0.05`, dan slip referensi. Untuk setiap titik hitung `Nr=(1-s)Ns`, `fr=sf`, `R2'/s`, serta torsi model Thevenin pada `Materi.md`.

## 4. Program Wajib
```bash
python Modul-09-Motor-Induksi-Rangkaian-Ekivalen-Torsi-Slip/program/induction_torque_speed.py
python Modul-09-Motor-Induksi-Rangkaian-Ekivalen-Torsi-Slip/program/parameter_sweep.py
```

Catat `Ns`, starting torque, breakdown torque, slip breakdown, rpm breakdown, dan torsi pada slip referensi.

## 5. Sweep Tegangan
Bandingkan `Vth` sebesar 100%, 90%, dan 80% baseline. Buat tabel `V/Vbase`, `Tstart`, `Tmax`, dan `Tmax/Tmax_base`, lalu uji kecenderungan `T ∝ V²`.

## 6. Sweep Resistansi Rotor
Bandingkan `R2'` sebesar 0.5×, 1×, 1.5×, dan 2× baseline. Catat `Tstart`, `Tmax`, slip puncak, dan rpm puncak.

## 7. Aliran Daya
Untuk contoh `P_ag=1000 W`, hitung `P_rotor_cu=s P_ag` dan `P_conv=(1-s)P_ag` pada slip 1.00, 0.10, 0.04, dan 0.01.

## 8. Variasi Frekuensi/Kutub
Bandingkan 50 Hz–4 kutub, 60 Hz–4 kutub, dan 50 Hz–6 kutub. Fokuskan analisis pada perubahan `Ns` dan sumbu rpm.

## 9. Analisis Dataset
Jika diberikan rpm/torsi/arus, tambahkan kolom slip dan `fr`, urutkan berdasarkan slip, tandai outlier, lalu bandingkan tren data dengan kurva model.

## 10. Pertanyaan
1. Mengapa torsi induksi memerlukan slip?
2. Apa arti `R2'/s`?
3. Mengapa `fr` kecil dekat rpm nominal?
4. Mengapa tegangan berpengaruh kuat pada torsi?
5. Apa beda rated torque dan breakdown torque?
6. Mengapa `R2'` menggeser slip puncak?
7. Mengapa model steady-state berbeda dari transien starting?
8. Sebutkan empat asumsi model.

## 11. Deliverable
- tabel hitung manual;
- output dua script;
- grafik `T-rpm` dan `T-slip`;
- tabel sweep tegangan dan `R2'`;
- analisis maksimum 2 halaman;
- jawaban pertanyaan.

## 12. Rubrik
Perhitungan 20%, program 20%, grafik/sweep 25%, interpretasi 25%, kerapian 10%.