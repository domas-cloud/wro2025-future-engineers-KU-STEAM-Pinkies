# Hardware

## ⚙️ Used Components

- **Arduino Mega 2560**  
  The main control microcontroller responsible for reading all sensors and controlling the motors.  
  Chosen due to its larger memory and more I/O pins compared to the Arduino Uno.
  - **Raspberry pi zero2**
    To get info from camera

- **Adafruit Motor Shield V2**  
  Used to control DC motors. Allows speed and direction regulation.  
  Ensures stable control even under higher loads.  

- **TOF (VL53L1X) sensors**  
  Precise distance sensors used for obstacle detection and track analysis.  
  One is facing forward (for stopping before obstacles), others are facing sideways (for trajectory maintenance).  

- **Servo motor (SG90)**  
  Controls the front steering mechanism.  
  The servo angle is limited in software to avoid exceeding physical limits.  

- **DC motor**  
  Responsible for driving the car forward and backward.  
  Connected to the Motor Shield through L293D drivers.  

- **Li-ion batteries**  
  Power the entire system except raspberry pi.
- **Power bank** 
 Power the raspberry pi.
---

## 🔌 Wiring Diagram (described in words)

- Arduino Mega connects to the Motor Shield V2 via I2C.  
- The DC motor is connected to the Motor Shield output M1.  
- The servo motor is connected to a PWM output on the Mega.  
- TOF sensors are connected through the I2C bus (SDA, SCL).  
- The battery powers both the Arduino and the Motor Shield.  

---

## 🛠️ Component Selection Justification

- **Arduino Mega** was chosen for sufficient resources to handle multiple TOF sensors and PD control in real time.  
- **TOF sensors** provide much higher accuracy than ultrasonic sensors (±1 mm vs. ±10–20 mm).  
- **Servo motor** allows precise steering control, unlike regular DC motors.  
- **Li-ion batteries** provide a good balance between weight and energy capacity.  

---

## 📦 Hardware Expansion Possibilities

- Add an **IMU (gyroscope/accelerometer)** to improve corner detection.  
- Replace the servo with a **higher torque model** for more reliable steering.  
- Implement **battery voltage monitoring** so that the system automatically stops at a critical level.  

---
