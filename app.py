from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
import os

# =================================================================
# SYSTEM ENGINE: SAS (Serashii Anchor the Sovereign)
# CORE SERVER: POPUP.Ai Platform (Sovereign Edition)
# =================================================================

app = Flask(__name__)
# Tambahkan Secret Key untuk kestabilan sesi di awan
app.secret_key = os.environ.get("SECRET_KEY", "sas_sovereign_2026")
CORS(app)

# --- PERINGATAN BEN: JANGAN MEMBUAT FOLDER DI VERCEL ---
# Vercel adalah sistem Read-Only. os.makedirs akan menyebabkan Error 500.
# Kita biarkan folder statis dikelola oleh sistem Vercel secara otomatis.

@app.route('/')
def home():
    """Gerbang Utama: Horizon Peradaban"""
    return render_template('index.html')

@app.route('/movies')
def movies():
    """Galeri Sinematik: Jalur Visual"""
    return render_template('movies.html')

# Jalur khusus aset statis (CSS, JS, Ikon)
@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory('static', filename)

# Memastikan Vercel mengenali 'app' sebagai pintu masuk utama
app = app

if __name__ == '__main__':
    # Mode lokal tetap bisa berjalan di laptop Chef
    app.run(debug=True)