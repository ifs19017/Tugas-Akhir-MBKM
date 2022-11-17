from flask import Flask, render_template

app = Flask(__name__)

konten = [
    {
    'penulis': 'Montana Gurning',
    'judul': 'Postingan Pertama',
    'sinopsis': 'Ini adalah postingan pertama',
    'isi': 'Ini adalah isi dari postingan pertama',
    'tanggal': '12 Desember 2020',
    'jam': '16.00'
    },
    {
    'penulis': 'Alex Muhamad Kasiba',
    'judul': 'Postingan Kedua',
    'sinopsis': 'Ini adalah postingan kedua',
    'isi': 'Ini adalah isi dari postingan kedua',
    'tanggal': '13 Desember 2020',
    'jam': '18.00'
    },
    {
    'penulis': 'Muhammad Farid Al Hayat',
    'judul': 'Postingan Ketiga',
    'sinopsis': 'Ini adalah postingan ketiga',
    'isi': 'Ini adalah isi dari postingan ketiga',
    'tanggal': '14 Desember 2020',
    'jam': '20.00'
    },
    {
    'penulis': 'Putri Ekarani',
    'judul': 'Postingan Keempat',
    'sinopsis': 'Ini adalah postingan keempat',
    'isi': 'Ini adalah isi dari postingan keempat',
    'tanggal': '15 Desember 2020',
    'jam': '13.00'
    },
    {
    'penulis': 'Rein Aisyah',
    'judul': 'Postingan Kelima',
    'sinopsis': 'Ini adalah postingan kelima',
    'isi': 'Ini adalah isi dari postingan kelima',
    'tanggal': '16 Desember 2020',
    'jam': '14.00'
    }
]

@app.route("/home/")
def home():
    return render_template("home.html", konten=konten, judul='Beranda')

@app.route('/tentang/')
def tentang():
    return render_template("tentang.html")
# , judul='Tentang'

@app.route('/masuk/')
def masuk():
    return render_template("masuk.html")

@app.route('/daftar/')
def daftar():
    return render_template("daftar.html")

if __name__ == '__main__':
    app.run(debug=True, port=2812)