from gpiozero import LED
from time import sleep

# Initialization
led = LED(17)

try:
    while True:
        led.on()
        print('...LED ON')
    
        sleep(0.02)
    
        led.off()
        print('LED OFF...')
        
        sleep(0.02)
except KeyboardInterrupt:
    print('Exiting...')
finally:
    pass
    