# Program P04 — Motor DC Dasar

## Jalankan
```bash
python motor_dc_start.py
```

Script ini sekarang mempunyai **dua bagian**:

1. simulasi respons start dinamik menggunakan model listrik-mekanik sederhana;
2. sweep steady-state beberapa kombinasi tegangan dan arus untuk menghitung back-EMF, rpm model, torsi, daya masuk, daya konversi, dan rugi tembaga.

Jika Matplotlib tersedia, script menyimpan:

`motor_dc_start_response.png`

## Parameter yang Dapat Dipelajari
- `V`: tegangan model;
- `R`, `L`: parameter jangkar;
- `ke`: konstanta back-EMF;
- `kt`: konstanta torsi;
- `J`: inersia;
- `B`: gesekan viskos;
- `load_torque`: contoh torsi beban.

## Eksperimen Mahasiswa
1. jalankan parameter default;
2. ubah satu parameter saja;
3. jalankan ulang;
4. catat perubahan arus awal, rpm akhir, dan back-EMF;
5. ulangi untuk parameter kedua;
6. jelaskan hubungan sebab-akibatnya.

## Google Colab
```python
!python motor_dc_start.py
```

Gunakan parameter sebagai **model contoh**, bukan sebagai rating universal motor nyata.