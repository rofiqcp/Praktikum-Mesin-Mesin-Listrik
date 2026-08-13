# Jobsheet 07 — CADe SIMU dan Hardware Rangkaian Kendali

## Tahap 1 — Simulasi CADe SIMU
### A. Latching
`L -> STOP(NC) -> OLR(NC) -> [START(NO) || K1_aux(NO)] -> K1 coil -> N`

### B. Forward–Reverse
Rancang K1 FWD dan K2 REV dengan interlock NC silang. Simulasikan kondisi START FWD, STOP, START REV, dan tekan kedua START hampir bersamaan.

### C. Star–Delta
Gunakan Kmain, Kstar, Kdelta, timer. Verifikasi tidak ada state `Kstar=1` dan `Kdelta=1`.

## Tahap 2 — Hardware Kontrol
Mulai dari tegangan kontrol rendah bila tersedia. Dosen/laboran memverifikasi continuity sebelum sumber daya motor diaktifkan.

## Tahap 3 — Uji Fault
- STOP ditekan,
- overload contact dibuka secara simulasi/test,
- interlock diuji,
- power control diputus dan kembali: rangkaian tidak boleh auto-start bila SOP mensyaratkan no-voltage release.

## Program Verifikasi
```bash
python program/control_logic.py
```

## Checklist Kelulusan
- [ ] Latching lepas saat STOP/OLR.
- [ ] FWD dan REV tidak pernah ON bersamaan.
- [ ] STAR dan DELTA tidak pernah ON bersamaan.
- [ ] Timer menghasilkan transisi STAR→DELTA.
- [ ] Semua terminal diberi label.

## Analisa
Gambar ladder final, jelaskan setiap interlock, dan tulis failure mode jika satu kontak NC interlock dibypass.