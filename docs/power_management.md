# Power & Sense Management

## Architecture

- **Drive:**  
  2S Li-ion pack (~7.4 V) → Adafruit Motor Shield V2 → DC motor.

- **Logic + vision:**  
  Power bank 5 V → Arduino Mega 2560 + Raspberry Pi Zero 2.

- **Steering servo:**  
  Powered from Arduino 5 V rail.  
  Control via PWM signal from Arduino Mega pin (D8).

- **Sensors:**  
  ToF VL53L1X (3–5 units) and IMU MPU-6050 connected via Arduino I²C.

---

## Power budget

| Subsystem        | Voltage (V) | Nominal current (A) | Peak current (A) |
|------------------|------------:|--------------------:|-----------------:|
| DC motor         | 7.4–12      | 0.4–0.6             | **0.8** |
| Motor Shield V2 (limit) | — | — | **3.0** |
| Arduino Mega 2560 | 5          | 0.07                | 0.10 |
| Raspberry Pi Zero 2 | 5        | 0.35                | 0.8 |
| Steering servo (Arduino 5 V) | 5 | 0.20 | 1.0–1.5 |
| VL53L1X ToF (×3–5) | 5 | 0.06–0.10 | 0.12 |
| IMU MPU-6050      | 3.3–5       | 0.003–0.010         | 0.02 |

---

## Batteries and sources
- **2S Li-ion pack:** ~7.4 V, ≥1500 mAh.  
- **Power bank:** 5 V, must supply at least 2 A.  

---

## Calculations
- **Drive branch:** ~0.7–1.1 A average.  
- **2S 2000 mAh** → about 1.5–2 h runtime.  
- **5 V branch:** ~0.75–1.2 A (Arduino + RPi + servo + sensors).  
- Power bank must reliably provide ≥2 A.  

---

## Monitoring and testing
- **2S voltage:** measured via divider into Arduino ADC.  
- Tests: no-load → straight run → sharp turns → obstacle-stop → 5 min endurance.  

---

## Summary
- Two power sources: 2S Li-ion (drive) and Power bank 5 V (logic, servo, vision).  
- Motor max ~0.8 A (safely below 3 A Motor Shield limit).  
- Servo powered from Arduino 5 V and controlled directly from Arduino PWM pin.  
- Sensors: ToF and MPU-6050 connected via I²C.
