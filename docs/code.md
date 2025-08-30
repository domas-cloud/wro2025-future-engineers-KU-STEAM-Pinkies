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
# 📏 How Distance to the Wall (d₁) is Calculated



The value **d₁** represents the **true perpendicular distance** from the robot’s side to the wall.  
It is calculated using **two TOF sensors** (front and rear) mounted on the same side of the robot.

---
## 🔹 Geometric Calculation of d₁

To obtain the true perpendicular distance to the wall, the robot uses two TOF sensors (front and rear).  
The diagram below shows how x₁ and x₂ are projected to calculate d₁:

<img width="632" height="648" alt="image" src="https://github.com/user-attachments/assets/6dedc208-3fd4-406c-ae73-772a011d1af5" />


Here:
- x₁ = front TOF measurement  
- x₂ = rear TOF measurement  
- L = distance between sensors  
- d₁ = perpendicular distance to the wall  
- d₂ = desired setpoint distance  

The angle φ is used to project the sensor readings, so the real distance is:  

d₁ ≈ ((x₁ + x₂) / 2) * cos(φ)   

---
## 🔹 Step 1 – Sensor Readings
- **x₁** = front TOF measurement (mm)  
- **x₂** = rear TOF measurement (mm)  
- **L** = longitudinal distance between the two sensors (mm)

---

## 🔹 Step 2 – Angle to the Wall
The tilt angle θ of the robot relative to the wall is computed as:

θ = arctan((x₂ - x₁) / L)

- If **x₁ < x₂** → the robot’s nose points **towards** the wall  
- If **x₁ > x₂** → the robot’s nose points **away** from the wall  

---

## 🔹 Step 3 – Perpendicular Distance
Since the sensors measure along their own axis (not perpendicular to the wall),  
the perpendicular distance is calculated as:

d₁ ≈ ((x₁ + x₂) / 2) * cos(θ)

---

## 🔹 Step 4 – Distance Error
The error used by the PD/PID controller is:

Δd = d₁ - d₂

Where **d₂** is the desired (setpoint) distance from the wall.

### Sensor Reading  
- In the fallback configuration, it also reads the IMU yaw.  

---

### Error Calculation  
- With IMU: yaw error is added to side distance error to stabilize turns.  

---

### PD Control Algorithm  
- With IMU: yaw correction is combined with side distance correction.  

---

# 🧭 Sensor Fusion (ToF + IMU Fallback)  

When only 3 ToFs are available:  
- Two side ToFs are used for distance alignment.  
- IMU provides yaw for orientation stability.  

This ensures stable turning even with fewer distance sensors.  
The PD control loop remains the same, only the sensor inputs are different.  

---

### 📚 Required Libraries  
- Adafruit Sensor (for IMU)  


# Obstacle Avoidance Algorithm

## 1. Object Detection with Camera
The robot uses a camera to detect colored objects.  
First, the system isolates the object of interest from the camera feed using a predefined color filter.  
The detected object represents a potential obstacle.

## 2. Distance Calculation
Once the object is detected, the system calculates its distance from the robot or from a reference wall.  
The distance is estimated based on the camera’s field of view, the object’s size in the image, and the robot’s current position.

## 3. Object Position Estimation
Using the processed camera data, the robot determines the object’s coordinates relative to its own position (x, y).  
This allows the robot to understand the exact location of the obstacle within its coordinate system.

## 4. Side Determination (Left/Right)
The system evaluates whether the detected object is located on the left or right side of the robot’s field of view.  
- If the object is on the left → the obstacle is considered left-side.  
- If the object is on the right → the obstacle is considered right-side.  

This decision defines the avoidance direction.

## 5. PD Control for Path Adjustment
Based on the obstacle position, the robot generates a corrected trajectory line that must be followed.  
A PD controller is then used to smoothly adjust the robot’s movement, ensuring it bypasses the obstacle while maintaining stable navigation.

---

### Summary
- **Camera** detects the colored obstacle.  
- **Distance & position** are calculated relative to the robot.  
- **Left/Right** determination defines avoidance direction.  
- **PID controller** follows an adjusted line to safely avoid the obstacle.


## 💬 Additional Logic
- **Safety stop** if all sensors give invalid values.  
- **Servo angle limits** to avoid gear skipping.  
- **Base driving mode** if no obstacles are detected.  
- **TCS34725 Color Sensor** is used to **detect and count orange and blue lines**, serving as checkpoints for lap counting.  

---

# ▶️ How to Run the Code

### 1. Clone the Repository with Submodules
```bash
git clone --recurse-submodules https://github.com/domas-cloud/wro2025-future-engineers-KU-STEAM-Pinkies.git
cd wro2025-future-engineers-KU-STEAM-Pinkies
git submodule update --init --recursive
```

---

### 2. Open the `src/` Folder in PlatformIO
- Install [PlatformIO](https://platformio.org/) (VSCode extension or CLI).  
- Target board: **Arduino Mega 2560**.  

---

### 3. Build & Upload
```bash
pio run
pio run -t upload
```

---

### 4. Monitor Serial Output (optional)
```bash
pio device monitor
```

---

# ⚙️ Hardware Setup

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
