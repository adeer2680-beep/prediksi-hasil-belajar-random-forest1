
---

# 2. `prd.md`

```markdown
# PRODUCT REQUIREMENTS DOCUMENT (PRD)

## Prediksi Kategori Hasil Belajar Siswa Menggunakan Algoritma Random Forest Berbasis Web

---

## 1. Informasi Produk

### Nama Produk

Sistem Prediksi Kategori Hasil Belajar Siswa

### Jenis Produk

Intelligent Web Application berbasis Machine Learning.

### Metode Machine Learning

Random Forest Classification.

### Target Pengguna

- Guru
- Admin sekolah
- Pihak sekolah yang membutuhkan informasi hasil belajar siswa

---

## 2. Latar Belakang

Hasil belajar siswa merupakan salah satu informasi penting dalam proses pendidikan. Data hasil belajar biasanya terdiri dari berbagai atribut seperti nilai tugas, nilai ujian, kehadiran, dan aktivitas pembelajaran.

Pengolahan data secara manual membutuhkan waktu dan dapat menyulitkan ketika jumlah siswa cukup banyak.

Machine Learning dapat digunakan untuk menemukan pola dari data historis siswa dan menghasilkan prediksi terhadap kategori hasil belajar.

Pada penelitian ini digunakan algoritma Random Forest untuk melakukan klasifikasi kategori hasil belajar siswa.

Sistem dikembangkan berbasis web agar proses input data dan penyajian hasil prediksi dapat dilakukan melalui sebuah aplikasi yang mudah digunakan.

---

## 3. Permasalahan

Permasalahan yang ingin diselesaikan:

1. Bagaimana melakukan klasifikasi kategori hasil belajar siswa berdasarkan data yang tersedia?
2. Bagaimana menerapkan algoritma Random Forest untuk memprediksi kategori hasil belajar?
3. Bagaimana menyediakan hasil prediksi melalui aplikasi berbasis web?
4. Bagaimana mengetahui performa algoritma Random Forest dalam melakukan klasifikasi?

---

## 4. Tujuan Produk

Produk bertujuan untuk:

1. Membantu proses klasifikasi hasil belajar siswa.
2. Menerapkan algoritma Random Forest.
3. Menyediakan sistem prediksi berbasis web.
4. Menampilkan hasil prediksi dengan mudah dipahami.
5. Memberikan informasi tambahan kepada guru atau pihak sekolah mengenai kategori hasil belajar siswa.

---

## 5. Target Pengguna

### Admin

Admin bertugas mengelola sistem dan data.

Hak akses:

- Login
- Mengelola data siswa
- Mengelola dataset
- Melakukan proses training
- Melihat hasil evaluasi model
- Melakukan prediksi
- Melihat riwayat prediksi

### Guru

Guru menggunakan sistem untuk memperoleh informasi hasil prediksi siswa.

Hak akses:

- Login
- Melihat data siswa
- Memasukkan data siswa
- Melakukan prediksi
- Melihat hasil prediksi

---

## 6. Fitur Utama

### 6.1 Login

Pengguna melakukan autentikasi sebelum menggunakan sistem.

Input:

- Username/email
- Password

Output:

- Dashboard sesuai hak akses pengguna.

---

### 6.2 Dashboard

Dashboard menampilkan informasi ringkas mengenai sistem.

Informasi yang dapat ditampilkan:

- Jumlah siswa
- Jumlah data
- Jumlah hasil prediksi
- Akurasi model
- Distribusi kategori hasil belajar

---

### 6.3 Data Siswa

Pengguna dapat mengelola data siswa.

Fungsi:

- Tambah data
- Edit data
- Hapus data
- Lihat data
- Cari data

---

### 6.4 Dataset

Admin dapat memasukkan dataset yang akan digunakan untuk proses Machine Learning.

Format dataset dapat berupa CSV.

Dataset terdiri dari:

- Fitur/input
- Label/kategori hasil belajar

---

### 6.5 Preprocessing

Sistem melakukan preprocessing terhadap dataset sebelum proses training.

Proses dapat meliputi:

- Pemeriksaan data kosong
- Pembersihan data
- Transformasi data
- Encoding data kategorikal
- Pemilihan atribut
- Pembagian dataset

---

### 6.6 Training Model

Sistem menggunakan dataset training untuk membangun model Random Forest.

Alur:

```text
Dataset
   ↓
Preprocessing
   ↓
Training Data
   ↓
Random Forest
   ↓
Model