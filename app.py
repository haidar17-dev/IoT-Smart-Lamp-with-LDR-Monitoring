from flask import Flask, render_template, jsonify
import serial
import threading
import time

app = Flask(__name__, template_folder='templates', static_folder='static')

PORT = 'COM9'
BAUD = 9600

data_sensor = {
    "ldr_value": 0,
    "status": "Menghubungkan...",
    "timer": 0
}

def read_serial():
    global data_sensor
    try:
        ser = serial.Serial(PORT, BAUD, timeout=1)
        time.sleep(2)
        print(f"Connection successfully on {PORT}")
        
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                
                if line:
                    if line.isdigit():
                        data_sensor["ldr_value"] = int(line)
                        data_sensor["status"] = "Bright" if int(line) >= 10 else "Dark"
                    elif "Menghitung" in line:
                        val = line.split(":")[-1].strip()
                        data_sensor["timer"] = val
                        data_sensor["status"] = "Calculating the duration of darkness..."
                    elif "Sudah 30 detik" in line:
                        data_sensor["status"] = "Power-saving mode (8-second sleep)"
    except Exception as e:
        print(f"Error Serial: {e}")
        data_sensor["status"] = "Connection Lost"


thread = threading.Thread(target=read_serial, daemon=True)
thread.start()

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/get_data')
def get_data():
    return jsonify(data_sensor)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=2009)