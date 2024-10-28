from gpiozero import LED, Button
from time import sleep

# ts: touch sensor
ts = Button(17, pull_up=False)

# l1 = led 1, l2 = led 2
l1 = LED(22)
l2 = LED(27)

try:
    while True:
        if ts.is_pressed:
            print('touch the touch sensor')
            l1.off()
            l2.on()
        else:
            print('remove the touch sensor')
            l1.on()
            l2.off()
        sleep(0.5)
except KeyboardInterrupt:
    print('Exsiting...')
finally:
    pass

