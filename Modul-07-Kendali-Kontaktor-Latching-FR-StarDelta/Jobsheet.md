# Jobsheet 07 — Simulasi Kendali Kontaktor: Latching, Forward–Reverse, dan Star–Delta

**Pertemuan:** 7  
**Durasi:** 3 × 50 menit  
**Platform utama:** CADe SIMU + Python  
**Fokus:** verifikasi logika, bukan prosedur wiring daya.

---

## 1. Tujuan

Mahasiswa mampu:

1. menyusun truth table;
2. membuat state transition table;
3. mensimulasikan latching;
4. mensimulasikan forward–reverse dengan mutual exclusion;
5. mensimulasikan star–delta dengan state transisi;
6. melakukan fault injection;
7. memverifikasi invariant menggunakan Python;
8. membandingkan hasil CADe SIMU dengan state machine software.

---

## 2. File yang Harus Dihasilkan

Buat tiga file simulasi sendiri:

```text
P07_latching
P07_forward_reverse
P07_star_delta
```

Format file mengikuti versi CADe SIMU yang digunakan di laboratorium. Sertakan screenshot tiap state penting pada laporan.

---

## 3. Percobaan A — Latching

### State yang diamati

```text
IDLE
RUN
FAULT/STOP
```

### Truth table awal

| STOP_OK | START | RUN_prev | RUN_next |
|---:|---:|---:|---:|
|0|0|0|0|
|0|1|0|0|
|1|0|0|0|
|1|1|0|1|
|1|0|1|1|

### Skenario uji

1. initial state = IDLE;
2. beri event START;
3. lepaskan event START;
4. beri event STOP;
5. ulangi dengan fault input.

### Hasil

| Skenario | Expected | Actual | Pass/Fail |
|---|---|---|---|
| START | RUN | | |
| START release | RUN | | |
| STOP | IDLE | | |
| fault | output off | | |

---

## 4. Percobaan B — Forward–Reverse

Definisikan output virtual:

```text
FWD
REV
```

Invariant:

```text
NOT(FWD AND REV)
```

### Truth table

| Stop OK | FWD Req | REV Req | Expected FWD | Expected REV |
|---:|---:|---:|---:|---:|
|0|0|0|0|0|
|1|0|0|0|0|
|1|1|0|1|0|
|1|0|1|0|1|
|1|1|1|0|0|

### Test case

- forward request tunggal;
- reverse request tunggal;
- request ganda;
- stop saat forward;
- stop saat reverse;
- fault saat salah satu state aktif.

### Hasil

| Case | Expected State | Actual State | FWD | REV | Invariant Pass? |
|---|---|---|---:|---:|---|
|1||||||
|2||||||
|3||||||
|4||||||
|5||||||
|6||||||

---

## 5. Percobaan C — Star–Delta State Machine

Gunakan state:

```text
IDLE
STAR_RUN
TRANSITION
DELTA_RUN
FAULT
```

### State table

| Current | Event | Next | MAIN | STAR | DELTA |
|---|---|---|---:|---:|---:|
|IDLE|start valid|STAR_RUN|1|1|0|
|STAR_RUN|star timer|TRANSITION|1|0|0|
|TRANSITION|transition timer|DELTA_RUN|1|0|1|
|DELTA_RUN|stop|IDLE|0|0|0|
|ANY|fault|FAULT|0|0|0|

### Invariant

```text
STAR AND DELTA must always be False
```

### Test

Jalankan urutan normal dan catat state setiap event.

| Step | Event | State | MAIN | STAR | DELTA | Pass? |
|---:|---|---|---:|---:|---:|---|
|0|initial||||||
|1|start||||||
|2|timer-1||||||
|3|timer-2||||||
|4|stop||||||

---

## 6. Percobaan D — Fault Injection

Uji kombinasi input tidak normal pada **simulasi**:

| Fault/Test | Expected Response | Actual | Pass/Fail |
|---|---|---|---|
| START + STOP | STOP dominant | | |
| FWD + REV | reject conflict | | |
| fault saat FWD | outputs off | | |
| fault saat STAR | outputs off | | |
| timer event saat IDLE | tetap IDLE | | |
| reset tanpa kondisi valid | tetap aman | | |

Jelaskan mengapa hasil yang diharapkan dipilih demikian.

---

## 7. Percobaan E — Python State Machine

Jalankan:

```bash
cd Modul-07-Kendali-Kontaktor-Latching-FR-StarDelta/program
python control_logic.py
```

Catat state/output program. Bandingkan dengan CADe SIMU.

### Perbandingan

| Skenario | CADe SIMU | Python | Sama? | Catatan |
|---|---|---|---|---|
| latch start | | | | |
| latch stop | | | | |
| forward | | | | |
| reverse | | | | |
| conflict | | | | |
| star sequence | | | | |
| fault | | | | |

---

## 8. Audit Invariant

Checklist wajib:

- [ ] FWD dan REV tidak pernah aktif bersamaan;
- [ ] STAR dan DELTA tidak pernah aktif bersamaan;
- [ ] STOP dapat mengakhiri RUN;
- [ ] fault membuat output virtual OFF;
- [ ] DELTA tidak muncul dari IDLE tanpa urutan valid;
- [ ] reset fault kembali ke kondisi idle/ready, bukan langsung running.

---

## 9. Pertanyaan Analisis

1. Apa fungsi latching jika dilihat sebagai state memory?
2. Mengapa STOP dominant menyederhanakan perilaku sistem?
3. Apa beda electrical interlock dan state-machine interlock secara konsep?
4. Mengapa request FWD dan REV bersamaan perlu ditolak?
5. Apa fungsi state TRANSITION?
6. Mengapa `timer selesai` adalah event, bukan state?
7. Apa beda permissive dan interlock?
8. Apa keuntungan fault injection sebelum implementasi nyata?
9. Mengapa invariant penting untuk audit?
10. Bagaimana cara membuktikan bahwa simulasi CADe SIMU dan Python merepresentasikan logika yang sama?

---

## 10. Output Laporan

Wajib:

- tiga truth/state table;
- screenshot simulasi;
- hasil semua test case;
- output Python;
- tabel perbandingan simulator vs Python;
- daftar invariant;
- minimal tiga fault injection;
- jawaban analisis;
- kesimpulan 5–8 poin.

---

## 11. Rubrik

| Komponen | Bobot |
|---|---:|
| truth/state table | 15% |
| simulasi latching | 15% |
| simulasi F/R | 15% |
| simulasi star–delta | 15% |
| fault injection & invariant | 15% |
| Python | 10% |
| analisis | 10% |
| laporan | 5% |

---

## 12. Catatan

Seluruh langkah detail P7 dilakukan pada **simulator dan model software**. Implementasi pada trainer laboratorium mengikuti dokumentasi resmi alat, proteksi, dan SOP instruktur.