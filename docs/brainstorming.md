# Brainstorming & Idea Generation

## Core Principles: 
- Reliability over speed – better to be a bit slower, but always working 
- Simplicity is key – avoid overly complex solutions 
- Iterative improvement – enhance step by step 
-	Testing over theory – everything is tested in practice 
-	Mistakes = data – failure means learning something new

---	
## 🧠 Initial Ideas

1. **Multi-layer control architecture (SCA model)**
   - Create a multi-layer control system where each layer has its own responsibility:
     - Obstacle layer – obstacle detection  
     - Navigation layer – trajectory planning  
     - Control layer – motor and steering control  

2. **TOF (VL53L1X) sensors**
   - Use multiple accurate “Time-of-Flight” sensors for obstacle detection and distance measurement.  

3. **Motor Shield + DC motors**
   - Control the main driving system with the Adafruit Motor Shield V2.  
   - Ensure sufficient torque and speed.  

4. **Servo mechanism**
   - Use a servo for steering or moving an additional sensor.  
   - Allows more flexible obstacle analysis.  

5. **PD control**
   - Apply proportional-derivative control for speed and steering.  
   - Ensure smooth driving without sudden deviations.  

6. **AceSorting algorithms**
   - Use an algorithm library for optimization, e.g., decision logic or sensor data processing.  

---

## ⚖️ Comparison of Alternatives

| Idea | Advantages | Disadvantages |
|------|------------|---------------|
| Camera only (computer vision) | Can recognize signs, advanced analysis | Strongly depends on lighting, complex AI model |
| Ultrasonic sensors only | Simple and cheap | Low accuracy, sensitive to reflections |
| IMU only | Provides additional data for turns | Drift over longer distances |
| Hybrid solution (TOF+PD) | Reliability, fault tolerance | Higher complexity, requires more testing |

---

## ✅ Chosen Solution

We chose a **hybrid solution with multi-layer architecture**, which includes:  

- TOF sensors for obstacle detection  
- PD control for trajectory and speed  
- Servo mechanism for steering control  
- Motor Shield + DC motors  
- AceSorting algorithms for data logic  

This combination covers the weaknesses of single-technology approaches and ensures reliable performance on the WRO track.  

---

## 🔄 Rejected Ideas Justification

- **Camera** – rejected due to strong dependence on lighting.  
- **Ultrasonic sensors** – rejected due to limited accuracy.  
- **IMU** – rejected due to accumulated drift errors.  
