from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(18)

def buttonOn():
    button.when_pressed = led.on
    button.when_released = led.off
    pause()

try:
    buttonOn()
except KeyboardInterrupt:
    print('Existing...')
finally:
    pass