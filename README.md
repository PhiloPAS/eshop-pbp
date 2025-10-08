Philo Pradipta Adhi Satriya
2406495426
PBP F

tautan menuju pws https://philo-pradipta41-eshoppbp.pbp.cs.ui.ac.id

# Tugas 2:

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
>> Awalnya saya mengikuti tutorial 0 dan 1, lalu saya mempelajari juga via online untuk desain tambahan menggunakan tailwind (youtube web programming unpas)

> 1. Saya mulai dengan buka terminal di folder kerja, lalu menjalankan django-admin startproject eshop-pbp. Itu otomatis bikin struktur proyek dasar berisi file manage.py sama folder eshop-pbp (isi settings, urls, dll). Setelah itu aku bikin virtual environment pakai python -m venv venv dan aktifin dengan venv\Scripts\activate. Lanjut, aku install Django dan paket lain dari requirements.txt pakai pip install -r requirements.txt, terus cek hasilnya lewat pip list dan django-admin --version untuk memastikan version dari Django.

> 2. Lalu saya membuat aplikasi "main" di proyek itu dengan menjalanin python manage.py startapp main. Perintah ini otomatis bikin folder main yang isinya file standar seperti models.py, views.py, urls.py, dan admin.py. Ini dilakukan agar aplikasinya nyambung ke proyek utama, aku tambahin 'main' ke bagian INSTALLED_APPS di settings.py

> 3. Saya setup routing biar aplikasi main bisa jalan. Caranya, di file football_shop/urls.py (level proyek), aku impor include dari django.urls, lalu tambahin baris:
 > path('', include('main.urls'))
    > Dengan begitu, root URL langsung diarahkan ke aplikasi main. Lalu jalankan python manage.py runserver di terminal dan buka http://127.0.0.1:8000/ (cek hasil)

> 4. Lalu saya modifikasi file models.py yang sebelumnya kosong, sekarang diisi oleh
    ```python 
    name = models.CharField(max_length=100) (nama barang)
    price = models.IntegerField() (harga barang)
    description = models.TextField()  (deskripsi barang)
    thumbnail = models.URLField() (gambar/foto barang)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES) (kategori, contohnya "Sepatu Bola" atau "Baju Bola")
    is_featured = models.BooleanField(default=False) (status unggulan)
    stock = models.IntegerField(default=0) (atribut tambahan berupa stock barang tersebut)
    brand = models.CharField(max_length=50, blank=True, null=True) (atribut tambahan berupa merk barang tersebut)
```
    
    
    

> 5. Lalu saya membuat fungsi pada views.py untuk mengembalikan ke template main.html
```python
from django.shortcuts import render
def show_main(request):
    context = {
        'app_name' : 'FootyRetail',
        'name': 'Philo Pradipta Adhi Satriya',
        'kelas': 'PBP F'
    }
    
    return render(request, "main.html", context)
```

> 6. Lalu kita membuat routing di urls.py aplikasi main untuk memetakan fungsi main.html pada views.py

```python 
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

> 7. Terakhir, jangan lupa push ke github dan deploy ke pws
```
git add .
git commit -m ""
git push origin main
git push pws main
```


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

>> Bagan
> Bagan Versi Full ada di dalam file foto
![alt text](<Bagan Full.png>)

> Bagan Versi Simplified MVT (sesuai tutorial 1) ada di dalam file foto
![alt text](<Bagan MVT Simplified.png>)

> urls.py (URL Routing) sebagai penghubung antara URL yang diminta client dengan views.py yang sesuai
> views.py memproses request, berinteraksi dengan models.py, dan menyiapkan response
> models.py mendefinisikan struktur data dan berinteraksi dengan database
> main.html akan menampilkan antarmuka pengguna dengan data dari views serta program html yang telah dibuat di dalam file itu sendiri

3. Jelaskan peran settings.py dalam proyek Django!
```
>> File ini adalah pusat pengaturan Django. Isi file ini terdiri atas:
>SECRET_KEY: kunci rahasia buat keamanan.
>DEBUG: kalau True, error ditampilkan detail (dipakai saat ngembangin). Kalau False, lebih aman buat produksi.
>INSTALLED_APPS: daftar aplikasi yang aktif di proyek.
>MIDDLEWARE: lapisan tambahan yang memproses request/response (contoh: keamanan, login).
>DATABASES: pengaturan database (jenis, user, password).
>STATIC_URL: lokasi file statis (CSS, JS, gambar).
>TEMPLATES: pengaturan tempat nyari file HTML.
>ROOT_URLCONF: tunjuk ke urls.py utama.
```

4. Bagaimana cara kerja migrasi database di Django?
```
>> Migrasi = cara Django menyesuaikan database dengan perubahan di models.py.
>> Langkahnya:
> 1. Ubah/tambah model di models.py.
> 2. Jalankan python manage.py makemigrations --> bikin file migrasi (catatan perubahan).
> 3. Jalankan python manage.py migrate --> Django ubah database sesuai catatan itu.
```

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
>> Django cocok untuk pemula karena punya fitur bawaan yang lengkap seperti ORM, autentikasi, admin, dan migrasi, dilengkapi struktur rapih berbasis MVT yang dapat membantu kita dalam penulisan kode lebih teratur sejak awal(cocok untuk newbie). Selain itu, Django menyediakan panel admin otomatis untuk mengelola data, dokumentasi resmi yang jelas dan penuh contoh sehingga mudah dipahami, serta keamanan bawaan yang melindungi dari ancaman seperti SQL injection, XSS, dan CSRF.


6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
>> Feedback apresisasi karena tutorial dibuat dengan jelas dan terperinci, sehingga saya dapat dengan mudah mengikuti step-by-step.


--------------------------------------------------------------
# Tugas 3:
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
> agar kita dapat mengirimkan data produk/stock secara ke client (web/mobile/third-party), memungkinkan decoupling backend–frontend, mendukung multi-klien, konsistensi data, caching/performance, dan kontrol akses/security.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
> Menurut saya JSON lebih baik untuk API modern karena lebih ringkas, lebih mudah diparse di JavaScript, langsung merepresentasikan objek/array, dan lebih ringan. XML berguna untuk dokumen kompleks/namespace, tapi JSON lebih populer karena kesederhanaan dan ekosistem web.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
> is_valid() akan menjalankan validasi field & cross-field, mengisi cleaned_data dan errors, lalu mengembalikan boolean. Function ini dibutuhkan agar hanya data yang valid yang diproses/disimpan, mencegah data corrupt, dan menjaga keamanan data.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
> csrf_token mencegah CSRF (request palsu dari situs lain). Tanpa token tersebut, penyerang bisa memaksa browser korban melakukan hal-hal yang berbahaya, seperti memindah saldo, mengubah data, serta memakai sesi korban sehingga aksi-aksi berbahaya lainnya dapat dijalankan tanpa izin(ilegal).

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
> 1 -- Data delivery: saya membuat endpoint di views.py dan urls.py untuk menampilkan data produk dalam format JSON (misalnya serializers.serialize("json", products)), sehingga data bisa dipakai front-end atau aplikasi lain.
--------
> 2 -- Saya pilih JSON karena lebih sederhana untuk dibaca dan langsung bisa dipakai di Front-end.
--------
> 3 -- is_valid(): saat membuat form di Django (misalnya untuk create_product), saya gunakan form.is_valid() agar hanya data produk yang valid (name, price, stock, dll) yang masuk ke database.
--------
> 4 -- csrf_token: di template form seperti create_product.html, saya tambahkan {% csrf_token %} agar aman dari serangan CSRF saat user mensubmit produk baru.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
> Sama seperti tutorial-tutorial sebelumnya, props to team asdos dan dosen yang sudah membuat tutorial dengan sangat jelas sehingga saya tidak kesulitan memahami sedikitpun.


_____________
Foto Postman
_____________

![alt text](<Screenshot 2025-09-17 at 01.57.45.png>)
![alt text](<Screenshot 2025-09-17 at 01.57.19.png>)
![alt text](<Screenshot 2025-09-17 at 01.55.57.png>)
![alt text](<Screenshot 2025-09-17 at 01.55.37.png>)



--------------------------------------------------------------
# Tugas 4
1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
> AuthenticationForm adalah form bawaan Django yang (kali ini) kita gunakan di login_user sebagai tempat setor kredensial, memvalidasi melalui authenticate() dan memberi akses ke form.get_user() untuk dipakai oleh login(). Kelebihannya: cepat dipasang, aman secara default untuk validasi password, dan langsung kompatibel dengan login() sehingga session berfungsi tanpa banyak boilerplate. Kekurangannya muncul jika kita ingin login dengan email atau menambahkan 2FA/lockout, kita perlu subclass atau integrasi tambahan karena AuthenticationForm hanya menangani username/password dan tidak memberi proteksi brute-force atau OTP otomatis.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
> Autentikasi memastikan identitas (siapa pengguna) sedangkan otorisasi menentukan apa yang boleh dilakukan dan untuk di tugas kali ini, autentikasi dihandle oleh AuthenticationForm + login() dan AuthenticationMiddleware sehingga request.user tersedia, dan otorisasi sederhana diimplementasikan lewat decorator @login_required dan filter di show_main (Product.objects.filter(user=request.user) untuk “My Products”), serta pengecekan ownership yang kita gunakan di view/detail rendering — untuk granular permission (edit/delete hanya atmin).

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
> Session (server-side) dan cookies (client-side) masing-masing muncul di program. Kita menggunakan session-based auth (Django login() menyimpan session id) dan juga menulis cookie last_login sendiri, kelebihan session adalah data sensitif tidak tersimpan di client dan mudah di-invalidasi di server, sedangkan cookie mudah dipakai untuk data ringan dan persistensi di client. Kekurangannya session perlu storage/skalabilitas (shared store seperti Redis jika banyak user), menyimpan last_login sebagai cookie adalah nyaman tapi bukan sumber kebenaran terbaik (lebih baik gunakan request.user.last_login).

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
> Cookies tidak selalu aman karena bisa dicuri lewat XSS atau jaringan tanpa HTTPS, jadi jangan (tidak disarankan) untuk menyimpan data rahasia langsung di cookies. Django membantu dengan cara menyimpan data session di server (browser hanya pegang ID), memberi tanda tangan digital (signed) pada cookie supaya tidak bisa dipalsukan, dan mengaktifkan HttpOnly agar cookie tidak bisa diakses JavaScript.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
> Saya mengimplementasikan checklist dengan menambahkan field `user` pada model `Product` menggunakan `ForeignKey` agar setiap produk terkait dengan user, lalu menjalankan `makemigrations` dan `migrate` supaya database diperbarui tanpa merusak data lama. Di `views.py`, saya ubah `create_product` agar menggunakan `commit=False` sehingga bisa menetapkan `product.user = request.user` sebelum disimpan, serta menambahkan `request.FILES` agar upload file berfungsi. Fungsi `show_main` saya perbaiki untuk membaca query parameter `filter` sehingga bisa menampilkan semua produk atau hanya milik user yang sedang login, dan `show_product` saya ubah menjadi `select_related('user')` untuk mengurangi query sekaligus menambahkan `try/except` agar error saat increment views tidak memutus rendering. Di template, saya perbaiki `product_detail.html` untuk menampilkan author dengan aman dan menambahkan tombol filter All/My Product di `main.html` agar user bisa memilih produk yang ditampilkan. Selain itu, saya menambahkan cookie `last_login` saat login dan menghapusnya saat logout supaya informasi login terakhir bisa ditampilkan.

--------------------------------------------------------------
# Tugas 5

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
> Jika ada beberapa CSS selector yang mengatur elemen yang sama, browser menentukan prioritas dengan aturan specificity, yaitu urutannya dari paling kuat hingga paling lemah: inline style (style="..."), kemudian ID selector (#id), lalu class/attribute/pseudo-class (.class, :hover, [type="text"]), dan terakhir element/pseudo-element selector (div, h1, ::before). Jika tingkatnya sama, maka rule yang ditulis paling akhir dalam CSS yang akan berlaku.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
> Responsive design penting karena tampilan web harus menyesuaikan berbagai ukuran layar (desktop, tablet, smartphone) agar pengalaman pengguna tetap baik tanpa harus zoom in atau scroll berlebihan, serta meningkatkan SEO karena Google mengutamakan situs mobile-friendly; contohnya, aplikasi seperti Shopee atau Tokopedia sudah menerapkan responsive design dengan layout yang fleksibel di HP maupun desktop, sedangkan beberapa website lama instansi pemerintah masih belum responsive sehingga tampilan tabel atau teks jadi sulit dibaca di perangkat kecil.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
> Margin, border, dan padding adalah bagian dari box model CSS yang berfungsi berbeda: margin adalah jarak di luar border untuk memberi ruang antar elemen, border adalah garis bingkai di sekitar elemen, sedangkan padding adalah jarak antara isi (konten) dengan border agar konten tidak mepet; ketiganya dapat diatur dengan CSS misalnya margin: 20px;, border: 2px solid black;, dan padding: 10px; untuk menampilkan perbedaan fungsi masing-masing.

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
> Flexbox dan Grid adalah teknik layout modern di CSS dengan fungsi berbeda, di mana Flexbox cocok untuk tata letak satu dimensi (horizontal atau vertikal) seperti navbar atau daftar card, karena dapat mengatur alignment dan distribusi ruang menggunakan properti justify-content dan align-items, sedangkan Grid digunakan untuk tata letak dua dimensi (baris dan kolom sekaligus) seperti dashboard atau galeri produk, dengan pengaturan seperti grid-template-columns dan grid-template-rows, sehingga keduanya saling melengkapi tergantung kebutuhan layout.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
> 1. Pertama-tama kita mengatuk static files yang terletak pada file settings.py, terdapat static_root untuk menentukan absolute path ke directory static files dan berguna untuk menyediakan path konten statis ke akses production.
> 2. Kedua, menambahkan tailwind ke base.html (saya sudah menambahkan tailwind sejak tugas 2)
> 3. Ketiga, kita menambahkan fitur edit product dan hapus product alias buat function baru di views.py, lalu kita tambahkan berkas html baru di aplikasi main yang berjudul edit_product.html. Jangan lupa import di urls.py serta tambahkan path urlpatterns.
> 4. Modifikasi main.html yang terletak di aplikasi main agar ada button untuk edit dan delete product.
> 5. Kita gunakan navigation bar (navbar) agar saat user menggunakan handphone/tab yang pixel width nya lebih kecil daripada laptop, beberapa tombol akan terkumpul di navbar tersebut untuk mempermudah user dalam penggunaan web
> 6. Jangan lupa konfigurasi static files pada middleware yang terletak di settings.py serta pastikan static_root, staticfiles_dirs, dan static_url terkonfigurasi.
> 7. Terakhir, kita styling global.css, login.html, create_product, product_detail.html, register.html, dan edit_product menggunakan script tailwind agar web terlihat lebih bagus, modern, dan user-friendly.


--------------------------------------------------------------
# Tugas 6

 1. Apa perbedaan antara synchronous request dan asynchronous request?
 > Request synchronous memblokir eksekusi sampai ada respons, contohnya user klik link lalu browser menunggu seluruh halaman baru selesai didownload dan dirender sebelum bisa interaksi lagi. sedangkan asynchronous request (AJAX/fetch) berjalan di background tanpa menghentikan interaksi UI, jadi halaman utama tetap responsif sementara data dimuat/diubah secara bertahap.

 2. Bagaimana AJAX bekerja di Django (alur request–response)?
 > Browser JavaScript membuat HTTP request (biasanya fetch/XMLHttpRequest) ke endpoint Django dengan header seperti X-Requested-With: XMLHttpRequest dan header CSRF. Django menerima request, memverifikasi CSRF dan autentikasi, memproses data (misal validasi form atau operasi DB), lalu mengembalikan JsonResponse atau status HTTP yang sesuai, pada client, callback/then memproses JSON tersebut dan memperbarui DOM tanpa reload penuh(jika perlu), client juga memperbarui URL/history atau menampilkan pesan sukses/gagal.

 3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
 > AJAX memungkinkan partial update sehingga hanya data yang berubah yang dikirim/dirender (mengurangi bandwidth dan latency), membuat app lebih cepat dan interaktif karena tidak ada full page reload, memungkinkan UX yang lebih halus (inline edit, infinite scroll, live search), dan memisahkan logika tampilan/client dari logika server sehingga bisa membangun pengalaman single-page–like sambil tetap memanfaatkan Django sebagai backend.

 4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
 > Selalu gunakan CSRF protection (sertakan token CSRF dan periksa di server), gunakan HTTPS untuk melindungi kredensial, jangan membuka @csrf_exempt kecuali sangat perlu, lakukan validasi dan sanitasi input di server (misal Django AuthenticationForm/UserCreationForm), batasi percobaan (rate limit/lockout), kembalikan pesan error umum (jangan bocorkan detail sensitif), simpan kata sandi hanya lewat mekanisme hashing Django, serta pastikan endpoint memeriksa autentikasi/otorisasi dan membatasi akses berdasarkan metode HTTP yang sesuai (POST untuk kredensial).

 5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
 > AJAX meningkatkan persepsi kecepatan dan kelancaran interaksi karena user melihat respon instan tanpa reload, memungkinkan fitur modern (instant feedback, inline edit, load-on-scroll) yang membuat aplikasi terasa modern, namun bila salah pakai bisa menimbulkan masalah konsistensi state, kebingungan navigasi (back/forward), atau isu aksesibilitas. Oleh karena itu, gunakan indikator loading, update history (History API) bila perlu, dan sediakan fallback server-rendered agar pengalaman tetap baik untuk semua user.