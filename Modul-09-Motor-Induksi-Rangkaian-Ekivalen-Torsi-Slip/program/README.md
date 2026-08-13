# Program P09

Jalankan program utama:
```bash
python induction_torque_speed.py
```

Program mencetak `Ns`, breakdown torque, rpm/slip pada titik maksimum, serta beberapa titik referensi slip.

## Eksperimen
Ubah satu parameter pada satu waktu:
- `Vth`;
- `R2`;
- `f`;
- `poles`.

Untuk tiap perubahan catat:
- starting torque;
- breakdown torque;
- slip breakdown;
- rpm breakdown.

Gunakan `Jobsheet-Lengkap.md` untuk tabel sweep dan analisis.

## Colab
Upload file lalu:
```python
!python induction_torque_speed.py
```

Nilai parameter pada script adalah contoh pendidikan; jangan mencampur parameter dari dataset berbeda tanpa mencatat sumbernya.