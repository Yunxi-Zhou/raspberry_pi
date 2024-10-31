from gpiozero import OutputDevice, LED
import threading

# Setup GPIO pins for 74HC595 shift register
SDI = OutputDevice(24)
RCLK = OutputDevice(23)
SRCLK = OutputDevice(18)

placePin = [OutputDevice(pin) for pin in (10,22,27,17)]

number = (0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90)

ledPinR = LED(25)
ledPinG = LED(8)
ledPinY = LED(7)

# green light = gl, yellow light = yl, red light = rl
gl = 30
yl = 5
rl = 60

# light color = lc
lc = ('Red','Green','Yellow')

# Initialize the state variable
colorState = 0
counter = 0
timer1 = None

def setup():
    global timer1
    timer1 = threading.Timer(1.0, timer)
    timer1.start()
    
def clearDisplay():
    for _ in range(8):
        SDI.on()
        SRCLK.on()
        SRCLK.off()
    RCLK.on()
    RCLK.off()

def hc595_shift(data):
    for i in range(8):
        SDI.value = 0x80 & (data << i)
        SRCLK.on()
        SRCLK.off()
    RCLK.on()
    RCLK.off()

def pickDigit(digit):
    for pin in placePin:
        pin.off()
    placePin[digit].on()

def timer():
    global counter, colorState, timer1
    timer1 = threading.Timer(1.0,timer)
    timer1.start()
    counter -= 1
    if counter == 1:
        counter = [gl, yl, rl][colorState]
        colorState = (colorState + 1) % 3
    print(f'counter: {counter}   color: {lc[colorState]}')

def lightup():
    global colorState
    ledPinR.off()
    ledPinG.off()
    ledPinY.off()
    [ledPinR, ledPinG, ledPinY][colorState].on()

def display():
    global counter
    for i in range(4):
        digit = counter
        if i == 0 and digit == 0:
            continue
        clearDisplay()
        pickDigit(3 - i)
        hc595_shift(number[digit])
    
def loop():
    while True:
        display()
        lightup()

def destroy():
    global timer1
    timer1.cancel()
    ledPinR.off()
    ledPinG.off()
    ledPinY.off()

try:
    setup()
    loop()
except KeyboardInterrupt:
    destroy()
    print('Existing...')
finally:
    pass