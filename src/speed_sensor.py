from gpiozero import LED, Button
from signal import pause

# Initialize GPIO pins for the speed sensor and LEDs 
# speed sensor = ss
ss = Button(17, pull_up=False)
# green led = gl, red led = rl
gl = LED(27)
rl = LED(22)

def update_leds():
    
    if ss.is_pressed:
        gl.off()
        rl.on()
        print('light was blocked')
    else:
        gl.on()
        rl.off()

try:
    while True:
        ss.when_pressed = update_leds
        ss.when_released = update_leds

except KeyboardInterrupt:
    print('Existing...')
finally:
    pass
