from flask import Flask, render_template

app = Flask(__name__)

# Rute Utama: Langsung buka Movies Premiere
@app.route('/')
def home():
    return render_template('movies.html')

# Rute Tambahan: Untuk masuk ke Music Hub
@app.route('/music')
def music_hub():
    return render_template('music.html')

if __name__ == '__main__':
    print("--- [SYSTEM ACTIVE]: Menghubungkan Arsitek ke Platform ---")
    app.run(host='127.0.0.1', port=5000, debug=True)