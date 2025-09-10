Philo Pradipta Adhi Satriya
2406495426
PBP F

tautan menuju pws https://philo-pradipta41-eshoppbp.pbp.cs.ui.ac.id

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
>> Awalnya saya mengikuti tutorial 0 dan 1, lalu saya mempelajari juga via online untuk desain tambahan menggunakan tailwind (youtube web programming unpas)

> 1. Saya mulai dengan buka terminal di folder kerja, lalu menjalankan django-admin startproject eshop-pbp. Itu otomatis bikin struktur proyek dasar berisi file manage.py sama folder eshop-pbp (isi settings, urls, dll). Setelah itu aku bikin virtual environment pakai python -m venv venv dan aktifin dengan venv\Scripts\activate. Lanjut, aku install Django dan paket lain dari requirements.txt pakai pip install -r requirements.txt, terus cek hasilnya lewat pip list dan django-admin --version untuk memastikan version dari Django.

> 2. Lalu saya membuat aplikasi "main" di proyek itu dengan menjalanin python manage.py startapp main. Perintah ini otomatis bikin folder main yang isinya file standar seperti models.py, views.py, urls.py, dan admin.py. Ini dilakukan agar aplikasinya nyambung ke proyek utama, aku tambahin 'main' ke bagian INSTALLED_APPS di settings.py

> 3. Saya setup routing biar aplikasi main bisa jalan. Caranya, di file football_shop/urls.py (level proyek), aku impor include dari django.urls, lalu tambahin baris:
 > path('', include('main.urls'))
    > Dengan begitu, root URL langsung diarahkan ke aplikasi main. Lalu jalankan python manage.py runserver di terminal dan buka http://127.0.0.1:8000/ (cek hasil)

> 4. Lalu saya modifikasi file models.py yang sebelumnya kosong, sekarang diisi oleh
    name = models.CharField(max_length=100) (nama barang)
    price = models.IntegerField() (harga barang)
    description = models.TextField()  (deskripsi barang)
    thumbnail = models.URLField() (gambar/foto barang)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES) (kategori, contohnya "Sepatu Bola" atau "Baju Bola")
    is_featured = models.BooleanField(default=False) (status unggulan)
    stock = models.IntegerField(default=0) (atribut tambahan berupa stock barang tersebut)
    brand = models.CharField(max_length=50, blank=True, null=True) (atribut tambahan berupa merk barang tersebut)

> 5. Lalu saya membuat fungsi pada views.py untuk mengembalikan ke template main.html
from django.shortcuts import render
def show_main(request):
    context = {
        'app_name' : 'FootyRetail',
        'name': 'Philo Pradipta Adhi Satriya',
        'kelas': 'PBP F'
    }

    return render(request, "main.html", context)

> 6. Lalu kita membuat routing di urls.py aplikasi main untuk memetakan fungsi main.html pada views.py
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

> 7. Terakhir, jangan lupa push ke github dan deploy ke pws
git add .
git commit -m ""
git push origin master
git push pws master


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

>> Bagan

+---------+     HTTP Request (URL)    +---------+
| Client  | ------------------------> | Django  |
+---------+                           +---------+
                                         |
                                         | (1) URL Routing
                                         v
                                     +---------+
                                     | urls.py | -- (2) Panggil View yang sesuai
                                     +---------+
                                         |
                                         | (3) Panggil fungsi di views.py
                                         v
                                     +----------+
                                     | views.py | -- (4) Jika perlu, akses Model
                                     +----------+
                                         |
                                         | (5) Query ke Database via Model
                                         v
                                     +----------+
                                     | models.py| --> (6) ORM ke Database
                                     +----------+
                                         |
                                         | (7) Kembalikan data ke View
                                         v
                                     +----------+
                                     | views.py | -- (8) Render Template dengan data
                                     +----------+
                                         |
                                         | (9) Kirim HTML yang di-render
                                         v
+---------+     HTTP Response (HTML)  +---------+
| Client  | <------------------------ | Django  |
+---------+                           +---------+

> bagan simplified MVT (sesuai tutorial 1)
+-------------+    +-------------+    +-------------+
|   urls.py   | -> |  views.py   | -> | template.html| -> Response ke Client
| (URL Config)|    | (Controller)|    |   (View)     |
+-------------+    +-------------+    +-------------+
                         |
                         | (Jika perlu data)
                         v
                   +-------------+    +-------------+
                   |  models.py  | -> |  Database   |
                   |   (Model)   |    |             |
                   +-------------+    +-------------+
> urls.py (URL Routing) sebagai penghubung antara URL yang diminta client dengan views.py yang sesuai
> views.py memproses request, berinteraksi dengan models.py, dan menyiapkan response
> models.py mendefinisikan struktur data dan berinteraksi dengan database
> main.html akan menampilkan antarmuka pengguna dengan data dari views serta program html yang telah dibuat di dalam file itu sendiri

3. Jelaskan peran settings.py dalam proyek Django!
>> File ini adalah pusat pengaturan Django. Isi file ini terdiri atas:
>SECRET_KEY: kunci rahasia buat keamanan.
>DEBUG: kalau True, error ditampilkan detail (dipakai saat ngembangin). Kalau False, lebih aman buat produksi.
>INSTALLED_APPS: daftar aplikasi yang aktif di proyek.
>MIDDLEWARE: lapisan tambahan yang memproses request/response (contoh: keamanan, login).
>DATABASES: pengaturan database (jenis, user, password).
>STATIC_URL: lokasi file statis (CSS, JS, gambar).
>TEMPLATES: pengaturan tempat nyari file HTML.
>ROOT_URLCONF: tunjuk ke urls.py utama.

4. Bagaimana cara kerja migrasi database di Django?
>> Migrasi = cara Django menyesuaikan database dengan perubahan di models.py.
>> Langkahnya:
> 1. Ubah/tambah model di models.py.
> 2. Jalankan python manage.py makemigrations --> bikin file migrasi (catatan perubahan).
> 3. Jalankan python manage.py migrate --> Django ubah database sesuai catatan itu.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
>> Django cocok untuk pemula karena punya fitur bawaan yang lengkap seperti ORM, autentikasi, admin, dan migrasi, dilengkapi struktur rapih berbasis MVT yang dapat membantu kita dalam penulisan kode lebih teratur sejak awal(cocok untuk newbie). Selain itu, Django menyediakan panel admin otomatis untuk mengelola data, dokumentasi resmi yang jelas dan penuh contoh sehingga mudah dipahami, serta keamanan bawaan yang melindungi dari ancaman seperti SQL injection, XSS, dan CSRF.


6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
>> Feedback apresisasi karena tutorial dibuat dengan jelas dan terperinci, sehingga saya dapat dengan mudah mengikuti step-by-step.