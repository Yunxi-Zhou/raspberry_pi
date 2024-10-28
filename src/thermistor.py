import ADC0834
from time import sleep
import math

ADC0834.setup()

try:
    while True:
        analogVal = ADC0834.getResult()
        
        # convert the analog value to a voltage
        vr = 5 * float(analogVal) / 255
        # cal the resistance of thermistor
        rt = 10000 * vr / (5 - vr)
        # cal the temp in Kelvin
        temp = 1 / (((math.log(rt / 10000)) / 3950) + (1 / (273.15 + 25)))
        # Convert Kelvin to C
        cel = temp - 273.15
        # Convert C to F
        fah = cel * 1.8 + 32
        print(f'C: {cel}, F: {fah}')
        
        sleep(0.2)
except KeyboardInterrupt:
    print('Existing...')
    ADC0834.destroy()
finally:
    pass

        
        