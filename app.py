import os
from flask import Flask, render_template

# --- KONFIGURASI JALUR ---
base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, 
            template_folder=os.path.join(base_dir, 'templates'),
            static_folder=os.path.join(base_dir, 'static'))

# Nama file target sesuai screenshot Properties Chef
TARGET_IMAGE = 'dreamina-orbit.jpg'

def check_asset_ready():
    """Memeriksa apakah aset gambar sudah siap di folder static."""
    full_path = os.path.join(app.static_folder, TARGET_IMAGE)
    if os.path.exists(full_path):
        return True, "✅ SINYAL AKTIF: File terdeteksi sempurna."
    else:
        try:
            actual_files = os.listdir(app.static_folder)
            return False, f"❌ 404: File '{TARGET_IMAGE}' tidak ditemukan. Isi folder static: {actual_files}"
        except:
            return False, "❌ 404: Folder static tidak ditemukan."

@app.route('/')
def home():
    # Mengirimkan nama file target ke index.html
    return render_template('index.html', bg_image=TARGET_IMAGE)

@app.route('/movies')
def movies_page():
    return render_template('movies.html', bg_image=TARGET_IMAGE)

@app.route('/music')
def music_page():
    return render_template('music.html')

if __name__ == '__main__':
    is_ready, message = check_asset_ready()
    
    print("\n" + "="*70)
    print("              POPUP.AI - PROTOKOL FINAL RESTORASI")
    print("="*70)
    print(f"  [STATUS] : {message}")
    print(f"  [FOLDER] : {base_dir}")
    print(f"  [URL]    : http://127.0.0.1:5000")
    print("="*70)
    
    if not is_ready:
        print("\n  INSTRUKSI UNTUK CHEF:")
        print(f"  Pastikan file di folder static bernama: {TARGET_IMAGE}")
        print("="*70 + "\n")
    
    app.run(host='127.0.0.1', port=5000, debug=True)