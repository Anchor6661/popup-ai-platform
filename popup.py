from flask import Flask, render_template

app = Flask(__name__)

# --- CORE ROUTING: Memastikan Homepage adalah index.html ---
@app.route('/')
def home():
    # Kita kunci ke index.html sebagai Homepage Utama
    return render_template('index.html')

# Jalur cadangan jika Chef ingin memisahkan halaman movies
@app.route('/movies')
def movies_page():
    return render_template('index.html')

if __name__ == '__main__':
    print("--- [SYSTEM ACTIVE]: Menghubungkan Arsitek ke Platform ---")
    # Menjalankan di localhost port 5000
    app.run(host='127.0.0.1', port=5000, debug=True)