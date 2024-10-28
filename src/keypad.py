from gpiozero import DigitalOutputDevice, Button
from time import sleep

class Keypad:
    def __init__(self, rows_pins, cols_pins, keys):
        # Initialize row pins as DigitalOutputDevice
        self.rows = [DigitalOutputDevice(pin) for pin in rows_pins]
        self.cols = [Button(pin, pull_up=False) for pin in cols_pins]
        self.keys = keys
    
    def read(self):
        pressed_keys = []
        for i, row in enumerate(self.rows):
            row.on()
            for j, col in enumerate(self.cols):
                if col.is_pressed:
                    index = i * len(self.cols) + j
                    pressed_keys.append(self.keys[index])
            row.off()
        return pressed_keys
try:
    rows_pins = [18, 23, 24, 25]
    cols_pins = [10, 22, 27, 17]
    keys = ["1", "2", "3", "A",
            "4", "5", "6", "B",
            "7", "8", "9", "C",
            "*", "0", "#", "D"]
    
    keypad = Keypad(rows_pins, cols_pins, keys)
    # last key pressed = lp
    lp = []
    
    while True:
        # pressed key = pk
        pk = keypad.read()
        if pk and pk != lp:
            print(pk)
            lp = pk
        sleep(0.1)
except KeyboardInterrupt:
    print('Existing...')
finally:
    pass

                