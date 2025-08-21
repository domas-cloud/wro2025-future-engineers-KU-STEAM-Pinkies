# ⚙️ Hardware Documentation

## 🧩 Used Components

- **Arduino Mega 2560**  
  Main control microcontroller responsible for reading all sensors and controlling the motors.  
  - Large memory and many I/O pins compared to Arduino Uno  
  - Handles sensor fusion, obstacle avoidance, and communicates with Raspberry Pi  

- **Raspberry Pi Zero 2**  
  - Processes camera data (line / object detection)  
  - Sends simplified results to Arduino over serial (115200 baud)  
  - Offloads heavy tasks (image recognition) from Arduino  

- **Adafruit Motor Shield V2**  
  - Motor driver shield, controls DC motor via I2C  
  - Provides PWM speed regulation, H-bridge for direction control  
  - Leaves most Arduino pins free  

- **TOF Sensors (VL53L1X)**  
  - Millimeter-accurate time-of-flight sensors  
  - **Front sensor** → obstacle detection  
  - **Side sensors** → track centering  
  - More precise and reliable than ultrasonic sensors  

- **Color Sensor (TCS34725)**  
  - Reads RGB + clear light via I2C  
  - Used to **detect and count orange & blue lines** on the track  
  - Essential for lap counting and checkpoints  

- **Servo Motor (SG90)**  
  - Controls front steering mechanism  
  - PWM control from Arduino  
  - Software-limited range to prevent oversteering  

- **DC Motor**  
  - Drives the robot forward/backward  
  - Controlled through Motor Shield with PWM  
  - Gear reduction for torque & smoother motion  
  - Bearings used in drivetrain for efficiency  

- **Li-ion Batteries**  
  - Power Arduino, Motor Shield, motors, and sensors  
  - High energy density & rechargeability  

- **Power Bank**  
  - Dedicated 5V supply for Raspberry Pi  
  - Isolates Pi from motor power spikes  

---

## 🔌 Wiring Diagram (textual)

- **Arduino Mega ↔ Motor Shield V2**: I2C bus  
- **DC Motor** → Motor Shield **M1**  
- **Servo Motor** → Arduino **D9 (PWM)**  
- **TOF Sensors (VL53L1X)** → I2C (SDA, SCL), each with unique I2C address  
- **Color Sensor (TCS34725)** → I2C (same bus)  
- **Li-ion Battery Pack** → Arduino Mega + Motor Shield  
- **Raspberry Pi Zero 2** ↔ Arduino Mega → Serial (TX/RX, 115200 baud)  
- **Raspberry Pi Camera** → Pi camera port  
- **Power Bank → Raspberry Pi** (stable 5V supply)  

---

## 🛠️ Component Selection Justification

- **Arduino Mega** → many peripherals at once, strong I/O support  
- **Raspberry Pi Zero 2** → dedicated vision processor, avoids overloading Arduino  
- **Motor Shield V2** → reliable I2C control, PWM, H-bridges included  
- **TOF sensors** → accurate, fast, unaffected by surface angles (better than ultrasonic)  
- **Servo motor** → accurate steering vs DC continuous motors  
- **DC motor w/ gear reduction** → torque + smooth control  
- **Li-ion + Power bank separation** → isolates Pi from noisy motor voltage  

---

## 📦 Hardware Expansion Possibilities

- Add **IMU (accelerometer + gyroscope)** → tilt/orientation feedback  
- Add **wheel encoders** → closed-loop speed & distance tracking  
- Add **current sensors** → detect stalls / overload  
- Add **battery monitoring** → prevent low-voltage damage  
- Upgrade to **Raspberry Pi 4** → enable advanced vision (object detection, SLAM)  
- Add **Wi-Fi / Bluetooth** → for remote debugging & telemetry  

---
