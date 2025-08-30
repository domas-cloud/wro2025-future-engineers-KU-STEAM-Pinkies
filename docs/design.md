# 🛠️ Mechanical Design

## 🚗 Chassis Structure

The car chassis is designed to ensure:
- Stable driving on straight sections and in turns.  
- Sufficient space for electronics and wiring.  
- Optimal weight balance between the front and rear axles.  

The main construction is based on a **layered plywood (“stacking”) system** – this allows creating multiple levels for electronics while keeping the structure lightweight but strong.  

---

## 🔧 Component Layout

- **DC motor with gear reduction** mounted at the rear.  
  - 3D-printed gear reducers increase torque and reduce speed for more stable driving.  

- **Steering mechanism with servo** uses a **rack-and-pinion gear system** (3D-printed).  
  - The servo’s rotary motion is converted into linear rack motion.  
  - Ensures precise and durable steering compared to direct servo mounting.  

- **Arduino Mega** placed in the center of the chassis to minimize cable lengths.  

- **Batteries** located close to Arduino for compact wiring.  

---

## 📡 Sensor Placement Variants

### Variant A – Without IMU (5× ToF sensors)
- **Front ToF** – obstacle detection.  
- **Four side ToFs** (two on each side) – wall-following and angle measurement.  
- Purely geometric control from multiple distance points.  

### Variant B – With IMU (3× ToF + IMU)
- **Front ToF** – obstacle detection.  
- **Two side ToFs** (front + rear on one side) – Δx calculation for wall alignment.  
- **IMU** – provides yaw/orientation for turns, compensates for fewer ToFs.  
- Same **PD algorithm**, but input data comes from ToFs + IMU fusion.  

---

## 🛠️ Design Rationale

- The **plywood stacking system** provides flexibility – layers can be reconfigured quickly.  
- **3D-printed gear reducers** allow torque customization per track.  
- **Rack-and-pinion steering** ensures reliability and prevents servo overload.  
- **Lower center of gravity** improves stability in sharp turns.  
- **Modular layout** makes it easy to swap faulty sensors (as proven by IMU fallback integration).  

---

## 🔮 Future Development Opportunities

- Create a **protective 3D-printed body shell** to safeguard electronics.  
- Upgrade the **gear rack system** with metal parts for long-term durability.  
- Integrate a **suspension system** for tracks with uneven surfaces.  
- Add **mounting slots for spare sensors**, so replacement in emergencies is quicker.  

---

