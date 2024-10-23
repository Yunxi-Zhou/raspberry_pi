from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)

try:
    while True:
        print('Buzzer On')
        buzzer.on()
        sleep(0.1)
        
        print('Buzzer Off')
        buzzer.off()
        sleep(0.1)
except KeyboardInterrupt:
    print('Existing...')
finally:
    pass
       