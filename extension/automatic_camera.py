from picamera2 import Picamera2, Preview
from gpiozero import MotionSensor
from time import sleep
import os

user = os.getlogin()
user_home = os.path.expanduser(f'~{user}')

camera = Picamera2()
camera.start()

pir = MotionSensor(17)

try:
    i = 1
    while True:
        if pir.motion_detected:
            camera.capture_file(f'{user_home}/capture%s.jpg' % i)
            print('The number is %s' % i)
            i += 1
        else:
            print('waiting')
            sleep(0.5)
except KeyboardInterrupt:
    camera.stop_preview()
    print('Existing...')
finally:
    pass
