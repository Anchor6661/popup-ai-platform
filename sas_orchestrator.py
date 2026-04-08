import os
import sys
import time

# =================================================================
# SYSTEM CORE: SAS (Serashii Anchor the Sovereign)
# MISSION: STABILIZATION & DOMAIN SYNC
# AGENT: Ben (Execution) & Lumia (Orchestration)
# =================================================================

try:
    from google import genai
except ImportError:
    print("❌ ERROR: Library 'google-genai' belum terpasang!")
    print("Saran: Jalankan 'pip install -U google-genai' di terminal.")
    sys.exit()

# 1. OTORITAS AKSES (API KEY)
# Kunci ini adalah jembatan menuju kecerdasan eksternal Gemini
RAW_KEY = "AIzaSyCy9KPc6DNh4VAX9EnkJAYEsOfBA1AL9V8"
API_KEY = RAW_KEY.strip()
client = genai.Client(api_key=API_KEY)
MODEL_TARGET = "gemini-2.5-flash"

def hajar_tugas(file_target, deskripsi_misi):
    """
    Fungsi utama Ben untuk mengambil instruksi Lumia dan 
    menerapkannya langsung ke dalam kode sumber file target.
    """
    if not os.path.exists(file_target):
        print(f"⚠️ SKIPPED: {file_target} tidak ditemukan.")
        return

    print(f"⚡ BEN SINKRONISASI: {file_target}")
    
    try:
        with open(file_target, 'r', encoding='utf-8') as f:
            kode_sumber = f.read()

        # Instruksi sistem yang mendikte gaya dan kualitas peradaban POPUP.Ai
        prompt = f"""
        Identitas: Ben (Teknisi SAS).
        Visi: POPUP.Ai - Planetary Edge 2.0 (Sovereign Edition).
        Slogan: 'Pop Up your world'.
        Domain: 'popup-ai.com'.
        Filosofi: Mendukung perjuangan Musik & Kuliner Serashii.
        
        WAJIB:
        1. Fix CSS: Pastikan 'background-clip: text;' bekerja untuk efek gradasi teks.
        2. Fix JS: Pastikan deteksi URL '?code=' untuk login otomatis berfungsi.
        3. Visual: Pertahankan estetika Living Universe (Nebula & Stars).
        4. MISI KHUSUS: {deskripsi_misi}
        
        KODE SUMBER SAAT INI:
        {kode_sumber}
        """

        response = client.models.generate_content(
            model=MODEL_TARGET,
            contents=prompt
        )
        
        kode_baru = response.text
        
        # Operasi Pembersihan: Membuang markdown pembungkus dari AI
        if "```html" in kode_baru:
            kode_baru = kode_baru.split("```html")[1].split("```")[0].strip()
        elif "```" in kode_baru:
            kode_baru = kode_baru.split("```")[1].split("```")[0].strip()
        
        # Menulis kembali hasil pemikiran Ben ke file fisik
        with open(file_target, 'w', encoding='utf-8') as f:
            f.write(kode_baru)
        
        print(f"✅ BEN SELESAI: {file_target} berhasil diperbarui!")
        
    except Exception as e:
        print(f"❌ ERROR PADA {file_target}: {e}")

if __name__ == "__main__":
    # Target misi sinkronisasi fajar ini
    target = {
        "templates/index.html": "Aktifkan sensor login otomatis, perhalus gerakan nebula, dan pastikan slogan 'Pop Up your world' terlihat megah.",
        "templates/movies.html": "Sinkronkan rute navigasi dengan popup-ai.com dan bersihkan sisa kode lama."
    }

    print("\n" + "="*60)
    print("🚀 SAS ORCHESTRATOR: MENGAKTIFKAN TANGAN BEN")
    print("🚀 TARGET: DOMAIN KEDAULATAN POPUP-AI.COM")
    print("="*60)
    
    for file, task in target.items():
        hajar_tugas(file, task)
        time.sleep(1.5) # Memberi jeda napas bagi mesin
        
    print("\n🏁 MISSION COMPLETE! Peradaban telah disinkronkan.")
    print("💡 Jalankan 'python app.py' untuk melihat hasilnya secara lokal.")
    print("💡 Jalankan 'git push origin main' untuk mengirimnya ke orbit global.")