# Analisis Data P05

Dokumen ini melengkapi Materi.md dengan fokus pengolahan data simulasi dan dataset kelas.

## Langkah analisis

1. Buka `program/data_dc.csv`.
2. Periksa nama kolom dan satuan.
3. Hitung kecepatan sudut dari rpm dengan `omega = 2*pi*n/60`.
4. Hitung daya masuk `Pin = V*I`.
5. Jika torsi tersedia pada dataset, hitung `Pout = T*omega`.
6. Hitung efisiensi `eta = Pout/Pin*100%` bila semua besaran tersedia.
7. Buat grafik rpm terhadap beban, arus terhadap beban, daya terhadap beban, dan efisiensi terhadap beban.
8. Tandai data yang tidak konsisten untuk dibahas, bukan langsung dihapus.

## Pertanyaan

- Bagaimana perubahan rpm saat beban meningkat?
- Bagaimana perubahan arus?
- Pada titik mana efisiensi maksimum pada dataset?
- Apa perbedaan tren data dengan model ideal?
- Faktor apa yang dapat menjelaskan perbedaan tersebut?

## Output

Kumpulkan tabel hasil, grafik, satu contoh hitung manual, dan lima kesimpulan berbasis angka.