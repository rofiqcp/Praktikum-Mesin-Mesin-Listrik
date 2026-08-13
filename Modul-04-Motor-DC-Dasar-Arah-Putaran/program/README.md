# Program P04 — Motor DC Dasar

## 1. Respons Start + Sweep Internal

```bash
python motor_dc_start.py
```

Program utama mempunyai dua bagian:

1. **respons start dinamik** menggunakan model listrik-mekanik sederhana;
2. **sweep steady-state** untuk beberapa kombinasi tegangan dan arus.

Besaran yang dihitung antara lain:
- arus jangkar;
- back-EMF;
- rpm model;
- torsi model;
- daya masuk;
- daya konversi elektromekanik;
- rugi tembaga.

Jika Matplotlib tersedia, grafik disimpan sebagai:

`motor_dc_start_response.png`

## 2. Sweep Steady-State Ringkas

```bash
python motor_dc_sweep.py
```

Script ini mengimpor fungsi `steady_state()` dari program utama lalu menghasilkan tabel CSV-like yang mudah dipindahkan ke Excel/Colab.

## 3. Parameter Model

| Parameter | Arti |
|---|---|
| V | tegangan model |
| R | resistansi jangkar |
| L | induktansi jangkar |
| ke | konstanta back-EMF |
| kt | konstanta torsi |
| J | inersia |
| B | koefisien gesekan viskos |
| load_torque | contoh torsi beban |

## 4. Eksperimen Numerik

1. jalankan parameter default;
2. ubah hanya satu parameter;
3. jalankan ulang;
4. catat arus, rpm, back-EMF, dan torsi;
5. ulangi untuk parameter lain;
6. jelaskan hubungan sebab-akibatnya.

## 5. Google Colab

```python
!python motor_dc_start.py
!python motor_dc_sweep.py
```

## 6. Output Laporan

- output terminal dua script;
- grafik respons start;
- tabel minimal tiga skenario;
- perbandingan manual vs program;
- interpretasi parameter.

> Nilai parameter pada script adalah **model pembelajaran**, bukan rating universal motor. Untuk laporan eksperimen, gunakan parameter/dataset yang diberikan pada sesi praktikum.