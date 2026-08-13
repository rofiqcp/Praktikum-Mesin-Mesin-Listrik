# Modul 03 — Transformator 1 Fasa: Uji Beban, Regulasi, Efisiensi, dan Rangkaian Ekivalen

## Batas Materi
P2 membahas tanpa beban dan rasio. P3 berfokus pada **perubahan ketika dibebani**, uji hubung-singkat terkontrol, rugi tembaga, regulasi, dan efisiensi.

## Konsep
Saat beban naik, arus sekunder meningkat, arus primer mengikuti, drop pada impedansi ekivalen bertambah, sehingga tegangan terminal sekunder turun.

### Regulasi Tegangan
`VR = (Vnl - Vfl)/Vfl × 100%`

### Efisiensi
`eta = Pout/Pin × 100%`
`Pout = V2 I2 pf_load`
Kerugian utama: rugi inti mendekati konstan dan rugi tembaga `I^2R` berubah dengan kuadrat arus.

### Uji Hubung-Singkat
Dilakukan hanya pada trainer/lab sesuai SOP dengan tegangan **rendah** yang dinaikkan sampai arus uji tercapai. Jangan pernah menghubung-singkat sekunder lalu menerapkan tegangan primer nominal.

Dari data `Vsc, Isc, Psc` dapat diperoleh `Zeq=Vsc/Isc`, `Req=Psc/Isc^2`, `Xeq=sqrt(Zeq^2-Req^2)`.

## Eksperimen
Gunakan beban resistif bertingkat. Untuk setiap titik, ukur V1, I1, Pin, V2, I2, Pout/atau faktor daya. Plot regulasi dan efisiensi terhadap persentase beban.

## Interpretasi
Efisiensi maksimum mendekati kondisi rugi tembaga = rugi inti. Regulasi yang kecil berarti tegangan sekunder lebih stabil.