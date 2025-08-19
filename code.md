# Software Idea and Implementation

## 🧠 Main Idea

The goal of our code is to ensure that the car drives stably, can detect obstacles, and adapts to the track shape.  
For this, we use a **three-layer architecture**: obstacle detection, navigation, and control.  

---

## 🔑 Step-by-Step Code Flow

1. **Sensor Reading**  
   In the main loop, the program first reads the TOF sensors.  
   If one sensor returns an invalid value, the program assigns a maximum distance so that a faulty signal does not cause sudden braking.  

   The car always first “looks at the environment,” checks the front and side distances, and only then makes decisions.  

---

2. **Error Calculation**  
   The measured data is compared to the desired distance from the wall or the center of the track.  
   The difference (error) shows how much the car has deviated.  

   If the car is too close to the wall – the error is positive; if too far – it is negative. This error becomes the main indicator used to adjust the steering.  

---

3. **PD Control Algorithm**  
   The control signal consists of:  
   - **Proportional part** (how much the car has deviated),  
   - **Derivative part** (how quickly that deviation is changing).  

   The program not only sees *how much* the car deviates from the track, but also *how fast* it happens. This prevents oscillation from side to side.  

---

4. **Steering Servo Control**  
   The PD algorithm outputs a value that is converted into the steering angle.  
   If the error is large – the steering is adjusted more strongly, if small – just slightly.  

   The car “turns the wheel” just enough to return to the trajectory.  

---

5. **Motor Update**  
   The motors are controlled through the Motor Shield.  
   If the sensors show a clear path – a base speed is maintained.  
   If there is an obstacle ahead – the motors are stopped or slowed down.  

   At every moment, the car decides whether to “keep driving,” “slow down,” or “stop.”  

---

6. **Obstacle Detection Logic**  
   If the front sensor shows a distance smaller than safe, the car stops.  
   If the obstacle is only on the left – the car turns right, and vice versa.  

   The car can decide whether it is better to stop or to go around the obstacle.  

---

## 💬 Additional Logic

- If all sensors return faulty data – the car stops in a safety mode.  
- If the PD controller outputs a value that is too large – it is limited so that the servo does not go beyond physical limits.  
- If there are no obstacles on the track – the car returns to a “base driving” mode.  

The program has “safety checks” to make sure the car always behaves predictably, even if the sensors or algorithms provide imperfect data.  

---

## 🔮 Future Improvements

- An integral part could be added (full PID control) to reduce long-term errors.  
- Machine learning could be used to let the car optimize Kp and Kd values by itself.  

---

## ✅ Summary

Our program works as follows:  
- The car **first observes the environment** (sensors).  
- Then it **evaluates whether it is driving correctly** (error).  
- Finally, it **adjusts its movement** (servo and motors).  

The whole system works like a human – first looking, then deciding, and finally turning the wheel and adjusting speed.  
