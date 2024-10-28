from gpiozero import LED, Button
from time import sleep

# initialize micro switch on GPIO pin 17 with the pull-up resistor
micro_switch = Button(17, pull_up=False)
led1 = LED(22)
led2 = LED(27)

try:
    while True:
        if micro_switch.is_pressed:
            print('LED1 ON')
            led1.on()
            led2.off()
        else:
            print('   LED2 ON')
            led2.on()
            led2.off()
        sleep(0.5)
except KeyboardInterrupt:
    print('Existing...')
finally:
    pass
