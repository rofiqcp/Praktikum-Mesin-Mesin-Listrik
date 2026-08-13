# Analisis Data P06 — Motor Induksi 3 Fasa

Dokumen ini melengkapi `Materi.md` dan memusatkan pekerjaan pada perhitungan, dataset, dan simulasi.

## 1. Kecepatan Sinkron

Gunakan:

```text
Ns = 120*f/P
```

Hitung untuk beberapa kombinasi frekuensi dan jumlah kutub. Buat tabel `f, P, Ns` dan jelaskan pengaruh masing-masing variabel.

## 2. Slip dan Frekuensi Rotor

Gunakan:

```text
s = (Ns-Nr)/Ns
fr = s*f
```

Buat minimal lima titik `Nr` untuk satu `Ns`, lalu analisis perubahan slip dan `fr`.

## 3. Star dan Delta

Bandingkan hubungan matematis:

```text
Star : Vph = VL/sqrt(3), IL = Iph
Delta: Vph = VL,         IL = sqrt(3)*Iph
```

Buat tabel beberapa nilai `VL` dan hitung `Vph` star serta delta.

## 4. Pendekatan Torsi

Gunakan hubungan konseptual `T proportional to V^2` untuk membandingkan rasio teoritis torsi pada tegangan fasa berbeda. Nyatakan bahwa ini model pendekatan, bukan model rangkaian ekivalen lengkap.

## 5. Grafik

Buat:

- `Ns vs P`;
- `slip vs Nr`;
- `Vph star vs delta`.

## 6. Pertanyaan

1. Mengapa Nr berbeda dari Ns?
2. Apa arti slip dalam persen?
3. Mengapa fr turun ketika Nr mendekati Ns?
4. Apa beda line dan phase?
5. Mengapa P6 berbeda dari P7?
6. Mengapa P6 belum membahas kurva torsi-slip lengkap?

## 7. Output

Kumpulkan tabel perhitungan, tiga grafik, output Python, dan minimal lima kesimpulan berbasis angka.