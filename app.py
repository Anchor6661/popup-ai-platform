from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
import os

# =================================================================
# SYSTEM ENGINE: SAS (Serashii Anchor the Sovereign)
# CORE SERVER: POPUP.Ai Platform (Sovereign Edition)
# =================================================================

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    """Gerbang Utama: Horizon Peradaban"""
    # Mengarahkan pengunjung ke halaman utama nebula
    return render_template('index.html')

@app.route('/movies')
def movies():
    """Galeri Sinematik: Jalur Visual"""
    # Membuka gerbang galeri film
    return render_template('movies.html')

# Jalur khusus untuk aset statis (gambar, css, js)
# Vercel akan secara otomatis memetakan folder 'static'
@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory('static', filename)

# JANGAN tambahkan 'app = app' di sini untuk menghindari loop import.
# Vercel secara otomatis akan mencari variabel bernama 'app' di file ini.
if __name__ == '__main__':
    # Mode lokal untuk pengujian di laptop Chef
    app.run(debug=True)