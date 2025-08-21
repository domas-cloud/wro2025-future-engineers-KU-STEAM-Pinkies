# 📊 Evaluation

## ✅ Achievements
- Successfully integrated **Arduino Mega** with **Raspberry Pi Zero 2**, enabling real-time communication between camera processing and low-level control.  
- Implemented **TOF VL53L1X sensors** for accurate obstacle detection and trajectory maintenance.  
- Added a **Color Sensor (TCS34725)** that reliably detects and counts **orange and blue lines** for lap/checkpoint counting.  
- Developed a **rack-and-pinion steering system** driven by a servo, designed to avoid skew and prevent gear tooth skipping.  
- Implemented a **gear reduction drivetrain with bearings**, reducing friction while increasing torque for stable movement.  
- Created a **multi-level frame** that allows easy maintenance and compact assembly.  
- Designed and documented a complete hardware & software workflow, with clear repository structure and build instructions.

---

## ⚠️ Challenges & Limitations
- **Servo torque limitation**: the SG90 servo sometimes struggles under load, reducing steering precision at higher speeds.  
- **Camera processing**: the Raspberry Pi Zero 2 has limited performance, making advanced image recognition difficult in real time.  
- **Lighting conditions**: the color sensor is sensitive to changes in ambient light, which may affect orange/blue line detection.  
- **Battery management**: currently no automatic voltage monitoring – sudden drops can cause resets or unstable performance.  
- **PID/PD tuning**: requires manual calibration per environment; not yet fully adaptive.  

---

## 💡 Lessons Learned
- Precise **mechanical design** (using bearings and correct gear ratios) significantly improves drivetrain reliability.  
- **Sensor fusion** is critical: combining TOF sensors with color detection provides much more robust navigation than using a single sensor type.  
- Splitting computation between **Arduino (real-time tasks)** and **Raspberry Pi (vision tasks)** is effective, but requires careful communication handling.  
- Documentation and version control (with submodules) save time and make the project easier to share with the team.

---

## 🚀 Future Improvements
- Upgrade the steering servo to a **higher-torque model** for more reliable control.  
- Replace the Raspberry Pi Zero 2 with a **Raspberry Pi 4** (or similar) for faster image processing and potential AI vision features.  
- Implement **adaptive PID control**, allowing the robot to auto-tune its parameters in different track conditions.  
- Add **IMU sensors (gyroscope + accelerometer)** for better orientation tracking.  
- Introduce **battery voltage monitoring** with automatic safe shutdown.  
- Optimize **color sensor calibration** by adding dynamic lighting compensation.  
- Improve modularity of the codebase for easier debugging and testing.  

---

## 🎯 Conclusion
Overall, our project demonstrates a **well-balanced integration of mechanical, electronic, and software systems**.  
Despite hardware and computational limitations, the robot is capable of autonomous navigation, obstacle avoidance, and line counting.  
We identified clear improvement areas and defined concrete next steps, which will guide the team toward building a more **robust, reliable, and competition-ready robot** for WRO 2025 Future Engineers.
