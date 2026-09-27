# Prediksi Kategori Hasil Belajar Siswa Menggunakan Algoritma Random Forest Berbasis Web

## Deskripsi

Penelitian ini mengembangkan sebuah aplikasi web yang digunakan untuk memprediksi kategori hasil belajar siswa menggunakan algoritma Machine Learning, yaitu Random Forest.

Sistem menerima data yang berkaitan dengan hasil belajar siswa, kemudian melakukan proses prediksi untuk menentukan kategori hasil belajar siswa. Hasil prediksi dapat digunakan sebagai informasi tambahan bagi pihak sekolah atau guru dalam mengetahui kondisi hasil belajar siswa.

Aplikasi dikembangkan dalam bentuk web sehingga dapat diakses dengan lebih mudah oleh pengguna.

## Dokumen

Dokumen perancangan sistem:

- hld.md : High-Level Design sistem
- lld-awal.md : Low-Level Design awal sistem
- prompt-log.md : Dokumentasi penggunaan prompt AI dalam proses perancangan

## Latar Belakang

Hasil belajar siswa merupakan salah satu indikator yang dapat digunakan untuk mengetahui tingkat pencapaian siswa dalam proses pembelajaran. Dalam praktiknya, proses identifikasi dan pengelompokan hasil belajar siswa masih dapat dilakukan secara manual berdasarkan nilai yang diperoleh.

Penggunaan Machine Learning dapat membantu melakukan prediksi berdasarkan data historis siswa. Salah satu algoritma yang dapat digunakan adalah Random Forest karena mampu menangani data dengan beberapa atribut dan menghasilkan klasifikasi berdasarkan pola dari data yang digunakan sebagai data pelatihan.

Oleh karena itu, penelitian ini berfokus pada pengembangan aplikasi web untuk memprediksi kategori hasil belajar siswa menggunakan algoritma Random Forest.

## Tujuan

Tujuan penelitian ini adalah:

1. Mengembangkan aplikasi web untuk melakukan prediksi kategori hasil belajar siswa.
2. Menerapkan algoritma Random Forest dalam proses klasifikasi hasil belajar siswa.
3. Mengetahui hasil prediksi kategori hasil belajar berdasarkan data siswa.
4. Menyediakan sistem yang dapat membantu guru atau pihak sekolah dalam memperoleh informasi mengenai kategori hasil belajar siswa.

## Fitur Sistem

Fitur utama yang direncanakan dalam aplikasi:

- Login pengguna
- Dashboard
- Pengelolaan data siswa
- Input data hasil belajar siswa
- Import data siswa
- Proses preprocessing data
- Pelatihan model Random Forest
- Prediksi kategori hasil belajar
- Tampilan hasil prediksi
- Riwayat prediksi
- Evaluasi model
- Logout

## Metode

Algoritma yang digunakan dalam penelitian ini adalah:

**Random Forest**

Random Forest merupakan algoritma Machine Learning berbasis ensemble yang menggunakan beberapa decision tree untuk menghasilkan keputusan klasifikasi.

Alur proses secara umum:

1. Mengumpulkan dataset siswa.
2. Melakukan preprocessing data.
3. Membagi dataset menjadi data training dan testing.
4. Melatih model Random Forest menggunakan data training.
5. Melakukan prediksi menggunakan data testing.
6. Melakukan evaluasi model.
7. Menggunakan model untuk melakukan prediksi pada data siswa baru.
8. Menampilkan hasil prediksi melalui aplikasi web.

## Input Sistem

Data yang digunakan meliputi beberapa atribut yang relevan terhadap hasil belajar siswa, seperti:

- Nilai tugas
- Nilai ujian
- Nilai kehadiran
- Nilai aktivitas pembelajaran
- Nilai lainnya yang tersedia pada dataset

Atribut akhir akan disesuaikan dengan dataset yang digunakan dalam penelitian.

## Output Sistem

Output utama sistem adalah kategori hasil belajar siswa.

Contoh kategori:

- Rendah
- Sedang
- Tinggi

Kategori tersebut dapat disesuaikan berdasarkan dataset dan rancangan penelitian.

## Teknologi

Teknologi yang digunakan dalam pengembangan sistem:

- Frontend:
  - HTML
  - CSS
  - JavaScript

- Backend:
  - Python
  - Flask

- Machine Learning:
  - Python
  - Scikit-learn
  - Random Forest Classifier

- Database:
  - MySQL

## Struktur Repository

```text
prediksi-hasil-belajar-random-forest/
│
├── README.md
├── prd.md
├── srs.md
│
├── docs/
│   ├── requirements/
│   │   ├── prompt-log.md
│   │   └── user-stories.md
│   │
│   └── design/
│       ├── hld.md
│       ├── lld-awal.md
│       └── prompt-log.md
│
├── dataset/
│   └── dataset-siswa.csv
│
├── model/
│   └── random-forest-model.pkl
│
├── backend/
│   ├── app.py
│   ├── routes/
│   └── models/
│
└── frontend/
    ├── index.html
    ├── css/
    └── js/