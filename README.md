Link aplikasi Adaptable yang telah di-deploy: https://ingredients-collection-app.adaptable.app/main/

# Penjelasan tentang Aplikasi Pengelolaan yang Saya Buat
Aplikasi pengelolaan yang saya buat terinspirasi dari *mobile game* Adorable Home, yang merupakan sebuah *game* simulasi.
Pada awal permainan, pengguna akan diminta untuk memilih seorang pasangan dan menempati sebuah rumah virtual dengan seekor kucing.
Selama permainan, pengguna akan mengelola rumah virtual tersebut bersama pasangannya.
Terdapat berbagai kegiatan yang dapat dilakukan pengguna selama bermain, salah satunya adalah memasak.
Akan tetapi, pengguna harus mencukupi banyak bahan makanan yang dibutuhkan agar dapat memasak suatu makanan. 
Bahan makanan yang dibutuhkan pun harus ditanam serta dipanen terlebih dahulu di kebun rumah virtual.
Proses ini tentunya akan memakan banyak waktu, terlebih (TODO)

# Penjelasan Implementasi Checklist
## Checklist 1 : Membuat Sebuah Proyek Django
### Step 1: Membuat Direktori Utama Proyek dan Mengaktifkan *Virtual Environment*
Sebelum membuat sebuah proyek Django untuk aplikasi saya, saya membuat sebuah direktori baru bernama `ingredients_collection` yang menjadi direktori utama pembuatan aplikasinya.
Setelah itu, saya mengaktifkan *virtual environment* di perangkat saya dengan *command*:
```
python -m venv env
```
dan 
```
source env/bin/activate
```
### Step 2: Melakukan *Setup Library* yang Dibutuhkan
Selanjutnya, saya membuat sebuah *file* bernama `requirements.txt` yang berisi beberapa *dependencies* (komponen-komponen yang diperlukan oleh perangkat lunak kita untuk berfungsi yang berisi *library*, *framework*, maupun *package*). Tanpa *dependencies*, perangkat lunak kita tidak akan berjalan semestinya. Isi dari `requirements.txt` adalah sebagai berikut:
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
Kemudian, *dependencies* akan dipasang dengan *command* berikut: 
```
pip install -r requirements.txt
```
### Step 3: Membuat Proyek `ingredients_collection`
Selanjutnya, saya membuat proyek Django yang bernama `ingredients_collection` dengan *command* berikut:
```
django-admin startproject ingredients_collection .
```
## Checklist 2: Membuat Aplikasi dengan Nama `main` dalam Proyek
## Checklist 3: Melakukan Routing pada Proyek
## Checklist 4: Membuat Model pada Aplikasi `main` dengan Nama `Item`
## Checklist 5: Membuat Sebuah Fungsi pada `views.py`
## Checklist 6: Membuat Sebuah *Routing* pada `urls.py` Aplikasi `main`
## Checklist 7: Melakukan *Deployment* ke Adaptable terhadap Aplikasi yang Sudah Dibuat
## Checklist 8: Membuat Sebuah `README.md` 
