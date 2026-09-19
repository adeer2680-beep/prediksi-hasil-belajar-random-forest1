# User Stories, Use Case, User Flow, Acceptance Criteria & Traceability Matrix

# 1. Functional Requirement (FR)

Functional Requirement diambil dari dokumen SRS sistem **Prediksi Kategori Hasil Belajar Siswa Menggunakan Algoritma Random Forest Berbasis Web**.

| ID FR | Functional Requirement |
|---|---|
| FR-01 | Sistem dapat mengelola data siswa |
| FR-02 | Sistem dapat mengelola dataset hasil belajar |
| FR-03 | Sistem dapat melakukan preprocessing data |
| FR-04 | Sistem dapat melatih model Random Forest |
| FR-05 | Sistem dapat melakukan prediksi kategori hasil belajar siswa |
| FR-06 | Sistem dapat menampilkan hasil prediksi |
| FR-07 | Sistem dapat menampilkan evaluasi model |
| FR-08 | Sistem dapat menyimpan riwayat prediksi |


# 2. User Story

## US-01 Mengelola Data Siswa

**Sebagai** admin sistem,  
**saya ingin** mengelola data siswa,  
**agar** data siswa dapat digunakan dalam proses prediksi hasil belajar.

**FR Asal:** FR-01

**Prioritas:** Must Have

**Kategori:** Fitur Inti


---

## US-02 Mengelola Dataset Hasil Belajar

**Sebagai** admin sistem,  
**saya ingin** mengelola dataset hasil belajar siswa,  
**agar** sistem memiliki data yang dapat digunakan untuk proses analisis.

**FR Asal:** FR-02

**Prioritas:** Must Have

**Kategori:** Fitur Inti


---

## US-03 Melakukan Preprocessing Data

**Sebagai** admin sistem,  
**saya ingin** melakukan preprocessing data hasil belajar,  
**agar** data yang digunakan dalam model Random Forest memiliki kualitas yang sesuai.

**FR Asal:** FR-03

**Prioritas:** Must Have

**Kategori:** Fitur AI ★


---

## US-04 Melatih Model Random Forest

**Sebagai** admin sistem,  
**saya ingin** melatih model Random Forest menggunakan dataset hasil belajar,  
**agar** sistem memiliki model yang dapat digunakan untuk melakukan prediksi.

**FR Asal:** FR-04

**Prioritas:** Must Have

**Kategori:** Fitur AI ★


---

## US-05 Melakukan Prediksi Kategori Hasil Belajar

**Sebagai** guru,  
**saya ingin** melakukan prediksi kategori hasil belajar siswa,  
**agar** saya dapat mengetahui kategori capaian belajar siswa.

**FR Asal:** FR-05

**Prioritas:** Must Have

**Kategori:** Fitur AI ★


---

## US-06 Melihat Hasil Prediksi

**Sebagai** guru,  
**saya ingin** melihat hasil prediksi kategori hasil belajar siswa,  
**agar** saya dapat memahami hasil analisis sistem.

**FR Asal:** FR-06

**Prioritas:** Must Have

**Kategori:** Fitur Inti


---

## US-07 Melihat Evaluasi Model

**Sebagai** admin sistem,  
**saya ingin** melihat hasil evaluasi model Random Forest,  
**agar** saya dapat mengetahui performa model prediksi.

**FR Asal:** FR-07

**Prioritas:** Should Have

**Kategori:** Fitur AI ★


---

## US-08 Melihat Riwayat Prediksi

**Sebagai** guru,  
**saya ingin** melihat riwayat hasil prediksi siswa,  
**agar** saya dapat melakukan pemantauan perkembangan hasil belajar.

**FR Asal:** FR-08

**Prioritas:** Should Have

**Kategori:** Fitur Inti


---

# 3. Evaluasi INVEST User Story

| ID | Independent | Negotiable | Valuable | Estimable | Small | Testable |
|---|---|---|---|---|---|---|
| US-01 | Ya | Ya | Ya | Ya | Ya | Ya |
| US-02 | Ya | Ya | Ya | Ya | Ya | Ya |
| US-03 | Ya | Ya | Ya | Ya | Ya | Ya |
| US-04 | Ya | Ya | Ya | Ya | Ya | Ya |
| US-05 | Ya | Ya | Ya | Ya | Ya | Ya |
| US-06 | Ya | Ya | Ya | Ya | Ya | Ya |
| US-07 | Ya | Ya | Ya | Ya | Ya | Ya |
| US-08 | Ya | Ya | Ya | Ya | Ya | Ya |


---

# 4. Use Case

## UC-01 Mengelola Data Siswa

**Aktor Utama:**  
Admin Sistem

**Precondition:**
- Admin telah login ke sistem.
- Sistem tersedia.

**Postcondition:**
- Data siswa berhasil tersimpan atau diperbarui.

**Alur Utama:**
1. Admin membuka menu data siswa.
2. Admin memasukkan data siswa.
3. Sistem melakukan validasi data.
4. Sistem menyimpan data siswa.

**Alur Alternatif:**
- Data siswa tidak lengkap.
- Sistem meminta admin memperbaiki data.


---

## UC-02 Mengelola Dataset Hasil Belajar

**Aktor Utama:**  
Admin Sistem

**Precondition:**
- Admin telah login.
- Dataset tersedia.

**Postcondition:**
- Dataset berhasil tersimpan.

**Alur Utama:**
1. Admin mengunggah dataset hasil belajar.
2. Sistem membaca dataset.
3. Sistem melakukan validasi dataset.
4. Sistem menyimpan dataset.


---

## UC-03 Melakukan Prediksi Kategori Hasil Belajar

**Aktor Utama:**  
Guru

**Aktor Pendukung:**
- Database
- Model Random Forest

**Precondition:**
- Dataset hasil belajar tersedia.
- Model Random Forest tersedia.

**Postcondition:**
- Sistem menghasilkan kategori hasil belajar siswa.

**Alur Utama:**
1. Guru memilih data siswa.
2. Sistem mengambil data akademik siswa.
3. Sistem melakukan preprocessing data.
4. Sistem menjalankan model Random Forest.
5. Sistem menampilkan hasil prediksi.

**Alur Alternatif:**
- Data siswa belum lengkap.
- Sistem meminta pengguna melengkapi data.

**Alur Eksepsi AI:**
- Model gagal melakukan prediksi.
- Data tidak sesuai format.
- Sistem menampilkan pesan kesalahan.


---

# 5. User Flow

```mermaid
flowchart TD

A[Guru Login] --> B[Pilih Menu Prediksi]

B --> C[Input Data Siswa]

C --> D{Data Lengkap?}

D -- Tidak --> E[Tampilkan Pesan Perbaikan]

E --> C

D -- Ya --> F[Preprocessing Data]

F --> G[Proses Random Forest]

G --> H{Prediksi Berhasil?}

H -- Tidak --> I[Tampilkan Error]

H -- Ya --> J[Tampilkan Kategori Hasil Belajar]

J --> K[Simpan Riwayat Prediksi]

# 6. Acceptance Criteria

## AC-01 Pengelolaan Data Siswa

### Scenario: Data siswa berhasil disimpan

**Given**  
Admin telah login dan berada pada halaman pengelolaan data siswa.

**When**  
Admin memasukkan data siswa lengkap dan menyimpan data.

**Then**  
Sistem menyimpan data siswa ke database.


---

## AC-02 Prediksi Kategori Hasil Belajar

### Scenario: Prediksi berhasil dilakukan

**Given**  
Dataset hasil belajar tersedia dan model Random Forest siap digunakan.

**When**  
Guru menjalankan proses prediksi kategori hasil belajar.

**Then**  
Sistem menampilkan kategori hasil belajar siswa.


### Scenario: Data siswa tidak lengkap

**Given**  
Terdapat data siswa yang belum lengkap.

**When**  
Guru melakukan proses prediksi.

**Then**  
Sistem menampilkan pesan bahwa data harus dilengkapi.


### Scenario: Model Random Forest gagal

**Given**  
Model Random Forest mengalami gangguan.

**When**  
Guru menjalankan proses prediksi.

**Then**  
Sistem menampilkan pesan kegagalan proses.


---

## AC-03 Melihat Hasil Prediksi

### Scenario: Hasil prediksi ditampilkan

**Given**  
Proses prediksi telah selesai dilakukan.

**When**  
Guru membuka hasil prediksi siswa.

**Then**  
Sistem menampilkan kategori hasil belajar siswa.


---

# 7. Traceability Matrix

| ID FR | User Story | Use Case | Acceptance Criteria | Komponen Sistem |
|---|---|---|---|---|
| FR-01 | US-01 Mengelola Data Siswa | UC-01 Mengelola Data Siswa | AC-01 | Database Siswa |
| FR-02 | US-02 Mengelola Dataset Hasil Belajar | UC-02 Mengelola Dataset | AC-01 | Dataset |
| FR-03 | US-03 Melakukan Preprocessing Data | UC-03 Prediksi Hasil Belajar | AC-02 | Preprocessing |
| FR-04 | US-04 Melatih Model Random Forest | UC-03 Prediksi Hasil Belajar | AC-02 | Random Forest Model |
| FR-05 | US-05 Melakukan Prediksi Kategori Hasil Belajar | UC-03 Prediksi Hasil Belajar | AC-02 | Machine Learning Model |
| FR-06 | US-06 Melihat Hasil Prediksi | UC-03 Prediksi Hasil Belajar | AC-03 | Dashboard |
| FR-07 | US-07 Melihat Evaluasi Model | UC-03 Prediksi Hasil Belajar | AC-03 | Evaluasi Model |
| FR-08 | US-08 Melihat Riwayat Prediksi | UC-03 Prediksi Hasil Belajar | AC-03 | Riwayat Prediksi |