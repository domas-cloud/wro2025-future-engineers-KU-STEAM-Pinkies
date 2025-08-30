# 🤖 WRO 2025 Future Engineers – KU STEAM Pinkies

![Arduino](https://img.shields.io/badge/Arduino-Mega%202560-00979D?logo=arduino&logoColor=white) ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Zero%202-A22846?logo=raspberrypi&logoColor=white) ![PlatformIO](https://img.shields.io/badge/PlatformIO-Ready-orange?logo=platformio&logoColor=white) ![License](https://img.shields.io/badge/License-MIT-green)

Welcome to our official repository for **WRO 2025 Future Engineers Challenge**!  

We are **KU STEAM Pinkies**, a passionate team of young engineers building an **autonomous robot car** capable of navigating real-world tracks, avoiding obstacles, and detecting checkpoints.

---

## 👥 Team Introduction

**Team Members & Roles**
- **Marius** – Programmer & Mechanical Designer  
- **Domas** – Manager, Marketing & Testing  
- **Jonas** – Electronics Specialist & Designer  

**Our Goal:**  
To design and build a reliable autonomous robot that can perceive its environment, make decisions in real time, and drive smoothly and safely.

---

## 📚 Documentation

Our development process is fully documented:

- 🧠 [Brainstorming](docs/brainstorming.md)  
- 🗓️ [Planning](docs/planning.md)  
- ⚙️ [Hardware](docs/hardware.md)  
- 🛠️ [Mechanical Design](docs/design.md)  
- 💻 [Software / Code](docs/code.md)  
- 🧪 [Testing](docs/testing.md)  
- 📊 [Evaluation](docs/evaluation.md)  
- ❗ [Encountered Problems and Solutions](docs/Encountered_Problems_and_Solutions.md)  
---

## ⚙️ Hardware Overview

- **Arduino Mega 2560** – main controller (sensors + decision-making)  
- **Raspberry Pi Zero 2** – handles camera vision, communicates with Arduino via Serial  
- **Adafruit Motor Shield V2** – motor driver (DC + Servo)  
- **TOF sensors (VL53L1X)** – distance & obstacle detection (front + sides)  
- **TCS34725 Color Sensor** – detects orange/blue track lines for checkpoint counting  
- **Servo motor (SG90)** – precise steering  
- **DC motor + gear reduction + bearings** – smooth driving with torque optimization  
- **Li-ion batteries** – powering Arduino + motors  
- **Power bank** – powering Raspberry Pi for stable 5V  



---

## 💻 Software Overview

The software is based on a **three-layer architecture**:

1. **Obstacle Detection** (sensors)  
2. **Navigation** (error calculation + decision making)  
3. **Control** (PD steering + motor speed regulation)  

### 🔑 Step-by-Step Flow
1. **Sensor Reading** – TOF + color sensor data  
2. **Error Calculation** – compare measured distance vs desired trajectory  
3. **PD Control** – proportional + derivative parts for stable steering  
4. **Servo Steering** – adjusts angle based on PD output  
5. **Motor Update** – base speed / slow down / stop depending on obstacles  
6. **Obstacle Logic** – stop, bypass, or continue safely  

### 💬 Extra Features
- **Safety stop** if all sensors fail  
- **Servo angle limits** to avoid mechanical stress  
- **Base driving mode** if no obstacles detected  
- **Color sensor** counts **checkpoints** (orange & blue lines)  

---

## ▶️ How to Run the Code

### 1. Clone the Repository with Submodules
```bash
git clone --recurse-submodules https://github.com/domas-cloud/wro2025-future-engineers-KU-STEAM-Pinkies.git
cd wro2025-future-engineers-KU-STEAM-Pinkies
git submodule update --init --recursive
```

### 2. Open in PlatformIO
- Install [PlatformIO](https://platformio.org/) (VSCode extension or CLI).  
- Target board: **Arduino Mega 2560**.  

### 3. Build & Upload
```bash
pio run
pio run -t upload
```

### 4. Monitor Serial Output (optional)
```bash
pio device monitor
```

---

## 📚 Required Libraries

Make sure the following libraries are installed in PlatformIO or Arduino IDE:  

- `Adafruit Motor Shield V2 Library`  
- `Adafruit VL53L1X`  
- `Adafruit TCS34725`  
- `Wire` (I2C)  
- `Servo`  

---

## ⚠️ Limitations & Known Issues

### 1. Ultrasonic Sensors (Initial Tests)  
- In the early prototype, we used **HC-SR04 ultrasonic sensors**.  
- **Problems encountered:**  
  - Narrow field of view.  
  - Inaccurate measurements on uneven or angled surfaces.  
  - “Blind spots” in curves.  
- Because of these limitations, we switched to **VL53L1X TOF sensors**, which provide faster and more reliable distance readings.

### 2. TOF (VL53L1X) Sensors  
- Sometimes inaccurate on **very shiny** or **black matte** surfaces.  
- Multiple TOFs on the same I2C bus require **address reassignment** in software to avoid conflicts.  

### 3. TCS34725 Color Sensor  
- Strong ambient light can interfere with detection.  
- Close color shades (similar orange/blue tones) sometimes cause **false checkpoint counts**.  

### 4. PD Control (No Integral Part)  
- Without the integral (I) term, **steady-state error** may occur (e.g., robot stays closer to one wall).  
- In very sharp turns, PD sometimes results in **over-steering**.  

### 5. Mechanical Limitations  
- Single DC motor + gear system does not provide perfectly stable speed.  
- Bearings reduced friction, but on longer tracks, slight **speed fluctuations** remain.  

### 6. Raspberry Pi Zero 2  
- Too weak for **real-time image processing**.  
- Cannot run complex ML/AI models effectively.  

### 7. Power Supply Issues  
- When batteries are low, the **servo and DC motor** become unstable.  
- A **voltage monitoring system** would help stop the robot before malfunction.  

✅ Despite these limitations, the system is **robust enough for competition use**, and each issue points toward **clear upgrade paths** for future iterations.

---

## 🔮 Future Improvements

- Add an **integral part (I)** for full PID control  
- Implement **adaptive PID tuning** (self-adjusting Kp & Kd)  
- Improve obstacle avoidance with **dynamic path planning**  
- Use **machine learning** on Raspberry Pi to optimize driving  
- Add **IMU + encoders** for precise navigation  
- Implement **battery monitoring & current sensing** for reliability  

---

## ✅ Summary

Our robot behaves like a human driver:  
1. **Look** → read sensors (TOF + Color)  
2. **Decide** → calculate errors & detect obstacles  
3. **Act** → adjust steering + motor speed  

With PD control, the car drives smoothly, avoids obstacles, and counts checkpoints reliably.  

---

## 📜 License
This project is licensed under the **MIT License** – feel free to use, modify, and share with credit.  
