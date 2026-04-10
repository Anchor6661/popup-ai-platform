from flask import Flask, render_template

# Inisialisasi Aplikasi Flask
app = Flask(__name__)

# --- CORE ROUTING ---
# Homepage: Mengarah ke templates/index.html yang sudah diverifikasi
@app.route('/')
def home():
    # Mengambil index.html yang baru saja kita beri background 8K
    return render_template('index.html')

# Jalur untuk fitur Cinema & Audio
@app.route('/movies')
def movies():
    return render_template('movies.html')

@app.route('/music')
def music():
    return render_template('music.html')

if __name__ == '__main__':
    print("--- [ORBIT SYSTEM ACTIVE] ---")
    print("Project Folder: popup_project")
    print("Sinyal Lokal: http://127.0.0.1:5000")
    # Debug mode aktif untuk memantau perubahan secara real-time
    app.run(host='127.0.0.1', port=5000, debug=True)