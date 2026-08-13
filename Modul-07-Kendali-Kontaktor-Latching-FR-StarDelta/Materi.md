# Modul 07 — Rangkaian Kendali Kontaktor: Latching, Forward–Reverse, dan Star–Delta

## Batas Materi
P6 sudah menjelaskan hubungan fisik star/delta dan arah fasa. P7 khusus **logika kendali industri**: coil, kontak bantu, seal-in, interlock, overload, timer, dan urutan transisi.

## 1. Latching / Seal-In
STOP NC dan overload NC berada seri dengan coil. START NO memberi pulsa awal. Kontak bantu NO dari kontaktor diparalel dengan START untuk mempertahankan coil setelah tombol dilepas.

## 2. Forward–Reverse
Dua kontaktor mengubah urutan dua fasa. Wajib ada:
- electrical interlock: kontak NC K-FWD seri dengan coil K-REV dan sebaliknya;
- mechanical interlock bila hardware mendukung;
- stop/dead time sebelum reversal untuk aplikasi tertentu.

## 3. Star–Delta Otomatis
Urutan umum: MAIN + STAR aktif → timer → STAR OFF → jeda → DELTA ON. Kontak NC silang STAR/DELTA mencegah keduanya aktif bersamaan. Jangan menganggap timer saja sebagai interlock.

## 4. Overload
Kontak NC overload ditempatkan di rangkaian kontrol sehingga trip melepaskan coil. Reset penyebab overload sebelum restart.

## 5. Simulasi CADe SIMU
Mahasiswa membuat tiga file simulasi sendiri: `latching`, `forward_reverse`, `star_delta`. README menyediakan daftar terminal/logika untuk dibandingkan.

## 6. State Machine
Program Python modul ini menguji logika interlock secara deterministik sebelum hardware.