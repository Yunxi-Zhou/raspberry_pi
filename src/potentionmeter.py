from gpiozero import PWMLED
import ADC0834
import time

led = PWMLED(22)

ADC0834.setup()

def MAP(x, in_min, in_max, out_min, out_max):
    
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

try:
    while True:
        res = ADC0834.getResult()
        print('res = %d' % res)
        
        R_val = MAP(res, 0, 255, 0, 100)
        led.value = float(R_val / 100)
        
        time.sleep(0.5)

except KeyboardInterrupt:
    led.value = 0