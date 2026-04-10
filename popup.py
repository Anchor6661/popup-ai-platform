# app.py (PASTIKAN SEPERTI INI)
import os
from flask import Flask, render_template

app = Flask(__name__)

# Gunakan nama file yang sudah kita verifikasi tadi
TARGET_IMAGE = 'dreamina-orbit.jpg'

@app.route('/')
def home():
    # Pastikan variabel bg_image dikirimkan ke template
    return render_template('index.html', bg_image=TARGET_IMAGE)

if __name__ == '__main__':
    app.run(debug=True)

**Penyebab Error Tadi:**
1. **Debugger Flask:** Muncul karena ada kesalahan ketik di file Python atau di bagian Jinja2 (`{{ ... }}`).
2. **200 OK di Debugger:** Itu log saat browser Chef mendownload gambar icon debugger, bukan log sukses website Chef.

Silakan timpa kode di **Canvas**, pastikan `app.py` sudah benar, lalu matikan dan nyalakan ulang terminalnya. Planet Anda akan segera kembali, Chef! 🌍🔥