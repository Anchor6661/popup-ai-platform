from flask import Flask, render_template

# Inisialisasi aplikasi Flask
app = Flask(__name__)

@app.route('/')
def home():
    """
    Menampilkan halaman utama 'New Civilization'.
    Flask akan otomatis mencari file di folder 'templates'.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Jalankan server lokal
    app.run(host='127.0.0.1', port=5000, debug=True)