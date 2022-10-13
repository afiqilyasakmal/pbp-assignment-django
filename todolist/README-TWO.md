## Perbedaan antara asynchronous programming dengan synchronous programming

Sinkronus artinya saat client meng-click atau mengirim request, user harus menunggu server mengirim response terlebih dulu, baru user dapat berinteraksi lagi. Misal saat kita klik sesuatu di kolom pencarian google dan menekan enter, kita harus
menunggu google menampilkan semua informasi yang ada, baru kita bisa mengirim request lagi (misalnya ke halaman pencarian yang selanjutnya, mengklik URL hasil
pencarian). Pada sistem asinkronus user bisa terus berinteraksi saat menunggu respons dari server, jadi client tidak perlu menunggu halamannya selesai. Contoh: Whatsapp Web dan email.

## Maksud dari paradigma 'Event-driven Programming' dan penerapannya pada tugas ini.

Secara garis besarnya, 'event-driven programming' adalah alur program bukan ditentukan secara sekuensial (cara konvensional) melainkan alur program berjalan sesuai dengan 'event' yang diberikan oleh 'client'. Penerapannya pada tugas ini adalah saat 'button' pada modal pembuatan task baru diklik maka 'todolist' baru akan langsung ter-'trigger' dan langsung memperbarui daftar 'todolist'-nya.

## Penerapan asynchronous programming pada AJAX

Asynchronus programming diterapkan dengan AJAX dengan menggunakan XMLHttpRequest di mana proses yang diminta user dapat diproses di balik layar tanpa harus menunggu semua kode dieksekusi terlebih dahulu dan langsung mengirimkan request yang diminta oleh 'client'.

## Implementasi checklist di atas.

1. Membuat modal terlebih dahulu di `todolist.html` memanfaatkan modal bawaan Bootstrap kemudian modal diisi dengan kode yang sama dengan bagian `create_task.html`.
2. Membuat fungsi di `views.py` untuk menampilkan todolist menggunakan JSON.
3. Membuat 'routing' untuk implementasi fungsi tadi di `urls.py`
4. Membuat fungsi menggunakan JavaScript untuk mengambil data (sekaligus menampilkan) dan membuat task baru.
