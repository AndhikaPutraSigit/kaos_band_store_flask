# DISTORSI — Band Tee Store (Flask)

Prototipe e-commerce toko kaos bertema band untuk tugas kelompok PSWB. Proyek ini menggunakan Flask, Jinja2, CSS, dan JavaScript.

## Fitur
- Beranda dengan hero section, produk unggulan, dan informasi toko.
- Katalog produk dengan pencarian nama band/desain dan filter kategori.
- Form tambah produk yang menambahkan data ke katalog selama server aktif.
- Halaman profil dan bantuan dengan FAQ.
- Navigasi responsif untuk desktop dan ponsel.
- Tombol `+ ADD` untuk simulasi keranjang menggunakan `localStorage`.
- Ilustrasi produk SVG lokal sehingga gambar tidak bergantung pada URL eksternal.

## Struktur folder
```text
kaos_band_store_flask/
├── app.py
├── requirements.txt
├── README.md
├── static/
│   ├── css/style.css
│   ├── js/main.js
│   └── images/
└── templates/
    ├── base.html
    ├── index.html
    ├── produk.html
    ├── tambah_produk.html
    └── profil.html
```

## Cara menjalankan di VS Code (Windows)
1. Ekstrak file ZIP.
2. Buka folder `kaos_band_store_flask` di VS Code.
3. Buka terminal di VS Code.
4. Buat virtual environment:
   ```bash
   py -m venv venv
   ```
5. Aktifkan virtual environment:
   ```bash
   .\\venv\\Scripts\\activate
   ```
6. Instal dependensi:
   ```bash
   pip install -r requirements.txt
   ```
7. Jalankan aplikasi:
   ```bash
   python app.py
   ```
8. Buka `http://127.0.0.1:5000` di browser.

Jika perintah `py` tidak tersedia, coba `python -m venv venv`.

## Catatan prototipe
- Data produk tersimpan di memori, jadi produk yang ditambahkan akan hilang saat server dimulai ulang. Tahap berikutnya dapat mengintegrasikan SQLite.
- Keranjang hanya simulasi browser; checkout, akun pengguna, pembayaran, dan stok belum terhubung.
- Desain kaos adalah mockup grafis buatan untuk demonstrasi antarmuka, bukan merchandise resmi band.
- Google Fonts hanya digunakan untuk tipografi; jika internet tidak tersedia, browser akan menggunakan font cadangan.


## Foto produk
Empat foto produk yang digunakan pada katalog adalah foto yang diberikan pengguna: Rumah Sakit, The Jeblogs, The Sigit, dan Colorcode. File gambar berada di `static/images/`.
