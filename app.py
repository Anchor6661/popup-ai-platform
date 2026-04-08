from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
import os

# =================================================================
# SYSTEM ENGINE: SAS (Serashii Anchor the Sovereign)
# CORE SERVER: POPUP.Ai Platform (Sovereign Edition)
# =================================================================

app = Flask(__name__)
# Menambahkan Secret Key untuk stabilitas sesi serverless
app.secret_key = os.environ.get("SECRET_KEY", "sas_sovereign_2026")
CORS(app)

@app.route('/')
def home():
    """Gerbang Utama: Horizon Peradaban"""
    return render_template('index.html')

@app.route('/movies')
def movies():
    """Galeri Sinematik: Jalur Visual"""
    return render_template('movies.html')

# Jalur statis otomatis (Vercel handle folder static secara native)
@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory('static', filename)

# Vercel membutuhkan objek 'app' ini untuk dikenali sebagai entry point
# JANGAN pindahkan atau hapus baris di bawah ini
app = app

if __name__ == '__main__':
    # Mode lokal tetap aktif untuk laptop Chef
    app.run(debug=True)