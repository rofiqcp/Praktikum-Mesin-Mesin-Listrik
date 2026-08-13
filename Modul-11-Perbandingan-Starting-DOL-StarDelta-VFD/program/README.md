# Program P11

## Script
- `starting_compare.py`: membandingkan profil arus relatif dan waktu mencapai kecepatan relatif.
- `vfd_ramp.py`: membuat tabel ramp frekuensi dan tegangan per-unit.

## Menjalankan
```bash
python starting_compare.py
python vfd_ramp.py
```

Atau dari root repository gunakan path folder P11.

## Eksperimen
1. Catat baseline setiap metode.
2. Ubah waktu transisi pada model pembanding dan catat perubahan profil.
3. Ubah ramp pada `vfd_ramp.py` menjadi 2 s, 5 s, dan 10 s.
4. Bandingkan peak current relatif dan waktu mencapai target.
5. Dokumentasikan setiap parameter yang diubah.

## Colab
Upload file `.py`, lalu:
```python
!python starting_compare.py
!python vfd_ramp.py
```

Nilai pada script adalah model pendidikan/per-unit untuk perbandingan konsep, bukan parameter commissioning peralatan nyata.