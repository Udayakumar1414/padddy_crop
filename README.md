# 🌾 Smart Paddy Crop Management System

# 📌 Project Description

The Smart Paddy Crop Management System is an IoT-based agriculture monitoring project developed using Raspberry Pi, Ultrasonic Sensor, and Water Level Sensor.

This system helps farmers monitor crop growth stages and water levels automatically. Based on sensor readings, the system determines whether irrigation is required and displays the motor status.

The project supports:
- Smart farming
- Water conservation
- Automatic irrigation monitoring

---

# 🚀 Features

- ✅ Real-time crop monitoring
- ✅ Automatic water level detection
- ✅ Smart irrigation logic
- ✅ Crop stage identification
- ✅ Continuous sensor monitoring
- ✅ Low-cost smart farming solution

---

# 🛠️ Hardware Components Used

| Component | Quantity |
|---|---|
| Raspberry Pi 4 | 1 |
| HC-SR04 Ultrasonic Sensor | 1 |
| Water Level Sensor | 1 |
| Breadboard | 1 |
| Jumper Wires | As Required |
| Power Supply | 1 |

---

# 💻 Software Requirements

- Python 3
- Raspberry Pi OS
- RPi.GPIO Library

---

# 🧱 Block Diagram / Architecture

```text
               +-------------------+
               |   Ultrasonic      |
               |     Sensor        |
               +---------+---------+
                         |
                         |
                         v
                +----------------+
                | Raspberry Pi 4 |
                +----------------+
                         ^
                         |
                         |
               +---------+---------+
               |   Water Sensor    |
               +-------------------+

                         |
                         v

                +----------------+
                |  Motor Status  |
                | ON / OFF Logic |
                +----------------+
```

---

# 🔌 Pin Connections

# HC-SR04 Ultrasonic Sensor

| Sensor Pin | Raspberry Pi GPIO |
|---|---|
| VCC | 5V |
| GND | GND |
| TRIG | GPIO 23 |
| ECHO | GPIO 24 |

---

# Water Sensor

| Sensor Pin | Raspberry Pi GPIO |
|---|---|
| VCC | 3.3V |
| GND | GND |
| OUT | GPIO 17 |

---

# ⚙️ Working Principle

- 1️⃣ The ultrasonic sensor measures the distance between the sensor and crop surface.

- 2️⃣ Based on the measured distance, the crop stage is identified.

- 3️⃣ The water sensor checks the presence of water.

- 4️⃣ If water level is LOW:
- Motor Status → ON

- 5️⃣ If water level is HIGH:
- Motor Status → OFF

- 6️⃣ The complete field status is displayed continuously on the terminal.

---

# 📏 Crop Stage Classification

| Distance Range | Crop Stage |
|---|---|
| < 10 cm | GERMINATIVE |
| 10 – 30 cm | VEGETATIVE |
| > 30 cm | TILLERING |

---

# 🧪 Installation Steps

- 1️⃣ Update Raspberry Pi

```bash
sudo apt update
sudo apt upgrade
```

---

- 2️⃣ Install Python GPIO Library

```bash
pip install RPi.GPIO
```

---

- 3️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Smart-Paddy-Crop-Management.git
```

---

- 4️⃣ Open Project Folder

```bash
cd Smart-Paddy-Crop-Management
```

---

- 📚 Required Libraries

```python
import RPi.GPIO as GPIO
import time
```

---

- ▶️ How to Run the Project

```bash
python3 paddy_crop.py
```

---

- 🔄 Project Flowchart

```text
        START
          |
          v
 Initialize GPIO Pins
          |
          v
 Read Ultrasonic Sensor
          |
          v
 Calculate Distance
          |
          v
 Identify Crop Stage
          |
          v
 Read Water Sensor
          |
          v
 Check Water Level
          |
          +------------------+
          |                  |
          v                  v
     Water LOW          Water HIGH
          |                  |
          v                  v
     Motor ON            Motor OFF
          |
          v
 Display Field Status
          |
          v
       Repeat
```

---

- 📷 Sample Output

```text
Paddy Field Status
================================

Crop Distance : 12.34 cm
Crop Stage    : VEGETATIVE

--------------------------------

Water Level   : LOW
Motor Status  : ON

================================
```

---

# 🌾 Applications

- Smart Agriculture
- Precision Farming
- Automatic Irrigation System
- Water Conservation
- Crop Growth Monitoring

---

# ✅ Advantages

- Reduces water wastage
- Supports smart irrigation
- Easy to implement
- Low-cost agriculture solution
- Real-time monitoring

---

# 🔮 Future Improvements

- IoT Cloud Integration
- Mobile App Monitoring
- SMS/Email Alerts
- AI-based Crop Analysis
- Weather Prediction Integration

---

# 📌 Conclusion

The Smart Paddy Crop Management System provides an efficient and low-cost smart farming solution using Raspberry Pi and sensors.

The project helps monitor crop stages and water levels automatically, improving irrigation management and supporting sustainable agriculture practices.


