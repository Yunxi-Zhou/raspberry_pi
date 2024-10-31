from picamera2 import Picamera2, Preview
from gpiozero import LED, Button
from time import sleep
import os

user = os.getlogin()
user_home = os.path.expanduser(f'~{user}')

# Initialize the camera
camera = Picamera2()
camera.start()

# Initialize a variable to track the camera's status
global status
status = False

led = LED(17)
button = Button(18)

def takePhotos(pin):
    global status
    status = True

try:
    button.when_pressed = takePhotos
    
    while True:
        if status:
            for i in range(5):
                led.on()
                sleep(0.1)
                led.off()
                sleep(0.1)
            camera.capture_file(f'{user_home}/my_photo.jpg')
            print('Take a photo!')
            status = False
        else:
            led.off()
        sleep(1)
except KeyboardInterrupt:
    camera.stop_preview()
    led.off()
    print('Existing...')
finally:
    pass