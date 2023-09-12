[Link Adaptable](https://ingredients-collection-app.adaptable.app/main/)

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
Pada direktori proyek Django yang bernama `ingredients_collection`, saya membuat sebuah aplikasi bernama `main` dengan *command* berikut:
```
python manage.py startapp main
```
Aplikasi `main` terbentuk menjadi sebuah *folder* baru yang berisi *source codes* yang dibutuhkan untuk membuat aplikasi saya. 
## Checklist 3: Melakukan Routing pada Proyek
Selanjutnya, saya mendaftarkan aplikasi `main` dalam proyek dengan menambahkan `main` ke daftar aplikasi yang ada pada *file* `settings.py`. 
```
INSTALLED_APPS = [
    'main',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
## Checklist 4: Membuat Model pada Aplikasi `main` dengan Nama `Item`
### Step 1: Membuat Model `Item`
Model merupakan sumber data pada aplikasi yang akan kita buat. Model juga merupakan tempat penyimpanan yang menjadi *database* dari aplikasi kita karena menyimpan data-data yang bersesuaian dengan atribut yang telah kita tetapkan. Pada aplikasi ini, saya membuat sebuah model bernama `Item` yang memiliki empat atribut, yaitu `name`, `category`, `amount`, dan `description`.
```
from django.db import models

class Item(models.Model): 
    name = models.CharField(max_length=100) 
    category = models.CharField(max_length= 50, default = 'Uncategorized') 
    amount = models.IntegerField() 
    description = models.TextField() 
```
Setiap model merupakan Python class yang merupakan subclass dari `django.db.models.Model`. Setiap atribut pada model merepresentasikan sebuah *database*. Pada aplikasi saya, atribut-atribut yang saya buat memiliki kegunaan sebagai berikut:
* `name` berfungsi untuk menyimpan nama dari suatu bahan makanan.
* `category` berfungsi untuk menyimpan kategori dari suatu bahan makanan, misalnya 'strawberry' termasuk dalam kategori 'fruits'. *Default value* dari atribut ini adalah 'Uncategorized'.
* `amount` berfungsi untuk menyimpan banyak suatu bahan makanan.
* `description` berfungsi untuk menyimpan jenis-jenis makanan yang dapat dibuat dari suatu bahan makanan. Misalnya, dengan 'strawberry' kita dapat membuat 'strawberry pie'.
### Step 2: Melakukan Migrasi Model `Item`
Migrasi model dilakukan agar Django dapat melacak perubahan yang terjadi pada *database*, misalnya penambahan atribut. Saya melakukan migrasi setelah saya selesai menambahkan atribut-atribut pada model `Item` dengan *command* berikut:
```
python manage.py makemigrations
```
dan 
```
python manage.py migrate
```
## Checklist 5: Membuat Sebuah Fungsi pada `views.py`
### Step 1: Mengimpor Fungsi *render* dari Modul `django.shortcuts`
Pada *file* `views.py` yang terletak di dalam *folder* aplikasi `main`, saya menambahkan baris impor fungsi berikut:
```
from django.shortcuts import render
```
Fungsi *render* dibutuhkan untuk menghubungkan `view` dengan `template` menggunakan Django. Dengan fungsi *render*, fungsi yang akan kita buat dapat mengembalikan sebuah *template* HTML dan menampilkan nama beserta kelas kita saat aplikasi dijalankan.
### Step 2: Membuat Fungsi `show_main` yang Dapat Mengembalikan *Template* HTML dan Menampilkan Data
```
def show_main(request):
    context = {
        'name': 'Tengku Laras Malahayati',
        'class': 'PBP D'
    }
    return render(request, "main.html", context)
```
* Fungsi `show_main` akan mengembalikan sebuah *template* HTML dan menampilkan data nama beserta kelas saya.
### Step 3: Membuat *Template* HTML
Saya membuat sebuah *file* HTML bernama `main.html` dalam *folder* `main`. Isi dari *file* tersebut adalah sebagai berikut:
```
<head>
<title> Adorable Home's Ingredients Collection Page</title>
</head>

<h1>Adorable Home's Ingredients Collection Page</h1>

<h5>Name: </h5>
<p>{{ name }}</p> 
<h5>Class: </h5>
<p>{{ class }}</p> 
```
* *title* dari tampilan aplikasi saya adalah Adorable Home's Ingredients Collection Page.
* {{ name }} dan {{ class }} berfungsi untuk menampilkan nilai dari variabel `name` dan `class` yang telah didefinisikan pada `context` di fungsi `show_main`.
## Checklist 6: Membuat Sebuah *Routing* pada `urls.py` Aplikasi `main`
### Step 1: Mengizinkan Akses agar Tautan Aplikasi dapat Diakses secara Luas
Saya mengizinkan akses agar semua *host* dapat mengakses tautan aplikasi `main` dengan menambahkan *key* `"*"` pada variabel `ALLOWED_HOSTS`. Hal ini memungkinkan aplikasi `main` dapat diakses oleh publik. 
```
ALLOWED_HOSTS = ["*"]
```
### Step 2: Mengonfigurasi Routing URL pada aplikasi `main`

## Checklist 7: Melakukan *Deployment* ke Adaptable terhadap Aplikasi yang Sudah Dibuat
## Checklist 8: Membuat Sebuah `README.md` 
