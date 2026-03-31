from flask import Flask, render_template, jsonify, redirect, url_for
import serial
import threading
import time

app = Flask(__name__)

# Konfigurasi Serial
PORT = 'COM9'  # Sesuaikan dengan port kamu
BAUD = 9600

# Variabel Global untuk menyimpan data terakhir
data_sensor = {
    "ldr_value": 0,
    "status": "Menghubungkan...",
    "timer": 0
}

def read_serial():
    global data_sensor
    try:
        ser = serial.Serial(PORT, BAUD, timeout=1)
        time.sleep(2)  # Tunggu koneksi stabil
        print(f"Koneksi Berhasil di {PORT}")
        
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                
                if line:
                    if line.isdigit():
                        data_sensor["ldr_value"] = int(line)
                        data_sensor["status"] = "Terang" if int(line) >= 10 else "Gelap"
                    elif "Menghitung" in line:
                        # Mengambil angka dari teks "Menghitung : X"
                        val = line.split(":")[-1].strip()
                        data_sensor["timer"] = val
                        data_sensor["status"] = "Menghitung Durasi Gelap..."
                    elif "Sudah 30 detik" in line:
                        data_sensor["status"] = "Mode Hemat Daya (Tidur 8s)"
    except Exception as e:
        print(f"Error Serial: {e}")
        data_sensor["status"] = "Koneksi Terputus"

# Menjalankan pembacaan serial di thread terpisah agar Flask tidak hang
thread = threading.Thread(target=read_serial, daemon=True)
thread.start()

@app.route('/')
def ya():
    return redirect(url_for('index'))

@app.route('/dashboard')
def index():
    return render_template('dashboard.html')

@app.route('/get_data')
def get_data():
    # Route ini digunakan untuk update data secara otomatis via AJAX
    return jsonify(data_sensor)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=2009)