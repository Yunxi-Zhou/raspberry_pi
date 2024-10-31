from gpiozero import LED
import ADC0834
from time import sleep

ledPins = [25,12,16,20,21,5,6,13,19,26]
leds = [LED(pin) for pin in ledPins]

ADC0834.setup()

def LedBarGraph(value):
    for i in range(10):
        leds[i].off()
    for i in range(value):
        leds[i].on()

try:
    while True:
        analogValue = ADC0834.getResult()
        LedBarGraph(int(analogValue/25))
except KeyboardInterrupt:
    for i in range(10):
        leds[i].off()
    print('Existing...')
finally:
    pass
        