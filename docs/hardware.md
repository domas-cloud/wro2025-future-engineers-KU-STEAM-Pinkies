# Hardware

## ⚙️ Used Components

- **Arduino Mega 2560**  
  The main control microcontroller responsible for reading all sensors and controlling the motors.  
  Chosen due to its larger memory and more I/O pins compared to the Arduino Uno.  
  It handles sensor fusion, decision-making (e.g., obstacle avoidance), and communicates with the Raspberry Pi for vision data.

- **Raspberry Pi Zero 2**  
  Used to process information from the camera, such as line or object detection.  
  Sends simplified results (like coordinates or detection flags) to the Arduino Mega over serial communication.  
  Offloads heavy image processing tasks that the Arduino cannot handle.

- **Adafruit Motor Shield V2**  
  Dedicated motor driver shield that controls DC motors.  
  Connected via I2C, which leaves most of the Arduino pins free for sensors.  
  Provides stable current delivery, direction switching (H-bridge), and PWM speed regulation.

- **TOF (VL53L1X) sensors**  
  High-precision time-of-flight distance sensors.  
  Used for multiple tasks:  
  - Front-facing sensor → detects obstacles and prevents collisions.  
  - Side-facing sensors → help keep the robot centered on the track.  
  Compared to ultrasonic sensors, TOF gives millimeter accuracy, faster response, and is less affected by surface angles.

- **Color Sensor (TCS34725)**  
  Detects surface colors and light intensity under the robot.  
  In this project, it is specifically used to **detect and count orange and blue lines** on the track.  
  The sensor provides RGB and clear light readings via I2C, which allows reliable differentiation of these colors even under varying lighting conditions.  
  This functionality is important for lap counting, checkpoints, or special zone recognition.

- **Servo motor (SG90)**  
  Controls the front steering mechanism.  
  Operates based on PWM signals from Arduino.  
  Its range is software-limited to prevent mechanical stress on the steering rack and to ensure consistent accuracy.  

- **DC motor**  
  Provides forward and backward motion for the robot.  
  Controlled via the Motor Shield with PWM for speed regulation.  
  Coupled with a gear reduction system that increases torque and reduces excessive RPM, making motion smoother and controllable.  
  Bearings are used in the drivetrain to minimize friction and improve efficiency.

- **Li-ion batteries**  
  Supply power to the Arduino Mega, Motor Shield, motors, and sensors.  
  Offer high energy density and rechargeability, making them suitable for long operation.  
  Voltage is regulated to ensure safe levels for the electronics.

- **Power bank**  
  Powers the Raspberry Pi Zero 2 independently from the Li-ion battery pack.  
  This prevents voltage drops from the motors from affecting the Pi’s operation.  
  Ensures stable 5V delivery needed for continuous camera and image processing tasks.  

---

## 🔌 Wiring Diagram (described in words)

- **Arduino Mega ↔ Motor Shield V2**: connected via I2C.  
- **DC motor**: connected to Motor Shield output M1.  
- **Servo motor**: connected to Arduino PWM pin (e.g., D9).  
- **TOF sensors**: connected to Arduino via the I2C bus (SDA, SCL). Each sensor uses a different I2C address.  
- **Battery pack**: powers the Arduino Mega and Motor Shield (motors + logic).  
- **Raspberry Pi camera**: connected directly to the Pi camera port.  
- **Raspberry Pi ↔ Arduino**: serial connection for data exchange (camera → Arduino).  
- **Power bank → Raspberry Pi**: provides stable 5V power for the Pi.

---

## 🛠️ Component Selection Justification

- **Arduino Mega**: necessary for handling many simultaneous peripherals (multiple TOF sensors, servo, motor control).  
- **Raspberry Pi Zero 2**: lightweight but powerful enough for computer vision tasks; keeps main logic separate from image recognition.  
- **Motor Shield V2**: reliable I2C-based solution with built-in H-bridges and PWM support.  
- **TOF sensors**: provide far more accurate distance measurements than ultrasonic, crucial for precise navigation.  
- **Servo motor**: precise and responsive steering, avoids drift seen in continuous DC-based steering systems.  
- **DC motor with gear reduction**: balances speed and torque for stable driving.  
- **Li-ion batteries + power bank separation**: ensures that motor-induced voltage drops do not affect the Pi’s sensitive processing.  

---

## 📦 Hardware Expansion Possibilities

- Add **IMU (accelerometer + gyroscope)** for tilt, orientation, and better trajectory control.  
- Integrate **wheel encoders** to track distance traveled and enable closed-loop speed control.  
- Add **current sensors** to monitor motor load and detect stalls or obstacles.  
- Implement **battery monitoring** to warn or stop operation at low voltage.  
- Upgrade to a **Raspberry Pi 4** for advanced real-time vision tasks (object detection, SLAM).  
- Add **wireless communication (Wi-Fi / Bluetooth)** for remote control and debugging.  
