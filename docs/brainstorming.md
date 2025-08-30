# 🧠 Brainstorming & Idea Generation

## Core Principles
- Reliability over speed – better to be a bit slower, but always working.  
- Simplicity is key – avoid overly complex solutions.  
- Iterative improvement – enhance step by step.  
- Testing over theory – everything is tested in practice.  
- Mistakes = data – failure means learning something new.  

---

## 💡 Initial Ideas

1. **Multi-layer control architecture (SCA model)**  
   - Obstacle layer – obstacle detection.  
   - Navigation layer – trajectory planning.  
   - Control layer – motor and steering control.  

2. **TOF (VL53L1X) sensors**  
   - Multiple accurate Time-of-Flight sensors for obstacle detection and distance measurement.  

3. **Motor Shield + DC motors**  
   - Adafruit Motor Shield V2 for motor control.  
   - Ensure sufficient torque and speed.  

4. **Servo mechanism**  
   - Servo for steering (front axle).  
   - Possibility to move an additional sensor if needed.  

5. **PD control**  
   - Proportional-Derivative control for stable steering.  
   - Smooth driving without sudden deviations.  

6. **AceSorting algorithms**  
   - Library-based data logic for decision-making.  

---

## ⚖️ Comparison of Alternatives

| Idea                         | Advantages                           | Disadvantages                       |
|------------------------------|--------------------------------------|-------------------------------------|
| Camera only (computer vision)| Can recognize signs, advanced analysis | Strongly depends on lighting, requires heavy computing |
| Ultrasonic sensors only      | Simple and cheap                     | Low accuracy, sensitive to reflections |
| IMU only                     | Provides yaw and orientation         | Drift over long distances, needs correction |
| Hybrid solution (TOF + PD)   | Reliable, fault tolerant             | Higher complexity, more testing required |

---

## ✅ Chosen Solution

We chose a **hybrid solution with multi-layer architecture**, including:  
- TOF sensors for obstacle detection.  
- PD control for trajectory and speed.  
- Servo mechanism for steering.  
- Motor Shield + DC motors.  
- AceSorting algorithms for data processing.  

This covers the weaknesses of single-technology approaches and ensures reliable performance on the WRO track.  

---

## 🔄 Rejected Ideas Justification

- **Camera** – rejected due to lighting dependence.  
- **Ultrasonic sensors** – rejected due to accuracy issues.  
- **IMU** – initially rejected due to drift errors.  

---

## 🔁 Decision Update (Competition Reality)

Three days before the competition, **two ToF sensors burned out**.  
- Original design: 5× ToFs.  
- Emergency fallback: **3× ToFs + IMU**.  

**Key points:**  
- The **core PD algorithm did not change** – only sensor inputs were updated.  
- Side wall-following still uses two ToFs.  
- IMU yaw compensates for reduced ToF coverage and stabilizes turns.  
- Robot remained functional and competition-ready.  

👉 Lesson learned: sometimes a **previously rejected idea (IMU)** becomes critical when hardware fails. Flexibility is as important as the initial design.  
