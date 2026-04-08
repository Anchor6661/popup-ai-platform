import os
import base64

# =================================================================
# SYSTEM ENGINE: SAS (Serashii Anchor the Sovereign)
# MISSION: GENERATE PUBLIC ASSETS (FAVICON & ICONS)
# =================================================================

def create_icons():
    # 1. Buat folder public jika belum ada
    # Folder ini adalah tempat Vercel mencari aset root secara otomatis
    if not os.path.exists('public'):
        os.makedirs('public')
        print("✅ Folder 'public' berhasil dibuat.")

    # 2. Data Base64 untuk Ikon Orange (Sovereign Theme)
    # Ikon Kecil (16x16) untuk browser tab
    orange_dot_png = (
        "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAMUlEQVR42mP8z8BQD8S"
        "MQByI08EYp2FmIEYYf8S6AC8mSBoYf8S6AC8mSBoYf8S6AC8mSBoAAH+fDRYJpE/pA"
        "AAAAElFTkSuQmCC"
    )
    
    # Ikon Apple (180x180 - High Definition)
    # Digunakan untuk perangkat iOS saat menyimpan website ke home screen
    apple_icon_png = (
        "iVBORw0KGgoAAAANSUhEUgAAALQAAAC0CAYAAAA9z9U6AAAABHNCSVQICAgIfAhkiA"
        "AAAD5JREFUeJzt0TEBAAAAwqD1T20ND6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        "AAAAAAAAAAAAAAAAAOBvBj8AAVp98TcAAAAASUVORK5CYII="
    )

    # Daftar aset lengkap untuk memenuhi permintaan berbagai browser (Chrome, Safari, dll)
    assets = {
        "public/favicon.ico": orange_dot_png,
        "public/favicon.png": orange_dot_png,
        "public/apple-touch-icon.png": apple_icon_png,
        "public/apple-touch-icon-precomposed.png": apple_icon_png
    }

    print("🚀 Ben sedang mencetak ulang ikon peradaban...")
    
    for path, data in assets.items():
        with open(path, "wb") as f:
            # Mengonversi data teks base64 menjadi file gambar fisik
            f.write(base64.b64decode(data))
        print(f"✅ Berhasil membuat: {path}")

if __name__ == "__main__":
    create_icons()
    print("\n🏁 SEMUA IKON SIAP. Silakan lakukan 'git push' sekarang!")