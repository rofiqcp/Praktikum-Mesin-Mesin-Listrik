# Modul 13 — Motor Induksi 1 Fasa: Winding Utama, Winding Bantu, Kapasitor, Starting, dan Karakteristik

**Pertemuan:** 13 dari 16  
**Durasi:** 3 × 50 menit  
**Prasyarat:** medan magnet, daya AC, kecepatan sinkron, slip, dan pembacaan nameplate.  
**Fokus:** memahami karakteristik khusus motor induksi satu fasa, terutama pembentukan torsi awal, fungsi winding bantu, peran kapasitor, arah putaran secara konseptual, serta analisis arus–rpm–beban.

> P6 dan P9–P11 membahas motor induksi tiga fasa. P13 tidak mengulang starter tiga fasa. P13 fokus pada fenomena yang khas pada motor induksi **satu fasa**.

## 1. Capaian Pembelajaran
Mahasiswa mampu:
1. membedakan prinsip dasar motor induksi satu fasa dan tiga fasa;
2. menjelaskan mengapa kondisi diam pada motor satu fasa ideal tidak menghasilkan starting torque bersih yang memadai;
3. menjelaskan konsep double-revolving-field secara kualitatif;
4. membedakan winding utama dan winding bantu;
5. menjelaskan fungsi phase shift dalam pembentukan torsi awal;
6. menghitung reaktansi kapasitif `Xc`;
7. membedakan split-phase, capacitor-start, permanent split capacitor (PSC), dan capacitor-start capacitor-run;
8. menghitung `Ns`, slip, daya masuk, daya mekanik, dan efisiensi dari dataset yang cukup;
9. membaca hubungan arus, rpm, beban, faktor daya, dan temperatur;
10. menghubungkan teori dengan data trainer atau dataset tanpa menganggap satu diagram berlaku untuk semua motor.

## 2. Medan Pulsasi dan Torsi Awal
Sumber satu fasa menghasilkan medan stator yang secara sederhana dapat dipandang sebagai medan pulsasi. Dalam pendekatan double-revolving-field, medan ini dapat diuraikan menjadi dua medan berputar dengan besar yang sama tetapi arah berlawanan.

Pada kondisi rotor diam:

```text
T_forward ≈ T_backward
T_start_net ≈ 0
```

Karena itu diperlukan mekanisme yang membuat kondisi awal tidak simetris. Salah satu cara yang umum adalah menambahkan winding bantu yang mempunyai karakteristik impedansi berbeda dari winding utama, sering kali bersama kapasitor.

Setelah rotor mulai bergerak, slip terhadap medan forward dan backward tidak lagi sama sehingga torsi bersih menjadi dominan ke salah satu arah.

## 3. Winding Utama dan Winding Bantu
Motor satu fasa umumnya mempunyai:
- **main winding / winding utama**, sebagai winding utama operasi;
- **auxiliary winding / winding bantu**, ditempatkan berbeda secara ruang dan dirancang agar arusnya mempunyai beda fasa terhadap arus winding utama.

Secara konseptual:

```text
I_main = magnitude_main ∠phi_main
I_aux  = magnitude_aux  ∠phi_aux
phase displacement = phi_aux - phi_main
```

Winding bantu tidak sekadar "menambah arus". Perannya adalah membantu membentuk kondisi medan yang menghasilkan starting torque.

## 4. Reaktansi Kapasitif
Untuk kapasitor ideal:

```text
Xc = 1 / (2 pi f C)
```

Dengan:
- `Xc` dalam ohm;
- `f` dalam hertz;
- `C` dalam farad.

Contoh pada 50 Hz dan `C = 20 uF`:

```text
Xc ≈ 159.15 ohm
```

Jika `C` meningkat pada frekuensi tetap, `Xc` menurun. Namun nilai kapasitor yang lebih besar **tidak otomatis lebih baik**. Nilai aktual pada motor nyata bergantung pada desain winding, duty, tegangan kerja, karakteristik starting, temperatur, dan spesifikasi pabrikan.

P13 menggunakan sweep nilai kapasitor untuk memahami tren matematis. Hasil sweep bukan rekomendasi penggantian komponen motor nyata.

## 5. Jenis Motor 1 Fasa
### Split-phase
Winding bantu dibuat berbeda impedansinya terhadap winding utama sehingga terbentuk beda fasa arus saat starting.

### Capacitor-start
Kapasitor membantu meningkatkan beda fasa pada saat starting. Pada desain tertentu, bagian start tidak digunakan terus-menerus.

### Permanent Split Capacitor (PSC)
Kapasitor run merupakan bagian dari kondisi operasi normal sesuai desain motor.

### Capacitor-start Capacitor-run
Menggunakan fungsi kapasitor start dan run yang berbeda untuk memperoleh karakteristik starting dan running yang sesuai desain.

Mahasiswa perlu memahami **fungsi**, bukan hanya menghafal nama jenisnya.

## 6. Kecepatan Sinkron dan Slip
Rumus kecepatan sinkron tetap:

```text
Ns = 120 f / P
```

Slip:

```text
s = (Ns - Nr) / Ns
```

Contoh motor 4 kutub, 50 Hz, `Nr = 1425 rpm`:

```text
Ns = 1500 rpm
s  = 5%
```

Ketika kebutuhan torsi beban meningkat, rpm umumnya sedikit turun sehingga slip meningkat.

## 7. Arah Putaran
Arah putaran ditentukan oleh arah medan resultan saat starting. Pada motor yang memang dirancang reversible, perubahan hubungan relatif antara winding utama dan winding bantu dapat mengubah arah torsi awal.

Dalam praktikum, analisis arah menggunakan diagram resmi trainer atau data yang diberikan pengajar. Fokusnya adalah memahami hubungan **winding utama + winding bantu → medan resultan → arah**, bukan menebak terminal motor yang tidak terdokumentasi.

## 8. Daya dan Efisiensi
Jika dataset satu fasa memberikan `V`, `I`, dan `PF`:

```text
Pin = V I PF
```

Daya mekanik:

```text
omega = 2 pi n / 60
Pout  = T omega
```

Efisiensi:

```text
eta = Pout / Pin × 100%
```

Jika sensor torsi atau daya aktif tidak tersedia, jangan mengisi nilai `Pout` dan efisiensi dengan angka perkiraan tanpa dasar. Gunakan hanya besaran yang memang dapat dihitung dari data yang tersedia.

## 9. Karakteristik terhadap Beban
Kecenderungan yang umum terlihat pada dataset:
- arus meningkat ketika kebutuhan torsi meningkat;
- rpm turun sedikit;
- slip meningkat;
- faktor daya dapat membaik dari beban sangat ringan ke beban menengah;
- temperatur dapat meningkat seiring rugi dan waktu operasi.

Kecenderungan tersebut tidak selalu linear dan tidak boleh digeneralisasi tanpa melihat data motor yang dianalisis.

## 10. Starting Current dan Running Current
Starting adalah fenomena transien. Running current adalah kondisi setelah motor mendekati steady-state.

Karena itu, angka peak starting current tidak boleh dibandingkan langsung dengan arus RMS steady-state tanpa menjelaskan metode pengukurannya.

## 11. Data Minimum Praktikum

| Variabel | Satuan | Keterangan |
|---|---|---|
| load_pct | % | tingkat beban relatif |
| V | V | tegangan terminal |
| I | A | arus |
| PF | - | faktor daya bila tersedia |
| rpm | rpm | kecepatan rotor |
| torque | N.m | bila tersedia |
| temp | degC | bila tersedia |
| C | uF | nilai kapasitor pada data/desain trainer |

## 12. Program Wajib
Jalankan:

```bash
python Modul-13-Motor-Induksi-1Fasa-Kapasitor/program/single_phase_capacitor.py
python Modul-13-Motor-Induksi-1Fasa-Kapasitor/program/single_phase_performance.py
```

Program pertama menganalisis `Xc` terhadap `C` dan frekuensi. Program kedua membaca dataset contoh, menghitung `Ns`, slip, daya, efisiensi, dan quality check.

## 13. Eksperimen Numerik
Mahasiswa melakukan minimal:
1. sweep `C = 5–40 uF` pada 50 Hz;
2. membandingkan `Xc` pada 50 Hz dan 60 Hz;
3. menghitung `Ns` untuk beberapa jumlah kutub;
4. membandingkan slip pada beberapa rpm;
5. menganalisis hubungan beban–arus–rpm;
6. mengidentifikasi titik efisiensi terbaik jika data lengkap.

Tuliskan prediksi sebelum menjalankan program, lalu bandingkan dengan hasilnya.

## 14. Validasi Data
Tandai data jika:
- `C <= 0` atau `f <= 0`;
- `PF` di luar 0–1;
- rpm berada di luar konteks operasi yang dijelaskan;
- `Pout > Pin` pada dataset baseline normal;
- efisiensi >100% tanpa penjelasan ketidakpastian;
- satuan tidak konsisten.

Data yang ditandai tidak otomatis dihapus. Periksa dulu kemungkinan salah satuan, salah input, atau keterbatasan pengukuran.

## 15. Kesalahan Konsep yang Sering Terjadi
- menganggap medan satu fasa sama dengan rotating field tiga fasa;
- menganggap semakin besar kapasitor selalu semakin baik;
- menyamakan fungsi kapasitor start dan run;
- menganggap semua motor satu fasa mempunyai konstruksi internal identik;
- menghitung `Pout = T × rpm` tanpa konversi ke rad/s;
- menyebut slip hanya sebagai selisih rpm;
- menyimpulkan arah hanya dari warna kabel tanpa diagram yang valid.

## 16. Pertanyaan Analisis
1. Mengapa motor satu fasa membutuhkan mekanisme starting tambahan?
2. Apa fungsi winding bantu?
3. Mengapa kapasitor dapat membantu membentuk beda fasa?
4. Apa hubungan `C` dan `Xc`?
5. Mengapa hasil sweep kapasitor tidak otomatis menjadi rekomendasi komponen?
6. Apa perbedaan capacitor-start dan PSC?
7. Bagaimana kenaikan beban memengaruhi rpm dan slip?
8. Data apa yang diperlukan untuk menghitung efisiensi?
9. Mengapa starting current dan running current harus dibedakan konteksnya?
10. Apa batas fokus P13 dibanding P6 dan P9?

## 17. Hubungan ke P14
P13 menutup blok motor induksi dengan kasus satu fasa. P14 berpindah ke **mesin sinkron**, yang bekerja pada hubungan langsung antara kecepatan rotor, jumlah kutub, dan frekuensi, serta mempunyai eksitasi medan sebagai variabel penting.

## 18. Catatan Praktikum
Penggunaan trainer mengikuti SOP laboratorium dan dokumentasi peralatan yang digunakan. Model dan program pada repository dipakai untuk analisis akademik; data aktual selalu mengikuti nameplate dan konfigurasi trainer yang tersedia.

## 19. Ringkasan
P13 menghubungkan medan pulsasi, winding bantu, phase shift, kapasitor, slip, dan performa motor satu fasa. Mahasiswa diharapkan mampu menjelaskan **mengapa motor dapat start, variabel apa yang perlu diamati, bagaimana data diperiksa kewajarannya, dan bagaimana tren arus–rpm–slip dianalisis**.