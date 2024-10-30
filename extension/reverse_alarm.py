import LCD1602
from time import sleep
from gpiozero import DistanceSensor, Buzzer

sensor = DistanceSensor(echo=24, trigger=23)

buzzer = Buzzer(17)

def lcdsetup():
    LCD1602.init(0x27, 1)
    LCD1602.clear()
    LCD1602.write(0,0,'Ultrasonic Starting')
    LCD1602.write(1,1,'By Ethan')
    sleep(2)

def distance():
    dis = sensor.distance * 100
    print('Distance: {:.2f} cm'.format(dis))
    sleep(0.3)
    return dis

def loop():
    while True:
        dis = distance()
        if dis > 400:
            LCD1602.clear()
            LCD1602.write(0, 0, 'Error')
            LCD1602.write(3, 1, 'Out of range')
            sleep(0.5)
        else:
            LCD1602.clear()
            LCD1602.write(0, 0, 'Distance is')
            LCD1602.write(5, 1, str(round(dis, 2)) + ' cm')
            if dis >= 50:
                sleep(0.5)
            elif 20 < dis < 50:
                for _ in range(2):
                    buzzer.on()
                    sleep(0.05)
                    buzzer.off()
                    sleep(0.2)
            elif dis < 20:
                for _ in range(5):
                    buzzer.on()
                    sleep(0.05)
                    buzzer.off()
                    sleep(0.05)

try:
    lcdsetup()
    loop()
except KeyboardInterrupt:
    buzzer.off()
    print('Existing...')
finally:
    LCD1602.clear()
    pass
