from gpiozero import PWMLED
import ADC0834
from time import sleep

led = PWMLED(22)

ADC0834.setup()

def MAP(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def loop():
    while True:
        analogVal = ADC0834.getResult()
        print(f'value = {analogVal}')
        
        led.value = float(analogVal/255)
        sleep(0.2)
        
try:
    loop()
except KeyboardInterrupt:
    print('Existing...')
finally:
    pass