# 🧪 Testing

## 🎯 Testing Goals
- Evaluate the car's stability when driving on straight sections and in turns.  
- Verify the obstacle detection system and reaction time.  
- Tune the PD control parameters (Kp, Kd).  
- Ensure that the car complies with WRO rules.  

---

## 🧪 Test Scenarios

1. **Straight Line Test**  
   - Goal: evaluate if the car drives stably without oscillation.  
   - Expected result: deviation ≤ 5 cm from the track center.  

2. **90° Turn Test**  
   - Goal: check steering servo response and PD control in corners.  
   - Expected result: smooth turn without stopping.  

3. **Front Obstacle Detection Test**  
   - Goal: ensure the car stops in front of an obstacle.  
   - Expected result: stop ≤ 10 cm from the obstacle.  

4. **Side Obstacle Detection Test**  
   - Goal: verify that the car can avoid an obstacle.  
   - Expected result: turn to the opposite side while keeping trajectory.  

5. **Long-Term Driving Test**  
   - Goal: observe battery performance, sensor stability, and PD error accumulation.  
   - Expected result: the car maintains stable driving for at least 5 minutes.  

---

## 📊 Collected Data

- Sensor reading accuracy (mm).  
- Reaction time to obstacles (ms).  
- Maximum and average trajectory deviation (mm).  
- Energy consumption (battery runtime).  

---

## 🔄 Iterations

- Kp value decreased to reduce oscillation.  
- Kd value increased to improve cornering stability.  
- Safety limits added to restrict servo turning angle.  
- Implemented filtering of faulty sensor readings.  

---

## ✅ Results

- The car drives stably on straight sections.  
- Additional PD tuning required in corners.  
- Front obstacles detected reliably, stopping distance ~8 cm.  
- Obstacle avoidance logic still under testing.  

---

## 🧭 IMU + ToF Fallback Testing

When two ToF sensors failed shortly before the competition, the system was adapted to use **3 ToFs + IMU**.  
Additional tests were carried out to ensure stability:  

- **Sharp Turn Test with IMU**  
  - Goal: verify if IMU yaw helps smoother turning.  
  - Result: robot showed reduced oscillation compared to ToF-only setup.  

- **Stability Under Reduced Sensors**  
  - Goal: confirm that the PD algorithm still works with fewer distance sensors.  
  - Result: stable driving achieved, algorithm unchanged, only inputs adapted.  

- **Competition Simulation Run**  
  - Goal: full track drive with fallback configuration.  
  - Result: reliable driving, checkpoints detected, obstacle stop worked as expected.  

**Lesson learned:** IMU significantly improves stability when ToF coverage is reduced, and having a fallback plan was crucial for competition readiness.  

---

## 🔮 Next Steps

- More precise PD tuning in different track conditions.  
- Improvement of obstacle avoidance algorithms.  
- Automatic adaptation of Kp and Kd values based on speed.  
