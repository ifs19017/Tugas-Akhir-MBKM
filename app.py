from flask import Flask, render_template

app = Flask(__name__)

konten = [
    {
    'penulis': 'Montana Gurning',
    'judul': 'Anggota Kelompok Pertama',
    'sinopsis': 'Ini adalah Anggota Kelompok pertama',
    'isi': 'Ini adalah isi dari Anggota Kelompok pertama',
    'tanggal': '12 Desember 2020',
    'jobdesc': 'Deployment'
    },
    {
    'penulis': 'Alex Muhamad Kasiba',
    'judul': 'Anggota Kelompok Kedua',
    'sinopsis': 'Ini adalah Anggota Kelompok kedua',
    'isi': 'Ini adalah isi dari Anggota Kelompok kedua',
    'tanggal': '13 Desember 2020',
    'jobdesc': 'Data Scrapping'
    },
    {
    'penulis': 'Muhammad Farid Al Hayat',
    'judul': 'Anggota Kelompok Ketiga',
    'sinopsis': 'Ini adalah Anggota Kelompok ketiga',
    'isi': 'Ini adalah isi dari Anggota Kelompok ketiga',
    'tanggal': '14 Desember 2020',
    'jobdesc': 'Feature Engineering'
    },
    {
    'penulis': 'Putri Ekarani',
    'judul': 'Anggota KelompokKeempat',
    'sinopsis': 'Ini adalah Anggota Kelompok keempat',
    'isi': 'Ini adalah isi dari Anggota Kelompok keempat',
    'tanggal': '15 Desember 2020',
    'jobdesc': 'Modelling & Visualisasi'
    },
    {
    'penulis': 'Rein Aisyah',
    'judul': 'Anggota KelompokKelima',
    'sinopsis': 'Ini adalah Anggota Kelompok kelima',
    'isi': 'Ini adalah isi dari Anggota Kelompok kelima',
    'tanggal': '16 Desember 2020',
    'jobdesc': 'Text Processing'
    }
]

@app.route("/home/")
def home():
    return render_template("home.html", konten=konten, judul='Beranda')

@app.route('/aplikasi/')
def aplikasi():
    return render_template("aplikasi.html")
# , judul='Tentang'

@app.route('/informasi/')
def informasi():
    return render_template("informasi.html")

@app.route('/kontak/')
def kontak():
    return render_template("kontak.html")

if __name__ == '__main__':
    app.run(debug=True, port=2812)