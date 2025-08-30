# Encountered Problems and Solutions

## Burned ToF Sensors Before Competition
**Problem:**  
Three days before the competition, two of our VL53L1X ToF sensors burned out due to wiring or power instability. Our original plan relied on 5 ToFs for precise wall-following and obstacle detection.

**Solution:**  
- Reconfigured the system to work with **3 ToFs** only (two on the side, one in the front).  
- Integrated **IMU data (gyroscope + accelerometer)** to support orientation and turning.  
- Updated the control algorithm:  
  - Side alignment (Δx) still calculated from the two side ToFs.  
  - Yaw stability and smoother turning compensated with IMU feedback.  

**Result:**  
Robot remained functional and competition-ready. Even though distance precision decreased slightly, IMU fusion gave us reliable performance and smoother turns.

---

## Sensor Addressing Conflicts
**Problem:**  
When using multiple VL53L1X sensors on the same I²C bus, we encountered address conflicts.  
Sometimes sensors would not respond correctly or give inconsistent readings.

**Solution:**  
- Implemented sensor initialization sequence to set unique I²C addresses for each ToF.  
- Added error-handling logic to re-initialize sensors if no data was received.  

**Result:**  
Stable multi-ToF operation without random dropouts.

---

## Power Spikes on Servos
**Problem:**  
During sharp turns, the steering servo caused voltage dips that interfered with sensors and even reset the controller.  

**Solution:**  
- Added a separate BEC regulator for the servo.  
- Introduced capacitors for smoothing.  

**Result:**  
No more brownouts; reliable operation under full load.

---

## Limited Testing Time
**Problem:**  
Due to hardware failures and late fixes, we had limited time to test the robot on a real track.  

**Solution:**  
- Focused on critical test cases: sharp turns, obstacle avoidance, and recovery.  
- Logged data from each run and adjusted PD parameters iteratively.  

**Result:**  
Despite reduced testing, the robot performed consistently within competition rules.

---

# Lessons Learned
- Always have spare critical sensors/components.  
- IMU can successfully compensate for missing distance sensors.  
- Power management is crucial for reliable operation.  
- Systematic logging and quick iteration allow recovery even under time pressure.
