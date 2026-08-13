# Menjalankan Program di Google Colab

Semua script Python dapat dipakai di Colab.

## Cara 1 — Upload script
1. Buka notebook Colab baru.
2. Upload file `.py` dan CSV modul yang diperlukan.
3. Jalankan, misalnya:
```python
%run trafo_no_load.py
```

## Cara 2 — Clone repository
```python
!git clone -b v1 https://github.com/rofiqcp/Praktikum-Mesin-Mesin-Listrik.git
%cd Praktikum-Mesin-Mesin-Listrik/Modul-09-Motor-Induksi-Rangkaian-Ekivalen-Torsi-Slip/program
%run induction_torque_speed.py
```

## Catatan
Matplotlib umumnya tersedia di Colab. Dataset CSV diletakkan satu folder dengan script agar path konsisten.