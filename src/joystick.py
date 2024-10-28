from gpiozero import Button
import ADC0834
from time import sleep

# Initialize the button connected to GPIO pin 22
# Button Pin = bp
bp = Button(22)

ADC0834.setup()

try:
    while True:
        # x value = x, y value = y
        x = ADC0834.getResult(0)
        y = ADC0834.getResult(1)
        
        # button value = bv
        bv = bp.value
        print(f'X: {x}, Y: {y}, Btn: {bv}')
        sleep(0.2)
except KeyboardInterrupt:
    print('Existing...')
finally:
    pass
