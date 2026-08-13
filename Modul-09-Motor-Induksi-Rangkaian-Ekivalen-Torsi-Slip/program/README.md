# Program P09

Jalankan dua program wajib:

```bash
python induction_torque_speed.py
python parameter_sweep.py
```

`induction_torque_speed.py` mencetak `Ns`, breakdown torque, rpm/slip pada titik maksimum, serta beberapa titik referensi slip. `parameter_sweep.py` membandingkan pengaruh perubahan tegangan model dan resistansi rotor terhadap starting torque, breakdown torque, slip breakdown, dan rpm breakdown.

## Eksperimen
Ubah satu parameter pada satu waktu dan tuliskan prediksi sebelum menjalankan program. Parameter yang dapat dipelajari antara lain `Vth`, `R2`, `f`, dan `poles`.

Untuk tiap perubahan catat:
- starting torque;
- breakdown torque;
- slip breakdown;
- rpm breakdown;
- arah perubahan dibanding baseline.

Gunakan `../Jobsheet-Lengkap.md` untuk tabel sweep dan analisis.

## Google Colab
Upload kedua file, lalu:

```python
!python induction_torque_speed.py
!python parameter_sweep.py
```

Nilai parameter pada script adalah contoh pendidikan. Jangan mencampur parameter dari dataset berbeda tanpa mencatat sumbernya.