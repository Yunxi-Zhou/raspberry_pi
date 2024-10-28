from gpiozero import RotaryEncoder, Button
from time import sleep

encoder = RotaryEncoder(a=17, b=18)
button = Button(27)

global_counter = 0

def rotary_change():
    global global_counter
    global_counter += encoder.steps
    encoder.steps = 0
    print(f'Global Counter = {global_counter}')

def reset_counter():
    global global_counter
    global_counter = 0
    print('Counter reset')

button.when_pressed = reset_counter

try:
    while True:
        
        sleep(0.5)
except KeyboardInterrupt:
    print('Existing...')
finally:
    pass
