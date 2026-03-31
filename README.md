# IoT Smart Lamp with LDR + Monitoring

A real-time light intensity monitoring system using an **LDR sensor**, **Arduino**, and **Flask**.

---

## Important Information
This project runs on **Localhost**. It is not deployed to the cloud (Vercel) because it requires direct access to the **serial port (USB)** to physically read data from the Arduino.

---

## Tech Stack
- **Backend:** Python (Flask), PySerial
- **Frontend:** HTML, CSS, JavaScript (Fetch API)
- **Hardware:** Arduino Uno, Sensor LDR, 10k Ohm Resistor

---

## How to Run
1. Connect the Arduino to the USB port (Make sure the port is correct, e.g., `COM9`).
2. Install the libraries:
   ```bash
   pip install flask pyserial
3. Run the Flask server
   ```bash
   python app.py
4. Open in a browser:
   ```
   http://127.0.0.1:2009

# Folder Structure

- app.py: Main script (Flask & Serial Reader).
- /templates: Dashboard HTML files.
- /static: CSS files and supporting assets.
- Smart Lamp.ino: .ino code to upload to Arduino.

---

**Project by Haidar**
