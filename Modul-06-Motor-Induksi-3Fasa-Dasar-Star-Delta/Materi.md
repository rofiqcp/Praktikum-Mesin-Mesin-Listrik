# Modul 06 — Motor Induksi 3 Fasa: Medan Putar, Slip, Star/Delta, dan Arah Putaran

## Batas Materi
P6 membahas **fisik motor dan hubungan terminal**. P7 membahas logika kontaktor/ladder. P9-P11 membahas model ekivalen, beban, efisiensi, dan perbandingan metode starting.

## Kecepatan Sinkron
`Ns = 120 f / P`. Rotor motor induksi saat berbeban berputar pada `Nr < Ns`. Slip `s=(Ns-Nr)/Ns` diperlukan agar ada induksi pada rotor.

## Hubungan Star dan Delta
Untuk sistem seimbang:
- Star: `VL = sqrt(3) Vph`, `IL = Iph`.
- Delta: `VL = Vph`, `IL = sqrt(3) Iph`.

Pemilihan hubungan harus mengikuti **nameplate motor dan tegangan jaringan/trainer**. Star–delta starter hanya cocok jika motor memang dirancang run-delta pada tegangan suplai tersebut.

## Arah Putaran
Menukar dua dari tiga fasa membalik urutan fasa dan arah medan putar. Lakukan perubahan hanya saat sumber OFF.

## DOL
DOL menghubungkan motor langsung melalui contactor dan overload. P6 memakai DOL sederhana untuk memahami terminal dan arah, tanpa menyusun logic forward–reverse otomatis.

## Pengukuran
Ukur VL, IL tiap fasa bila memungkinkan, rpm, dan hitung Ns/slip. Ketidakseimbangan arus perlu dicatat dan dianalisis.