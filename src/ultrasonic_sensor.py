from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=24, trigger=23)

try:
    while True:
        dis = sensor.distance * 100
        print('Distance: {:.2f} cm'.format(dis))
        sleep(0.3)

except KeyboardInterrupt:
    print('Existing...')
finally:
    pass
