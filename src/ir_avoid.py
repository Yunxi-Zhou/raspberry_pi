from gpiozero import Button
from time import sleep

obstacle_sensor = Button(17, pull_up=True)

try:
    while True:
        if obstacle_sensor.is_pressed:
            print('touch the obstacle')
            sleep(1)
except KeyboardInterrupt:
    print('Existing...')
finally:
    pass
