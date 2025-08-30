# 🔌 Electronics Diagrams

We designed and tested two wiring configurations for our robot: one with **5 ToF sensors only**, and one with **3 ToFs + IMU**. Both share the same **core PD control algorithm** – only the sensor inputs differ.

---

## 📐 Variant A – Without IMU (5× ToF)

**Description:**  
- **Arduino Mega 2560** is the main controller.  
- **5× VL53L1X ToF sensors** connected to the I²C bus (SDA/SCL).  
- Each ToF has an **XSHUT** line connected to a digital pin on Arduino to assign unique I²C addresses during initialization.  
- Optional **GPIO1/INT** lines can be connected for interrupts (not required).  
- **Motor/Servo module** controls the steering servo (PWM) and the DC drive motor (PWM).  

**Power:**  
- ToFs powered at 3.3 V, common GND with Arduino.  
- Servo + motor require stable 5–6 V supply (separate BEC recommended).  

📄 *See schematic:* [`Without IMU.pdf`](Without%20IMU.pdf)

---

## 📐 Variant B – With IMU (3× ToF + IMU)

**Description:**  
- **Arduino Mega 2560** is again the main controller.  
- **3× VL53L1X ToFs** on the same I²C bus.  
- **IMU sensor** (gyroscope + accelerometer) also connected to I²C, providing yaw/gyro data.  
- ToF **XSHUT** pins used for unique addressing as before.  
- **IMU INT** (interrupt) optionally connected to a digital input for faster reaction.  
- **Motor/Servo module** wiring unchanged (PWM).  

**Power:**  
- IMU powered at 3.3 V, ToFs also at 3.3 V.  
- Common GND required.  
- Servo/motor powered separately as in Variant A.  

📄 *See schematic:* [`with IMU.pdf`](with%20IMU.pdf)

---

## ⚖️ Comparison

| Feature               | Without IMU (5 ToFs)        | With IMU (3 ToFs + IMU)    |
|------------------------|-----------------------------|-----------------------------|
| Distance sensing       | 5 directions (wider view)  | 3 directions + orientation |
| Orientation correction | From ToF geometry          | From IMU (yaw/gyro)        |
| I²C addressing         | 5× ToF via **XSHUT**       | 3× ToF via **XSHUT**, IMU fixed address |
| Wiring complexity      | More ToFs, more lines      | Fewer ToFs, extra IMU      |
| Algorithm              | **Same PD control**        | **Same PD control**        |

---

## 📝 Notes

- **Algorithm remains unchanged** in both cases (PD wall-following + motor control).  
- The only difference is the **sensor input**: either 5 ToFs, or 3 ToFs + IMU fusion.  
- Using IMU gave smoother turns and compensated for missing ToFs.  
- Proper power isolation (separate BEC for servo/motor, decoupling capacitors) is critical to avoid resets.  

---
