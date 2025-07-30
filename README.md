# 🤖   - WRO 2025 Future Engineers: KU STEAM Pinkies
## 📚 Table of Contents
- [Team Introduction](#team-introduction)
- [Ideas and Principles](#ideas-and-principles)
- [Robot Movement Control](#robot-movement-control)
- [Power and Sensor Management](#power-and-sensor-management)
- [Obstacle Avoidance](#obstacle-avoidance)
- [Encountered Problems and Solutions](#encountered-problems-and-solutions)
- [Robot Construction](#robot-construction)
- [Robot Control Architecture](#robot-control-architecture)
- [Electronics Wiring Diagram](#electronics-wiring-diagram)


WRO Future Engineers documentation 
Team Name: KU STEAM Pinkies
Project Title:   
## Team Introduction
We are **KU STEAM Pinkies**, a passionate group of young engineers with a shared vision:  
To build a reliable and fully autonomous robot capable of navigating real-world environments.

**Team Members & Roles:**
- **Marius** – Programmer
- **Domas** – Electronics Specialist
- **Jonas** – Mechanical Designer
  
By combining our individual strengths, responsibilities, and teamwork, we were able to design, build, and refine a reliable autonomous car ready for competition. 

**Our Goal:** 
 To create an autonomous, environment-aware robot that can move and make decisions independently, efficiently avoiding obstacles in real time.
 
## Ideas and Principles
This was one of the most complex projects we’ve worked on. We followed several guiding rules and ideas that helped us make decisions quickly and efficiently. 
**Core Principles:** 
- Reliability over speed – better to be a bit slower, but always working 
- Simplicity is key – avoid overly complex solutions 
- Iterative improvement – enhance step by step 
-	Testing over theory – everything is tested in practice 
-	Mistakes = data – failure means learning something new
   
**Effective Ideas:** 
-	Switched from ultrasonic to TOF for more stable side detection 
-	Used PID control for smooth turning 
-	3D printed mounts for fast design changes 
-	Kept code structured: sensor reading, decision-making, and action execution separated 
-	Built the frame from plywood for strength without excess weight 
-	Tested under real conditions – recreated the map at home for accuracy 

## Robot Movement Control
The robot moves using a single-motor drive powering the rear wheels. The direction is controlled using a gear and rack mechanism that adjusts the angle of the front axle wheels. A servo motor, controlled via a PWM signal, allows precise steering adjustments. 
To ensure stable movement parallel to a wall, two TOF (Time-of-Flight) sensors are mounted on the same side: 
•	x₁ – front (beam AA₁) 
•	x₂ – rear (beam BB₁) 
Important: Beams AA₁ and BB₁ are parallel because both TOF sensors are mounted parallel to each other, perpendicular to the robot's chassis. This allows precise estimation of: 
•	Whether the robot is angled relative to the wall (Δx) Control is based on two differences: 
•	Δx = x₂ − x₁ (angular tilt) 
•	Δd = d₁ − d₂ (distance difference from the wall) 
Δx is used to correct the angle – if the front distance is smaller than the rear (or vice versa), the robot isn't parallel to the wall. The system adjusts the front axle angle until Δx ≈ 0. 
To avoid sudden and uncontrolled turns that could cause instability, the turning angle of the front axle is adjusted gradually using a simple PID (Proportional–Integral–Derivative) control algorithm. 
PID logic ensures that: 
•	Reactions to errors (Δx or Δd) are proportional to their size 
•	No sudden jumps – angle changes gradually depending on the rate of change 
•	Long-term deviations are corrected smoothly, even if sensor data briefly fluctuates 
As a result, the robot moves smoothly, without overloading the steering mechanism or jumping between trajectories. 
This control allows the robot to: 
•	Maintain a smooth, straight trajectory 
•	Avoid colliding with walls 
•	Move safely even in narrow paths 
<img width="600" height="616" alt="image" src="https://github.com/user-attachments/assets/b2d9ebfe-193c-45cf-9ac2-bdeeccee2a55" />

## Power and Sensor Management

## Obstacle Avoidance

## Encountered Problems and Solutions

## Robot Construction

## Robot Control Architecture

## Electronics Wiring Diagram




