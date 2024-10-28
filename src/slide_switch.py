from gpiozero import LED, Button
from time import sleep

# initialize the slide switch on GPIO pin 17 
ss = Button(17, pull_up=False)
l1 = LED(22)
l2 = LED(27)

try:
    while True:
        if ss.is_pressed:
            print('led1 on')
            l1.on()
            l2.off()
        else:
            print('led2 on')
            l1.off()
            l2.on()
        sleep(0.5)
except KeyboardInterrupt:
    print('Existing...')
finally:
    pass