from flask import Flask, render_template, request, redirect, url_for, flash
from pathlib import Path
from werkzeug.utils import secure_filename
from uuid import uuid4

app = Flask(__name__)
app.secret_key = "distorsi-demo-secret-key"

# Data contoh disimpan di memori agar proyek mudah dipelajari.
# Produk baru akan tersedia selama server masih berjalan.
PRODUCTS = [
    {"id": 1, "name": "Rumah Sakit — Striped Tee", "band": "Rumah Sakit", "category": "Classic", "price": 185000, "size": "S, M, L, XL", "description": "Kaos garis horizontal navy dengan aksen merah dan hijau serta logo Rumah Sakit di bagian depan.", "image": "rumah-sakit.png", "tag": "LOCAL FAVORITE"},
    {"id": 2, "name": "The Jeblogs — Graphic Long Sleeve", "band": "The Jeblogs", "category": "Graphic", "price": 175000, "size": "S, M, L, XL", "description": "Kaos lengan panjang hitam dengan grafis monokrom khas The Jeblogs.", "image": "the-jeblogs.png", "tag": "GRAPHIC TEE"},
    {"id": 3, "name": "The Sigit — Psychedelic Tee", "band": "The Sigit", "category": "Graphic", "price": 195000, "size": "S, M, L, XL", "description": "Kaos hitam dengan artwork warna-warni bernuansa psychedelic di bagian depan.", "image": "the-sigit.png", "tag": "FAN FAVORITE"},
    {"id": 4, "name": "Colorcode — Long Sleeve", "band": "Colorcode", "category": "Essential", "price": 170000, "size": "S, M, L, XL", "description": "Kaos lengan panjang hitam dengan grafis Colorcode berwarna biru kehijauan.", "image": "colorcode.png", "tag": "NEW DROP"}
]
NEXT_ID = 5
UPLOAD_FOLDER = Path(app.root_path) / "static" / "images" / "uploads"
ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

def allowed_image(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_IMAGE_EXTENSIONS

@app.template_filter("rupiah")
def rupiah(value):
    return "Rp{:,.0f}".format(value).replace(",", ".")

@app.route("/")
def index():
    featured = PRODUCTS[:4]
    return render_template("index.html", featured=featured, page_title="Beranda")

@app.route("/produk")
def produk():
    q = request.args.get("q", "").strip()
    category = request.args.get("kategori", "Semua")
    shown = PRODUCTS
    if q:
        shown = [p for p in shown if q.lower() in p["name"].lower() or q.lower() in p["band"].lower()]
    if category and category != "Semua":
        shown = [p for p in shown if p["category"] == category]
    return render_template("produk.html", products=shown, q=q, category=category, page_title="Katalog")

@app.route("/tambah-produk", methods=["GET", "POST"])
def tambah_produk():
    global NEXT_ID
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        band = request.form.get("band", "").strip()
        category = request.form.get("category", "Essential")
        try:
            price = int(request.form.get("price", "0"))
        except ValueError:
            price = 0
        description = request.form.get("description", "").strip()
        size = request.form.get("size", "S, M, L, XL").strip()
        image_file = request.files.get("image")
        if not name or not band or price <= 0:
            flash("Nama produk, nama band, dan harga yang valid wajib diisi.", "error")
            return render_template("tambah_produk.html", page_title="Tambah Produk")

        image_name = "colorcode.png"  # Gambar bawaan jika pengguna tidak mengunggah gambar.
        if image_file and image_file.filename:
            if not allowed_image(image_file.filename):
                flash("Format gambar harus PNG, JPG, JPEG, atau WEBP.", "error")
                return render_template("tambah_produk.html", page_title="Tambah Produk")
            safe_name = secure_filename(image_file.filename)
            extension = safe_name.rsplit(".", 1)[1].lower()
            image_name = f"produk-{uuid4().hex}.{extension}"
            image_file.save(UPLOAD_FOLDER / image_name)
            image_name = f"uploads/{image_name}"

        PRODUCTS.append({
            "id": NEXT_ID, "name": name, "band": band, "category": category,
            "price": price, "size": size or "S, M, L, XL",
            "description": description or "Produk baru dari katalog Distorsi.",
            "image": image_name, "tag": "ADDED"
        })
        NEXT_ID += 1
        flash("Produk berhasil ditambahkan ke katalog.", "success")
        return redirect(url_for("produk"))
    return render_template("tambah_produk.html", page_title="Tambah Produk")

@app.route("/profil")
def profil():
    return render_template("profil.html", page_title="Tentang")

if __name__ == "__main__":
    app.run(debug=True)
