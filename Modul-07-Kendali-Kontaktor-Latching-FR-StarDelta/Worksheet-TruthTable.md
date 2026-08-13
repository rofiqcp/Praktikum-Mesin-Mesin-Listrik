# Worksheet P07 — Truth Table, State, dan Invariant

## A. Latching

Lengkapi tabel berikut berdasarkan model pada `Materi.md`.

| STOP_OK | START | RUN_prev | RUN_next | Alasan |
|---:|---:|---:|---:|---|
|0|0|0|||
|0|1|0|||
|1|0|0|||
|1|1|0|||
|1|0|1|||

## B. Mutual Exclusion

Gunakan dua output virtual `A` dan `B`.

Invariant:

```text
NOT(A AND B)
```

| Req A | Req B | Expected A | Expected B | Pass/Fail |
|---:|---:|---:|---:|---|
|0|0||||
|1|0||||
|0|1||||
|1|1||||

## C. Sequential State

Gunakan urutan:

```text
IDLE -> A_RUN -> TRANSITION -> B_RUN -> IDLE
```

| Current State | Event | Next State | A | B |
|---|---|---|---:|---:|
|IDLE|start||||
|A_RUN|timer_a||||
|TRANSITION|timer_b||||
|B_RUN|stop||||

## D. Fault Injection

Buat minimal lima test case, termasuk dua conflict case.

| No | Current State | Input/Event | Expected | Actual | Pass/Fail |
|---:|---|---|---|---|---|
|1||||||
|2||||||
|3||||||
|4||||||
|5||||||

## E. Audit

- Apakah output eksklusif pernah aktif bersama?
- Apakah STOP mempunyai prioritas sesuai desain?
- Apakah event timer hanya mengubah state yang relevan?
- Apakah reset dari FAULT kembali ke kondisi idle?
- Apakah hasil simulator sama dengan `control_logic.py`?

## F. Kesimpulan

Tuliskan lima kesimpulan yang menyebut state, event, atau invariant secara eksplisit.