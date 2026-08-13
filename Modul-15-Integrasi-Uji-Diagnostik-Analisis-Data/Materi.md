# Modul 15 — Integrasi Pengujian, Diagnostik, dan Analisis Data Mesin Listrik

## Tujuan
P15 tidak menambah jenis mesin baru. Pertemuan ini mengintegrasikan P2–P14 menjadi workflow engineering: `gejala → data → validasi → hipotesis → pengukuran tambahan → kesimpulan`.

## Mapping Gejala
- Tegangan sekunder trafo turun: periksa beban, input, regulasi, dan koneksi.
- Motor DC rpm turun: korelasikan V, I, beban, dan back-EMF.
- Motor induksi tiga fasa: bandingkan arus antar fasa, supply, rpm/slip, PF, dan beban.
- Motor 1 fasa: evaluasi data running dan komponen sesuai diagram trainer.
- Mesin sinkron: korelasikan rpm, frekuensi, eksitasi, dan tegangan.

## Prinsip Diagnosis
Jangan menyimpulkan fault dari satu angka. Gunakan baseline/nameplate, perbandingan antar kanal/fasa, dan tren terhadap beban/waktu.

## Data Pipeline
Format CSV standar:
`timestamp,machine,test,V,I,P,PF,rpm,torque,temp,note`

Python dipakai untuk derived metrics dan flag anomali. Node.js menghasilkan ringkasan JSON sehingga mahasiswa melihat bagaimana data laboratorium bisa diteruskan ke dashboard atau laporan otomatis.

## Error Pengukuran
Sumber error antara lain resolusi alat, koneksi sensor, perubahan supply, pembacaan operator, suhu, sampling, dan kesalahan satuan. Data mencurigakan harus diulang sebelum diagnosis final.

## Mini Audit Energi
Hitung `Pin`, `Pout`, `eta`, dan tentukan apakah operating point berada pada daerah yang masuk akal berdasarkan data sebelumnya. Rekomendasi tidak boleh mengubah proteksi atau parameter mesin di luar izin laboratorium.