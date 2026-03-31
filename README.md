# IoT Smart Lamp Monitoring

Sistem monitoring intensitas cahaya real-time menggunakan **Sensor LDR**, **Arduino**, dan **Flask**.

---

## Informasi Penting
Proyek ini dijalankan di **Localhost**. Tidak di-deploy ke Cloud (Vercel) karena membutuhkan akses langsung ke **Serial Port (USB)** untuk membaca data dari Arduino secara fisik.

---

## Tech Stack
- **Backend:** Python (Flask), PySerial
- **Frontend:** HTML, CSS, JavaScript (Fetch API)
- **Hardware:** Arduino Uno, Sensor LDR, Resistor 10k Ohm

---

## Cara Menjalankan
1. Hubungkan Arduino ke USB (Pastikan port sesuai, misal: `COM9`).
2. Install library:
   ```bash
   pip install flask pyserial
3. Jalankan server Flask
   ```bash
   python app.py
4. Buka di browser:
   ```
   http://127.0.0.1:2009

# Struktur Folder

<li>app.py : Script utama (Flask & Serial Reader).</li>
<li>/templates : File HTML dashboard.</li>
<li>/static : File CSS dan aset pendukung.</li>
<li>Smart Lamp.ino : Kode .ino untuk di-upload ke Arduino.</li>

---

**Project by Haidar**
