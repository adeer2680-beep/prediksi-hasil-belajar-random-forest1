# API Contract

## Sistem Prediksi Kategori Hasil Belajar Siswa Menggunakan Random Forest


## 1. Overview

API digunakan sebagai penghubung antara frontend, backend, database, dan model Machine Learning pada sistem prediksi kategori hasil belajar siswa.


## 2. Format Request dan Response

Semua komunikasi API menggunakan format JSON.

Contoh response berhasil:

```json
{
  "status": "success",
  "message": "Data berhasil diproses",
  "data": {}
}

## 3. Authentication

Sistem menggunakan autentikasi untuk membatasi akses pengguna berdasarkan hak akses.

Endpoint login:

POST /api/auth/login

Pengguna yang dapat mengakses sistem:
- Admin
- Guru


## 4. HTTP Method

| Method | Fungsi |
|---|---|
| GET | Mengambil data |
| POST | Membuat data atau menjalankan proses |
| PUT | Memperbarui data |
| DELETE | Menghapus data |


## 5. Endpoint Utama


### Authentication

POST /api/auth/login

Digunakan untuk melakukan proses login pengguna.


### Student Management

GET /api/students

Mengambil seluruh data siswa.


POST /api/students

Menambahkan data siswa.


PUT /api/students/{id}

Memperbarui data siswa.


DELETE /api/students/{id}

Menghapus data siswa.


### Dataset Management

POST /api/datasets/upload

Mengunggah dataset hasil belajar siswa.


GET /api/datasets

Melihat daftar dataset.


### Model Training

POST /api/models/train

Melakukan proses training model Random Forest.


GET /api/models/{id}/evaluation

Melihat hasil evaluasi model.


### Prediction

POST /api/predictions

Melakukan prediksi kategori hasil belajar siswa.


GET /api/predictions

Melihat riwayat prediksi.


## 6. Error Handling

API menggunakan HTTP status code berikut:

| Status Code | Keterangan |
|---|---|
| 200 OK | Berhasil mengambil atau memproses data |
| 201 Created | Data berhasil dibuat |
| 400 Bad Request | Input tidak sesuai |
| 401 Unauthorized | Pengguna belum login atau token tidak valid |
| 403 Forbidden | Pengguna tidak memiliki akses |
| 404 Not Found | Data tidak ditemukan |
| 500 Internal Server Error | Kesalahan pada server |


## 7. Konsistensi Desain

Desain API mengikuti rancangan:

- ERD sebagai struktur database.
- models.py sebagai struktur data.
- OpenAPI sebagai spesifikasi endpoint.

Setiap perubahan pada struktur data harus disesuaikan pada seluruh dokumen sistem.