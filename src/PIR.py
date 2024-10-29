from gpiozero import RGBLED, MotionSensor
from time import sleep

led = RGBLED(red=18, green=27, blue=22)
pir = MotionSensor(17)

try:
    while True:
        if pir.motion_detected:
            led.color = (1,1,0)
        else:
            led.color = (0,0,1)
        sleep(0.1)
except KeyboardInterrupt:
    print('Existing...')
finally:
    pass
