# 🗓️ Planning

## 📅 Project Timeline

| Phase | Description | Responsible |
|-------|-------------|-------------|
| 1. Problem definition | Define project goals and success criteria | Domas |
| 2. Idea generation | Create and compare multiple ideas | Whole team |
| 3. Design and CAD models | Draw sketches, 3D models, wiring diagrams | Marius, Jonas |
| 4. Hardware assembly | Assemble motors, sensors, and electronics | Jonas |
| 5. Programming | Develop control architecture, implement PD control | Marius |
| 6. Testing and iterations | Perform tests, collect data, improve system | Domas |
| 7. Final evaluation | Verify against goals and WRO rules | Whole team |
| 8. Documentation | Complete engineering journal, GitHub documentation | Domas |
| 9. Emergency adaptations | React to unexpected hardware failures (e.g. fallback to IMU) | Whole team |

---

## 📦 Resource Planning

### Hardware
- Arduino Mega 2560  
- Adafruit Motor Shield V2  
- TOF (VL53L1X) sensors (originally 5 planned, fallback with 3)  
- IMU (gyro + accelerometer) – integrated after ToF failures  
- Servo motor for steering  
- DC motor  
- Li-ion battery pack  

### Software & Tools
- Arduino IDE / PlatformIO  
- GitHub for version control and documentation  
- CAD software for mechanical and wiring diagrams  
- Logging/plotting tools for test data analysis  

---

## 👥 Team Task Distribution

- **Marius – Programmer and Mechanical Designer**  
  Coding, PD control implementation, CAD design, IMU integration.  

- **Domas – Manager, Marketing and Testing**  
  Project coordination, testing (including emergency fallback testing), documentation, communication.  

- **Jonas – Electronics Specialist and Designer**  
  Electronics assembly, ToF wiring, IMU addition, sensor calibration, power management solutions.  

---

## 🎯 Milestones

- **M1** – Problem clearly defined and documented  
- **M2** – First prototypes tested (5× ToF configuration)  
- **M3** – Stable driving system with obstacle detection  
- **M4** – *Emergency adaptation:* 3× ToF + IMU configuration validated before competition  
- **M5** – Final tests completed  
- **M6** – Full documentation submitted  

---

## ⚠️ Risk Management 

- Always prepare **spare sensors/components**.  
- Define a **fallback plan** (e.g. replace missing ToFs with IMU input).  
- Allocate time for **unexpected hardware failures** close to competition.  
