import serial, math, platform

name = '/dev/cu.usbmodem101'
if platform.system() == 'Windows':
    name = "COM4"

ser = serial.Serial(name, 115200)

INITIAL_ANGLE = 100
DISTANCE_BETWEEN_SENSORS = 30
MAX_TURNING_ANGLE = 16
TURNING_SIDE_ANGLE = 30

# Kooeficieintai skirti PID
PROPORTIONAL_VALUE = 0.7
DERIVATIVE_VALUE = 0.6
INTEGRAL_VALUE = 0.05

last_value = 0
turning_angle = 0

# Nekartojame jau isiustu reiksmiu
last_sended_angle = 0
total_error = 0
turns = 0

def resetValues():
    global last_value, total_error, timeCounting, turning_angle
    last_value = 0
    total_error = 0
    timeCounting = 0
    turning_angle = 0

def writeData():
    global last_sended_angle, turning_angle
    rot = INITIAL_ANGLE + round(turning_angle)
    if last_sended_angle != rot:
        ser.write(bytes(f"Rotate,{rot}\n", 'utf-8'))
        last_sended_angle = rot

following_left = False
following_wall = True
engineOn = False
timeCounting = 0

while True:
    try:
        string = str(ser.readline())
    except:
        string = ""


    data = string.replace("b'", "").replace("\\n'", '').replace("'", "").split(',')
    # Stabilizatorius, kad sektu pagal trumpiausia siena
    if len(data) == 5:
        f_front = int(float(data[0]))
        f_left = int(float(data[1])) / 10 
        f_right = int(float(data[2])) / 10
        side_left = int(float(data[3])) / 10
        side_right = int(float(data[4])) / 10

        y = (f_right - side_right)

        if following_left:
            y = (f_left - side_left)
        
        angle = math.atan( (y or 1) / DISTANCE_BETWEEN_SENSORS)
        if not following_left:
            angle = math.pi / 2 - angle

        distance = f_right * math.cos(angle)

        if following_left:
            distance = f_left * math.cos(angle)
        
        # Atstumas tarp sienu
        distance_sum = (f_left + f_right) * math.cos(angle)

        if following_wall:
            # PI Controller

            # Stengiasi vaziuoti viduryje tarp sienu
            error = distance - (distance_sum / 2)
            total_error += error

            if abs(error) < 6:
                total_error = 0

            if last_value == 0:
                last_value = error
            
            derivative_angle = (error - last_value) * DERIVATIVE_VALUE
        
            turning_angle = PROPORTIONAL_VALUE * error + derivative_angle + total_error * INTEGRAL_VALUE

            if not following_left:
                turning_angle /= 1

            if abs(turning_angle) > MAX_TURNING_ANGLE:
                if turning_angle < 0:
                    turning_angle = -MAX_TURNING_ANGLE
                else:
                    turning_angle = MAX_TURNING_ANGLE

            last_value = error


        print(data,f_left, f_right, f_front, distance_sum)

        if f_front < 90 :
            # sukames
            following_wall = False
            print('turning', timeCounting)
            timeCounting += 1

            if timeCounting > 4:
                turns += 1

            if f_left > f_right:
                turning_angle = TURNING_SIDE_ANGLE
            else:
                turning_angle = -TURNING_SIDE_ANGLE

        elif not following_wall:
            following_wall = True
            resetValues()

    match data[0]:
        case "STOP":
            engineOn = False
        case "START":
            resetValues()
            engineOn = True
        
    if not engineOn:
        turning_angle = 0

    writeData()
