# Testing

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

## 🔮 Next Steps

- More precise PD tuning in different track conditions.  
- Improvement of obstacle avoidance algorithms.  
- Automatic adaptation of Kp and Kd values based on speed.  
