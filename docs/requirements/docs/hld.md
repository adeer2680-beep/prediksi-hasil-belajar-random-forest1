# High-Level Design (HLD)
# Sistem Prediksi Kategori Hasil Belajar Siswa Menggunakan Algoritma Random Forest Berbasis Web

## 1. Deskripsi Sistem

Sistem Prediksi Kategori Hasil Belajar Siswa merupakan aplikasi berbasis web yang digunakan untuk melakukan prediksi kategori hasil belajar siswa menggunakan algoritma Machine Learning Random Forest.

Sistem menerima data yang berkaitan dengan hasil belajar siswa, seperti nilai tugas, nilai ujian, nilai kehadiran, dan atribut pendukung lainnya. Data tersebut kemudian diproses melalui tahap preprocessing sebelum digunakan oleh model Random Forest untuk menghasilkan prediksi kategori hasil belajar.

Hasil prediksi yang diperoleh sistem dapat digunakan sebagai informasi tambahan bagi guru atau pihak sekolah dalam mengetahui kondisi hasil belajar siswa.

Aplikasi dirancang dalam bentuk web agar dapat digunakan dengan mudah melalui browser.

---

# 2. Arsitektur Sistem

Sistem menggunakan arsitektur client-server yang terdiri dari beberapa komponen utama:

## 2.1 Frontend

Frontend merupakan bagian yang berinteraksi langsung dengan pengguna.

Fungsi frontend:
- Menampilkan halaman aplikasi.
- Menyediakan form input data siswa.
- Menampilkan hasil prediksi.
- Menampilkan informasi data dan riwayat prediksi.

Teknologi:
- HTML
- CSS
- JavaScript


## 2.2 Backend

Backend bertugas mengatur proses utama aplikasi dan menjadi penghubung antara frontend, database, dan model machine learning.

Fungsi backend:
- Mengelola request dari pengguna.
- Melakukan validasi data.
- Menghubungkan aplikasi dengan database.
- Menjalankan proses prediksi.
- Mengirimkan hasil prediksi ke frontend.

Teknologi:
- Python
- Flask


## 2.3 Machine Learning Model

Komponen machine learning digunakan untuk melakukan klasifikasi kategori hasil belajar siswa.

Proses yang dilakukan:
1. Mengambil dataset siswa.
2. Melakukan preprocessing data.
3. Melakukan training model.
4. Menyimpan model Random Forest.
5. Melakukan prediksi terhadap data baru.

Teknologi:
- Python
- Scikit-learn
- Random Forest Classifier


## 2.4 Database

Database digunakan untuk menyimpan data yang dibutuhkan sistem.

Data yang disimpan:
- Data pengguna.
- Data siswa.
- Dataset pelatihan.
- Riwayat hasil prediksi.

Teknologi:
- MySQL

---

# 3. Diagram Arsitektur Sistem

```text
+-------------+
|    User     |
+-------------+
       |
       v
+----------------------+
|      Frontend        |
| HTML CSS JavaScript  |
+----------------------+
       |
       v
+----------------------+
|       Backend        |
|    Python Flask      |
+----------------------+
       |
       |
 +-----+-------------+
 |                   |
 v                   v

+------------+   +----------------+
|  MySQL     |   | Random Forest  |
| Database   |   | Model          |
+------------+   +----------------+

       |
       v

+----------------+
| Hasil Prediksi |
+----------------+