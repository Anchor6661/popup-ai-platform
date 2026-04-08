from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
import os

# =================================================================
# SYSTEM ENGINE: SAS (Serashii Anchor the Sovereign)
# CORE SERVER: POPUP.Ai Platform (Sovereign Edition)
# =================================================================

app = Flask(__name__)
CORS(app)

# Ben memastikan semua jalur folder tersedia
for folder in ["static/uploads/movies", "static/uploads/system", "templates"]:
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

@app.route('/')
def home():
    """Gerbang Utama: Horizon Peradaban"""
    return render_template('index.html')

@app.route('/movies')
def movies():
    """Galeri Sinematik: Jalur Visual yang Diperbaiki"""
    return render_template('movies.html')

# Jalur khusus untuk aset statis agar Vercel tidak bingung
@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    # Mode Lokal untuk Serashii
    app.run(debug=True, host='0.0.0.0', port=5000)