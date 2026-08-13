# Modul 07 — Rangkaian Kendali Kontaktor: Latching, Forward–Reverse, Interlock, Timer, dan Star–Delta

**Mata Kuliah:** Praktikum Mesin-Mesin Listrik  
**Pertemuan:** 7 dari 16  
**Durasi:** 3 × 50 menit  
**Fokus:** logika kendali diskrit dan urutan kerja kontaktor melalui CADe SIMU serta state machine Python.

---

## 1. Batas Anti-Overlay

P6 membahas **motor induksi dan hubungan listrik dasarnya**: medan putar, slip, line–phase, star dan delta. P7 tidak mengulang fisika tersebut. P7 membahas **bagaimana logika kendali menjaga urutan dan kondisi aman**.

P7 mencakup:

- push button NO/NC;
- coil kontaktor;
- auxiliary contact;
- latching/seal-in;
- STOP dominant logic;
- overload contact sebagai input proteksi dalam logika;
- forward/reverse request;
- electrical interlock;
- state transition;
- timer star–delta;
- permissive dan fault state;
- truth table dan state machine.

P11 nanti membandingkan performa metode starting; P7 hanya berfokus pada **logika urutannya**.

---

## 2. Capaian Pembelajaran

Mahasiswa mampu:

1. membaca diagram kontrol berbasis kontak dan coil;
2. membedakan kontak NO dan NC secara fungsi logika;
3. menjelaskan latching/seal-in;
4. menjelaskan mengapa STOP dan proteksi harus dapat memutus state RUN;
5. membuat truth table forward–reverse;
6. menjelaskan electrical interlock;
7. merancang state machine star–delta;
8. memverifikasi bahwa dua state yang saling eksklusif tidak aktif bersamaan;
9. mensimulasikan logika menggunakan CADe SIMU;
10. memverifikasi logika yang sama menggunakan Python.

---

## 3. Elemen Dasar Logika Kontaktor

### Push button NO

Secara logika:

```text
released = 0
pressed  = 1
```

### Push button NC

Pada logika kontrol, kontak NC sering digunakan untuk kondisi STOP/permissive agar perubahan status dapat memutus jalur logika.

### Coil kontaktor

Coil diperlakukan sebagai output boolean:

```text
coil = 0 -> kontaktor tidak diperintah aktif
coil = 1 -> kontaktor diperintah aktif
```

Pada P7 kita fokus pada logika status tersebut, bukan konstruksi elektromekanik coil.

### Auxiliary contact

Kontak bantu adalah feedback status yang dipakai untuk:

- seal-in;
- interlock;
- indikator;
- permissive;
- sequencing.

---

## 4. Latching / Seal-In

Masalah dasar: tombol START hanya aktif selama ditekan. Agar sistem mempertahankan state RUN, digunakan state memory.

Secara boolean sederhana:

```text
RUN_next = STOP_OK AND PROTECTION_OK AND (START OR RUN_previous)
```

`RUN_previous` merepresentasikan efek auxiliary contact seal-in.

### STOP dominant

STOP harus mengalahkan START pada rancangan logika dasar:

```text
if STOP_OK == 0:
    RUN = 0
```

Walaupun START sedang bernilai 1, kondisi STOP membuat output RUN menjadi 0.

---

## 5. Truth Table Latching

Contoh penyederhanaan:

| STOP_OK | START | RUN_prev | RUN_next |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 |

Mahasiswa harus memahami bahwa latching adalah bentuk **memori satu bit**.

---

## 6. Forward–Reverse sebagai Mutual Exclusion

Dalam logika forward–reverse terdapat dua request:

```text
FWD_REQUEST
REV_REQUEST
```

Kedua output tidak boleh aktif bersamaan:

```text
NOT(FWD AND REV)
```

Ini disebut **mutual exclusion**.

### Electrical interlock sebagai boolean

Model sederhananya:

```text
FWD = FWD_REQUEST AND NOT REV
REV = REV_REQUEST AND NOT FWD
```

Dalam implementasi state machine yang lebih baik, request diproses terhadap state sebelumnya untuk mencegah kondisi ambigu.

---

## 7. State Machine Forward–Reverse

Definisikan state:

```text
STOPPED
FORWARD
REVERSE
FAULT
```

Transisi konseptual:

```text
STOPPED + request_forward -> FORWARD
STOPPED + request_reverse -> REVERSE
FORWARD + stop           -> STOPPED
REVERSE + stop           -> STOPPED
ANY + protection_trip    -> FAULT
FAULT + reset_valid      -> STOPPED
```

Untuk latihan P7, direct transition `FORWARD -> REVERSE` dapat dilarang sehingga mahasiswa harus melalui `STOPPED`. Ini membuat state machine mudah diaudit.

---

## 8. Truth Table Forward–Reverse

| Stop OK | FWD Req | REV Req | Output FWD | Output REV | Status |
|---:|---:|---:|---:|---:|---|
| 0 | X | X | 0 | 0 | stop |
| 1 | 0 | 0 | 0 | 0 | idle |
| 1 | 1 | 0 | 1 | 0 | forward |
| 1 | 0 | 1 | 0 | 1 | reverse |
| 1 | 1 | 1 | 0 | 0 | conflict rejected |

Kebijakan untuk request ganda harus eksplisit. Pada modul ini dipilih **reject both** agar mudah diverifikasi.

---

## 9. Overload/Fault sebagai Input Logika

P7 tidak membahas setting proteksi secara detail. Fokusnya adalah bagaimana status fault memengaruhi state machine:

```text
if fault:
    all_outputs = OFF
    state = FAULT
```

Setelah fault, reset tidak boleh sekadar mengaktifkan kembali output. Reset mengembalikan state ke kondisi siap/idle, kemudian request baru diproses.

---

## 10. Konsep Star–Delta dari Perspektif P7

P6 sudah menjelaskan hubungan star/delta. P7 hanya memodelkan tiga output logika:

```text
MAIN
STAR
DELTA
```

Invariant wajib:

```text
NOT(STAR AND DELTA)
```

Urutan state konseptual:

```text
IDLE
  -> STAR_RUN
  -> TRANSITION
  -> DELTA_RUN
  -> IDLE
```

Saat fault:

```text
ANY_STATE -> FAULT
```

---

## 11. Mengapa Ada State TRANSITION?

Jika perpindahan dimodelkan langsung dari STAR ke DELTA dalam satu langkah, sulit menunjukkan bahwa output STAR sudah benar-benar OFF sebelum DELTA diperbolehkan ON.

Dengan state terpisah:

```text
STAR_RUN:
    MAIN=1, STAR=1, DELTA=0

TRANSITION:
    MAIN=1, STAR=0, DELTA=0

DELTA_RUN:
    MAIN=1, STAR=0, DELTA=1
```

State transition membuat invariant lebih mudah diuji.

---

## 12. Timer sebagai Event Generator

Timer tidak dianggap sebagai proteksi tunggal. Dalam state machine, timer menghasilkan event:

```text
star_time_elapsed
transition_time_elapsed
```

Contoh:

```text
if state == STAR_RUN and star_time_elapsed:
    state = TRANSITION

if state == TRANSITION and transition_time_elapsed:
    state = DELTA_RUN
```

Fokus mahasiswa adalah urutan event dan state, bukan nilai timer spesifik per motor.

---

## 13. Permissive

Permissive adalah syarat yang harus TRUE sebelum suatu state diizinkan.

Contoh abstrak:

```text
START_ALLOWED = stop_ok AND protection_ok AND no_conflict
```

Dengan pendekatan ini diagram kontrol menjadi lebih mudah dianalisis karena syarat dapat dikelompokkan.

---

## 14. Interlock vs Permissive vs Latching

| Konsep | Fungsi |
|---|---|
| latching | mempertahankan state setelah input momentary dilepas |
| interlock | mencegah dua state yang tidak boleh bersamaan |
| permissive | syarat agar transisi/output diizinkan |
| timer | menghasilkan event berbasis waktu |
| fault latch | mempertahankan status fault sampai reset |

Mahasiswa harus dapat membedakan kelimanya.

---

## 15. CADe SIMU sebagai Simulator Logika

CADe SIMU digunakan untuk membangun diagram kontrol virtual. Minimal tiga simulasi:

1. latching;
2. forward–reverse dengan mutual exclusion;
3. star–delta dengan state transisi.

Dokumen `program/CADE_SIMU_RANGKAIAN.md` berisi checklist simulasi dan skenario uji.

Tujuan simulasi bukan meniru semua fenomena elektromagnetik motor, tetapi memverifikasi **logika diskrit**.

---

## 16. Test Case Wajib

### Latching

- START sekali -> state RUN;
- START dilepas -> RUN tetap;
- STOP -> RUN hilang;
- fault -> RUN hilang.

### Forward–Reverse

- FWD request -> hanya FWD;
- REV request -> hanya REV;
- request ganda -> tidak ada output aktif;
- fault -> semua output OFF.

### Star–Delta

- start -> STAR state;
- timer event -> TRANSITION;
- transition event -> DELTA state;
- pada semua waktu `STAR AND DELTA == False`;
- stop/fault -> IDLE/FAULT dengan output OFF.

---

## 17. State Transition Table

Contoh format:

| Current State | Input/Event | Next State | MAIN | STAR | DELTA |
|---|---|---|---:|---:|---:|
| IDLE | start valid | STAR_RUN | 1 | 1 | 0 |
| STAR_RUN | star timer | TRANSITION | 1 | 0 | 0 |
| TRANSITION | transition timer | DELTA_RUN | 1 | 0 | 1 |
| DELTA_RUN | stop | IDLE | 0 | 0 | 0 |
| ANY | fault | FAULT | 0 | 0 | 0 |

Tabel ini harus dibuat sebelum menggambar simulator.

---

## 18. Program Python

Jalankan:

```bash
cd Modul-07-Kendali-Kontaktor-Latching-FR-StarDelta/program
python control_logic.py
```

Program bertindak sebagai **digital twin logika sederhana**: input event diproses menjadi state/output, kemudian invariant diperiksa.

Mahasiswa membandingkan hasil Python dengan CADe SIMU.

---

## 19. Invariant yang Harus Selalu Benar

Invariant adalah aturan yang tidak boleh dilanggar pada state mana pun.

```text
1. FWD dan REV tidak boleh sama-sama 1
2. STAR dan DELTA tidak boleh sama-sama 1
3. FAULT -> semua output 0
4. STOP condition -> output run 0
5. DELTA hanya boleh muncul setelah urutan state yang valid
```

Ini adalah inti audit logika P7.

---

## 20. Fault Injection di Simulasi

Fault injection berarti sengaja memberi kombinasi input tidak normal ke model software/simulator, misalnya:

- START dan STOP bersamaan;
- FWD dan REV bersamaan;
- fault muncul saat STAR state;
- timer event datang saat state tidak sesuai;
- reset diberikan saat fault condition masih aktif.

Mahasiswa mencatat apakah state machine merespons secara deterministik.

---

## 21. Troubleshooting Logika

Jika simulasi tidak sesuai, periksa berurutan:

1. nama input/output;
2. jenis kontak NO/NC pada model;
3. state awal;
4. seal-in;
5. interlock silang;
6. prioritas STOP/fault;
7. event timer;
8. invariant;
9. state transition table.

Jangan mengubah banyak hal sekaligus; satu perubahan satu pengujian.

---

## 22. Pertanyaan Analisis

1. Mengapa latching disebut memory satu bit?
2. Mengapa STOP sebaiknya dominant pada model dasar?
3. Apa beda interlock dan permissive?
4. Mengapa request FWD+REV perlu kebijakan eksplisit?
5. Mengapa timer tidak cukup dianggap sebagai interlock?
6. Apa keuntungan state TRANSITION pada star–delta?
7. Apa manfaat invariant dibanding sekadar melihat animasi?
8. Mengapa fault reset sebaiknya kembali ke IDLE, bukan langsung RUN?
9. Apa beda P6 dan P7 dalam pembahasan star–delta?
10. Bagaimana Python membantu memverifikasi CADe SIMU?

---

## 23. Hubungan ke Responsi P8

P8 akan menguji integrasi P1–P7. Dari P7, mahasiswa harus siap menjelaskan:

- satu truth table;
- satu state machine;
- satu invariant;
- satu fault scenario;
- perbedaan latching, interlock, permissive, dan timer.

---

## 24. Catatan Keselamatan Akademik

Seluruh langkah rinci di repository difokuskan pada **simulasi dan logika**. Implementasi hardware di laboratorium menggunakan trainer, diagram resmi, proteksi, dan SOP fasilitas di bawah supervisi instruktur. Diagram simulasi tidak boleh dianggap sebagai pengganti dokumentasi peralatan nyata.

---

## 25. Ringkasan

P7 mengubah rangkaian kontaktor dari sesuatu yang sekadar “digambar” menjadi sistem logika yang dapat diuji. Kunci utamanya adalah state, event, latching, permissive, interlock, timer, fault handling, dan invariant. Jika logika dapat dijelaskan dengan truth table dan state machine, simulasi CADe SIMU menjadi jauh lebih mudah diaudit.