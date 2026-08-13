# Jobsheet 06 — Analisis Motor Induksi 3 Fasa Dasar

Gunakan `Materi.md`, `Analisis-Data.md`, dan `Worksheet-Nameplate-Slip.md` sebagai satu paket praktikum P06.

## Tujuan

Mahasiswa mampu membaca nameplate, menghitung kecepatan sinkron, slip, frekuensi rotor, serta membedakan besaran line dan phase pada hubungan star/delta secara matematis.

## Bagian A — Nameplate

Salin parameter nameplate ke worksheet. Jelaskan arti setiap parameter, lalu tentukan kandidat jumlah kutub dari frekuensi dan rpm nominal.

## Bagian B — Kecepatan Sinkron

Gunakan:

```text
Ns = 120*f/P
```

Buat tabel untuk beberapa kombinasi `f` dan `P`, kemudian simpulkan pengaruh frekuensi dan jumlah kutub.

## Bagian C — Slip

Gunakan:

```text
s = (Ns-Nr)/Ns
fr = s*f
```

Hitung minimal lima titik `Nr` untuk satu nilai `Ns`. Buat grafik `slip vs Nr`.

## Bagian D — Line dan Phase

Bandingkan:

```text
Star : Vph = VL/sqrt(3), IL = Iph
Delta: Vph = VL,         IL = sqrt(3)*Iph
```

Buat minimal tiga contoh numerik dan jelaskan perbedaan line dengan phase.

## Bagian E — Python

Jalankan:

```bash
cd Modul-06-Motor-Induksi-3Fasa-Dasar-Star-Delta/program
python star_delta_calc.py
```

Bandingkan hasil program dengan hitungan manual. Ubah minimal dua parameter numerik untuk melihat perubahan hasil.

## Output Wajib

- tabel nameplate;
- tabel `Ns`;
- tabel slip dan `fr`;
- grafik `Ns vs jumlah kutub`;
- grafik `slip vs Nr`;
- tabel star/delta;
- output Python;
- jawaban analisis pada `Analisis-Data.md`;
- lima kesimpulan berbasis angka.

## Pertanyaan

1. Mengapa `Nr` berbeda dari `Ns`?
2. Apa makna slip secara fisik?
3. Mengapa `fr` berubah ketika `Nr` berubah?
4. Apa beda pole dengan pole pair?
5. Apa beda line voltage dan phase voltage?
6. Mengapa P6 berbeda dari P7?
7. Mengapa P6 belum membahas model rangkaian ekivalen P9?

## Rubrik

| Aspek | Bobot |
|---|---:|
| nameplate | 15% |
| Ns, slip, fr | 25% |
| line–phase | 20% |
| Python dan grafik | 20% |
| analisis | 15% |
| kesimpulan | 5% |
