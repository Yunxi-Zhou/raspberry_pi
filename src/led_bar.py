from gpiozero import LED
from time import sleep

#define LED pin
led_pins = [18,23,24,25,8,7,12,16,20,21]

# create LED 
leds = [LED(pin) for pin in led_pins]

def odd_led():
    for i in range(5):
        j = i * 2
        leds[j].on()
        print(f'odd led: {j}')
        sleep(1)
        leds[j].off()

def even_led():
    for i in range(5):
        j = i * 2 + 1
        leds[j].on()
        print(f'even led: {j}')
        sleep(1)
        leds[j].off()

def all_led():
    for led in leds:
        led.on()
        print(f'all led: {led}')
        sleep(1)
        led.off()

def turn_off():
    for led in leds:
        led.off()

try:
    while True:
        odd_led()
        sleep(1)
        even_led()
        sleep(1)
        all_led()
        sleep(1)
except KeyboardInterrupt:
    print('Existing...')
    turn_off()
finally:
    pass