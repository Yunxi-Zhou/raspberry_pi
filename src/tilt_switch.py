from gpiozero import LED, Button

# title pin = tp, blue light = bl, red light = rl
tp = Button(17, pull_up=False)
bl = LED(27)
rl = LED(22)

def detect():
    if tp.is_pressed:
        print('tilt')
        rl.on()
        bl.off()
    else:
        rl.off()
        bl.on()

try:
    while True:
        tp.when_pressed = detect
        tp.when_released = detect
except KeyboardInterrupt:
    print('Existing...')
finally:
    pass        