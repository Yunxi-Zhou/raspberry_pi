from gpiozero import LED, Button

reed_switch = Button(17, pull_up=True)

# green led = gl, red led = rl
gl = LED(27)
rl = LED(22)

def update_leds():
    if reed_switch.is_pressed:
        print('magnetic field')
        gl.off()
        rl.on()
    else:
        gl.on()
        rl.off()

try:
    gl.on()
    while True:
        reed_switch.when_pressed = update_leds
        reed_switch.when_released = update_leds
except KeyboardInterrupt:
    gl.off()
    rl.off()
    print('Existing...')
finally:
    pass