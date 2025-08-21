# 💻 Software Idea and Implementation

## 🧠 Main Idea

The goal of our code is to ensure that the car drives stably, can detect obstacles, and adapts to the track shape.  
For this, we use a **three-layer architecture**:  
1. **Obstacle Detection**  
2. **Navigation**  
3. **Control**

---

## 🔑 Step-by-Step Code Flow

### 1. Sensor Reading
- The program first reads the **TOF sensors** (front + sides).  
- If one sensor returns an invalid value, the program assigns a maximum distance so that a faulty signal does not cause sudden braking.  
- The car always first “looks at the environment,” checks the front and side distances, and only then makes decisions.  

---

### 2. Error Calculation
- The measured data is compared to the desired distance from the wall or the center of the track.  
- The difference (**error**) shows how much the car has deviated.  
- If the car is too close to the wall → error positive.  
- If too far → error negative.  
- This error becomes the main indicator used to adjust the steering.  

---

### 3. PD Control Algorithm
- The control signal consists of:  
  - **Proportional part (P)** → how much the car has deviated.  
  - **Derivative part (D)** → how quickly that deviation is changing.  
- The car not only sees *how much* it deviates, but also *how fast* it happens.  
- This prevents oscillation from side to side.  

---

### 4. Steering Servo Control
- The PD output is converted into a **steering angle**.  
- Large error → strong steering correction.  
- Small error → slight correction.  
- Steering values are limited in software so the servo does not exceed its physical range.  

---

### 5. Motor Update
- The **DC motor** is controlled through the Adafruit Motor Shield.  
- If sensors show a clear path → base speed is maintained.  
- If an obstacle is detected → the motor slows down or stops.  
- At each cycle, the robot decides whether to **keep driving**, **slow down**, or **stop**.  

---

### 6. Obstacle Detection Logic
- If the **front TOF sensor** shows a distance smaller than safe, the robot stops.  
- If the obstacle is only on one side, the car adjusts steering to go around it.  
- If all sensors fail → the robot stops in **safety mode**.  

---

## 💬 Additional Logic
- **Safety stop** if all sensors give invalid values.  
- **Servo angle limits** to avoid gear skipping.  
- **Base driving mode** if no obstacles are detected.  
- **TCS34725 Color Sensor** is used to **detect and count orange and blue lines**, serving as checkpoints for lap counting.  

---

## ▶️ How to Run the Code

### 1. Clone the Repository with Submodules
```bash
git clone --recurse-submodules https://github.com/domas-cloud/wro2025-future-engineers-KU-STEAM-Pinkies.git
cd wro2025-future-engineers-KU-STEAM-Pinkies
git submodule update --init --recursive
# 💻 Software – Build & Run

---

## 2. Open the `src/` Folder in PlatformIO
- Install [PlatformIO](https://platformio.org/) (VSCode extension or CLI).  
- Target board: **Arduino Mega 2560**.  

---

## 3. Build & Upload
```bash
pio run
pio run -t upload
# 💻 Software – Run & Setup

---

## 4. Monitor Serial Output (optional)
```bash
pio device monitor

---

# 💻 Software – Hardware Setup & Summary

## 5. Hardware Setup
- **Arduino Mega** connected to **Adafruit Motor Shield V2** (I2C)  
- **DC motor** → Motor Shield M1  
- **Servo motor** → PWM pin (D9)  
- **TOF sensors (VL53L1X)** → I2C bus (SDA, SCL)  
- **Color sensor (TCS34725)** → same I2C bus  
- **Raspberry Pi Zero 2 ↔ Arduino Mega** via Serial (115200 baud)  
- **Power**: Li-ion batteries (Arduino + Motor Shield) + Power bank (Raspberry Pi)  

---

## 📚 Required Libraries
Make sure the following libraries are installed in PlatformIO or Arduino IDE:  
- `Adafruit Motor Shield V2 Library`  
- `Adafruit VL53L1X`  
- `Adafruit TCS34725`  
- `Wire` (I2C)  
- `Servo`  

---

## 🔮 Future Improvements
- Add an **integral part (I)** for full PID control to reduce long-term errors  
- Implement **adaptive PID tuning** so the robot can adjust Kp and Kd automatically  
- Improve obstacle avoidance to include **dynamic path planning**  
- Add **machine learning** (on Raspberry Pi) to optimize driving behavior  

---

## ✅ Summary
Our program works as follows:  

1. The robot **observes the environment** (sensors)  
2. It **calculates deviation** (error)  
3. It **adjusts steering and speed** (servo + DC motor)  

This process mimics human driving: **look → decide → act**.  
With PD control, the car drives smoothly, avoids obstacles, and counts checkpoints using color detection.


