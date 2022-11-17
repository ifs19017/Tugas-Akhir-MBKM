from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h2>Hello, World!</h2>"

@app.route('/home')
def home():
    return "<p>Nama Saya Montana</p>"

if __name__ == '__main__':
    app.run(debug=True, port=2812)