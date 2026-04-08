from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
import os

# =================================================================
# SYSTEM ENGINE: SAS (Serashii Anchor the Sovereign)
# CORE SERVER: POPUP.Ai Platform (Sovereign Edition 2026)
# =================================================================

app = Flask(__name__)
CORS(app)

# --- KONFIGURASI DIREKTORI ---
# Ben memastikan jalur folder tersedia untuk penyimpanan aset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folders = [
    os.path.join("static", "uploads", "movies"),
    os.path.join("static", "uploads", "system"),
    "templates"
]

for folder in folders:
    path = os.path.join(BASE_DIR, folder)
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

# --- ROUTING PERADABAN ---

@app.route('/')
def home():
    """Gerbang Utama: Horizon Peradaban (Living Universe)"""
    return render_template('index.html')

@app.route('/movies')
def movies():
    """Galeri Sinematik: Jalur Visual yang Diperbaiki"""
    return render_template('movies.html')

# Jalur khusus untuk aset statis agar Vercel tidak bingung memetakan file
@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory(os.path.join(BASE_DIR, 'static'), filename)

# --- VERCEL EXPORT ---
# Variabel 'app' harus diekspor secara eksplisit di level global 
# agar Vercel Function Invocation tidak gagal (Error 500)
app = app

if __name__ == '__main__':
    # Mode Lokal untuk Serashii saat pengembangan di VS Code
    # Vercel akan mengabaikan blok ini dan langsung mengambil variabel 'app' di atas
    app.run(debug=True, host='0.0.0.0', port=5000)