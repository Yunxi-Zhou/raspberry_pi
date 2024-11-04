from gpiozero import LED, Button, TonalBuzzer
from time import sleep
import threading

BeepPin = TonalBuzzer(22)

ALedPin = LED(17)
BLedPin = LED(27)

switchPin = Button(18)

flag = 0

def ledWork():
    while True:
        if flag:
            ALedPin.on()
            sleep(0.5)
            ALedPin.off()
            BLedPin.on()
            sleep(0.5)
            BLedPin.off()
        else:
            ALedPin.off()
            BLedPin.off()
tune = [
    ('C4', 0.1), ('E4', 0.1), ('G4', 0.1),
    (None, 0.1),
    ('E4', 0.1), ('G4', 0.1), ('C5', 0.1),
    (None, 0.1),
    ('C5', 0.1), ('G4', 0.1), ('E4', 0.1),
    (None, 0.1),
    ('G4', 0.1), ('E4', 0.1), ('C4', 0.1),
    (None, 0.1)
]

def buzzerWork():
    while True:
        for note, duration in tune:
            if flag == 0:
                break
            print(note)
            BeepPin.play(note)
            sleep(duration)
        BeepPin.stop()

def main():
    global flag
    while True:
        flag = 1 if switchPin.is_pressed else 0

try:
    tBuzz = threading.Thread(target=buzzerWork)
    tBuzz.start()
    tLed = threading.Thread(target=ledWork)
    tLed.start()
    main()

except KeyboardInterrupt:
    BeepPin.stop()
    ALedPin.off()
    BLedPin.off()
    print('Existing...')
finally:
    pass 