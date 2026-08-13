# Panduan Gambar CADe SIMU

## Latching
STOP NC → OLR NC → cabang START NO paralel K1 AUX NO → coil K1.

## Forward Reverse
- FWD rung: STOP NC → OLR NC → K2 AUX NC → (START_FWD || K1 AUX NO) → K1.
- REV rung: STOP NC → OLR NC → K1 AUX NC → (START_REV || K2 AUX NO) → K2.
- Power: K2 menukar dua fasa dibanding K1.

## Star Delta
- Kmain latch dari START.
- Kstar aktif selama timer belum selesai dan melalui Kdelta AUX NC.
- Kdelta aktif setelah timer selesai dan melalui Kstar AUX NC.
- Sisipkan dead time jika timer/perangkat mendukung.

Simpan screenshot dan file native CADe SIMU di folder kerja mahasiswa; format native dapat berbeda antar versi software.