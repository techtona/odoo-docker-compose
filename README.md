# 🐘 Odoo 18 + PostgreSQL + PgAdmin (Docker Compose)

Repositori ini menyediakan environment siap pakai untuk menjalankan **Odoo 18** menggunakan Docker Compose, lengkap dengan database **PostgreSQL** dan antarmuka database **PgAdmin**. Mendukung baik Odoo Community maupun Enterprise (jika memiliki lisensi resmi).

---

## 📦 Komponen

- **Odoo 18** – ERP open-source berbasis Python
- **PostgreSQL 15** – Database backend untuk Odoo
- **PgAdmin 4** – GUI web untuk manajemen PostgreSQL
- **Custom Entrypoint** – Untuk substitusi konfigurasi dinamis via `.env`

---

## 🗂 Struktur Direktori

├── docker-compose.yml
├── .env
├── odoo.conf
├── entrypoint.sh
├── addons/
│ ├── custom/ ← Custom addons
│ └── enterprise/ ← Odoo Enterprise (opsional)
├── data/
│ ├── db/ ← Volume data PostgreSQL
│ ├── odoo/ ← Volume data Odoo
│ └── pgadmin/ ← Volume data PgAdmin
└── logs/ ← (Opsional) log file Odoo

## ⚙️ Cara Menjalankan

### 1. Clone Repositori

```bash
git clone https://github.com/techtona/odoo-2025.git
cd odoo-2025
```

### 2. Buat file .env
Buat file .env di root project dan isi dengan konfigurasi berikut atau bisa copy dari file .env.example:

```env
Copy
PG_DB=odoo
PG_USER=odoo
PG_PASSWORD=odoo123
Kamu bisa sesuaikan nilai PG_ di atas sesuai kebutuhan.
```

### 3. Jalankan Docker Compose
```bash
docker compose up --build
```

Docker akan:
- Menjalankan Odoo di port 8069
- Menjalankan PostgreSQL sebagai backend database
- Menjalankan PgAdmin di port 5019 (jika diaktifkan)

### 4. Akses Aplikasi
Layanan	URL	Username / Password
| 🧩 Layanan   | 🌐 URL                | 🔐 Username / Password           |
|--------------|------------------------|----------------------------------|
| **Odoo**     | http://localhost:8069  | Buat database saat pertama kali |
| **PgAdmin**  | http://localhost:5019  | admin@gmail.com / admin         |


### 5. Inisialisasi Database Odoo
Akses halaman berikut di browser:

```bash
http://localhost:8069/web/database/manager
```

Isi form:
- Master Password: admin (atau sesuai admin_passwd di odoo.conf)
- Nama Database: odoo18
- Email Admin: admin@domain.com
- Password Admin: admin123
- Klik Create Database, dan Odoo siap digunakan.

### 🔐 Odoo Enterprise (Opsional)
Jika kamu memiliki lisensi Enterprise, clone modul resminya ke folder berikut:

```bash
git clone git@github.com:odoo/enterprise.git addons/enterprise
Pastikan kamu sudah menambahkan SSH key ke GitHub Odoo dan memiliki akses resmi.
```

Lalu atur addons_path di odoo.conf:

```ini
addons_path = /mnt/custom,/mnt/enterprise
```

### 🧹 Membersihkan (Reset Total)
Untuk menghentikan dan menghapus semua container serta volume:

```bash
docker compose down -v
```

### 📄 Lisensi
Konfigurasi ini disediakan untuk keperluan pengembangan.
Jika menggunakan Odoo Enterprise, pastikan Anda memiliki lisensi resmi dari Odoo S.A.