from gpiozero import DigitalOutputDevice, Button
from time import sleep
import LCD1602

class Keypad:
    def __init__(self, row_pins, cols_pins, keys):
        self.rows = [DigitalOutputDevice(pin) for pin in row_pins]
        self.cols = [Button(pin, pull_up=False) for pin in cols_pins]
        self.krys = keys
    
    def read(self):
        pressed_key = []
        for i, row in enumerate(self.rows):
            row.on()
            for j, col in enumerate(self.cols):
                if col.is_pressed:
                    index = i * len(self.cols) + j
                    pressed_key.append(self.keys[index])
            row.off()
        return pressed_key

# password set up
LENS = 4
password = ['1','9','8','4']
testword = ['0','0','0','0']
keyIndex = 0

def check():
    for i in range(LENS):
        if password[i] != testword[i]:
            return 0
    return 1

def setup():
    global keypad, last_key_pressed
    rows_pins = [18,23,24,25]
    cols_pins = [10,22,27,17]
    keys = ["1", "2", "3", "A",
            "4", "5", "6", "B",
            "7", "8", "9", "C",
            "*", "0", "#", "D"]

    # initialize the keypad and LCD
    keypad = Keypad(rows_pins, cols_pins, keys)
    last_key_pressed = []
    LCD1602.init(0x27, 1)
    LCD1602.clear()
    LCD1602.write(0,0,'WELCOME!')
    LCD1602.write(2,1,'Enter password')
    sleep(2)

def loop():
    global keyIndex, LENS, keypad, last_key_pressed
    while True:
        pressed_keys = keypad.read()
        if pressed_keys and pressed_keys != last_key_pressed:
            if keyIndex < LENS:
                LCD1602.clear()
                LCD1602.write(0,0,'Enter password:')
                LCD1602.write(15-keyIndex, 1, pressed_keys[0])
                testword[keyIndex] = pressed_keys[0]
                keyIndex += 1
            
            if keyIndex == LENS:
                if check() == 0:
                    LCD1602.clear()
                    LCD1602.write(3,0,'WRONG KEY')
                    LCD1602.write(0,1,'please try again')
                else:
                    LCD1602.clear()
                    LCD1602.write(4,0,'CORRECT')
                    LCD1602.write(2,1,'welcome back')
                keyIndex = 0
        last_key_pressed = pressed_keys
        sleep(0.1)

try:
    setup()
    loop()
except KeyboardInterrupt:
    LCD1602.clear()
    print('Existing...')
finally:
    pass