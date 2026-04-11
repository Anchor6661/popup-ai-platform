from flask import Flask, render_template

# --- INISIALISASI MESIN ---
app = Flask(__name__)

# Nama file aset 8K yang sudah divalidasi
TARGET_IMAGE = 'dreamina-2026-04-10-9380.jpg'

@app.route('/')
def home():
    """
    Menjalankan Homepage. 
    Mengirimkan bg_image sebagai variabel agar sinkron dengan template.
    """
    return render_template('index.html', bg_image=TARGET_IMAGE)

@app.route('/movies')
def movies():
    return render_template('movies.html', bg_image=TARGET_IMAGE)

@app.route('/music')
def music():
    return render_template('music.html')

if __name__ == '__main__':
    print("\n" + "="*60)
    print("          POPUP.AI CORE - STATUS: READY FOR LAUNCH")
    print("="*60)
    print("  > AKSES SEKARANG: http://127.0.0.1:5000")
    print("="*60 + "\n")
    
    # Pastikan tidak ada teks tambahan di luar blok if ini
    app.run(host='127.0.0.1', port=5000, debug=True)