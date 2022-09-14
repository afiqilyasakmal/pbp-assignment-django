# Tautan Aplikasi Heroku

Tautan aplikasi Heroku tugas 2 PBP ini dapat dilihat [di sini](https://tugas2-pbp-afiq.herokuapp.com/katalog).

![Bagan](https://i.ibb.co/Qr3vXR3/bagan-cara-kerja-django.png)

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

Pertama-tama, Ketika users me-*request* sesuatu maka request tersebut akan masuk ke server Django dan diproses di urls.py di mana di urls akan dibuat routing atau bisa dibilang bagaimana dari request tersebut dialihkan ke halaman yang mana yang ada di aplikasi kita. Nah aturan-aturan penanganan routing ini diatur di urls.py. Dari urls, permintaan diteruskan di views.py di mana di file ini terdapat fungsi Python yang mengambil http request dan mengembalikan http response seperti dokumen HTML. Di bagian ini pula apabila request memerlukan database, views dapat memproses hal tersebut dengan memanggil query ke models.py dan database akan mengembalikan hasil query ke views tadi. Setelah segala request diproses, hasilnya akan ditampilkan ke user di browser dalam bentuk HTML yang didefinisikan di folder templates. Templates mana yg digunakan tergantung bagaimana routing yang kita atur di bagian urls.py.

## Cara Menggunakan

Apabila kamu ingin menggunakan repositori ini sebagai repositori awalan yang nantinya akan kamu modifikasi:

1. Buka laman GitHub repositori templat kode, lalu klik tombol "**Use this template**"
   untuk membuat salinan repositori ke dalam akun GitHub milikmu.
2. Buka laman GitHub repositori yang dibuat dari templat, lalu gunakan perintah
   `git clone` untuk menyalin repositorinya ke suatu lokasi di dalam sistem
   berkas (_filesystem_) komputermu:

   ```shell
   git clone <URL ke repositori di GitHub> <path ke suatu lokasi di filesystem>
   ```
3. Masuk ke dalam repositori yang sudah di-_clone_ dan jalankan perintah berikut
   untuk menyalakan _virtual environment_:

   ```shell
   python -m venv env
   ```
4. Nyalakan environment dengan perintah berikut:

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```
5. Install dependencies yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut:

   ```shell
   pip install -r requirements.txt
   ```

6. Jalankan aplikasi Django menggunakan server pengembangan yang berjalan secara
   lokal:

   ```shell
   python manage.py runserver
   ```
7. Bukalah `http://localhost:8000` pada browser favoritmu untuk melihat apakah aplikasi sudah berjalan dengan benar.

## Contoh Deployment 

Pada template ini, deployment dilakukan dengan memanfaatkan GitHub Actions sebagai _runner_ dan Heroku sebagai platform Hosting aplikasi. 

Untuk melakukan deployment, kamu dapat melihat instruksi yang ada pada [Tutorial 0](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-0).

Untuk contoh aplikasi Django yang sudah di deploy, dapat kamu akses di [https://django-pbp-template.herokuapp.com/](https://django-pbp-template.herokuapp.com/)

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.
