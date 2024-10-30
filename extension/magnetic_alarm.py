from gpiozero import Buzzer, Button
from time import sleep

buzzer = Buzzer(27)
reed_switch = Button(17, pull_up=True)

try:
    while True:
        if reed_switch.is_pressed:
            buzzer.off()
            print('magnetic field')
        else:
            buzzer.on()
            sleep(0.1)
            buzzer.off()
            sleep(0.1)
            
except KeyboardInterrupt:
    buzzer.off()
    print('Existing...')
finally:
    pass
