# Mechanical Design

## 🚗 Chassis Structure

The car chassis is designed to ensure:
- Stable driving on straight sections and in turns.  
- Sufficient space for electronics and wiring.  
- Optimal weight balance between the front and rear axles.  

The main construction is based on a **layered plywood (“stacking”) system** – this allows creating multiple levels for electronics while keeping the structure lightweight but strong.  

---

## 🔧 Component Layout

- **DC motors** are mounted at the rear, with an additional **gear reduction system**.  
  - 3D-printed gear systems are used, which allow:  
    - increasing torque,  
    - reducing speed for more stable driving.  

- **Steering mechanism with servo** uses a **gear rack** system, 3D-printed for precision.  
  - The servo movement is converted into linear motion that turns the wheels.  
  - This ensures more accurate and durable steering compared to direct servo mounting.  

- **TOF sensors**:  
  - one in the front – for obstacle detection,  
  - two on the sides – for trajectory control.  

- **Arduino Mega** is mounted in the central area, so the wiring to motors and sensors is as short as possible.  

- **Batteries** are mounted close to the Arduino to minimize wiring length.  

---

## 🛠️ Design Rationale

- The **plywood stacking system** provides flexibility – extra layers can be added for sensors or batteries.  
- **3D-printed gear reducers** allow torque adjustment depending on track requirements, reducing motor load.  
- The **gear rack steering system** provides much higher reliability and precision than direct servo turning.  
- **Lowering the center of gravity** reduces the risk of flipping during turns.  
- **Modular design** – components are mounted in a way that makes them easy to replace or upgrade.  

---

## 🔮 Future Development Opportunities

- Create a **fully enclosed 3D-printed body** to protect electronics from impacts.  
- Implement a **higher-precision gear system** with bearings to reduce friction.  
- Upgrade the **rack-and-pinion system** using metal gears for durability.  
- Add a **suspension system with shock absorbers** for uneven surfaces.  

---
