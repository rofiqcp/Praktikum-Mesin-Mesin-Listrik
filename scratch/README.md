# Scratch Activity — Peta Mesin Listrik (P1)

Scratch dipakai hanya sebagai **aktivitas visual konsep**, bukan untuk mensimulasikan rangkaian daya.

## Project: `MesinListrik-Concept-Map`
Buat 4 sprite: `Trafo`, `MotorDC`, `MotorInduksi`, `MesinSinkron`.

Variabel global: `f`, `pole`, `rpm`, `slip`.

### Blok Motor Induksi
- ketika sprite diklik,
- set `f=50`, `pole=4`, `rpm=1440`,
- set `Ns = 120*f/pole`,
- set `slip = (Ns-rpm)/Ns*100`,
- katakan nilai Ns dan slip.

### Blok Transformator
- set `V1=220`, `N1=1000`, `N2=100`,
- set `V2=V1*N2/N1`,
- katakan rasio dan V2.

### Target
Mahasiswa merekam project Scratch berjalan dan menjelaskan mengapa Scratch hanya dipakai untuk pemahaman alur/rumus, sedangkan analisis numerik semester memakai Python/Octave.