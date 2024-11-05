from gpiozero import OutputDevice, Button
import time
import threading

sensorPin = Button(26)

SDI = OutputDevice(24)
RCLK = OutputDevice(23)
SRCLK = OutputDevice(18)

placePin = [OutputDevice(pin) for pin in (10,22,27,17)]

number = (0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90)

counter = 0
timer1 = None
gameState = 0

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

def display():
    global counter
    clearDisplay()
    pickDigit(0)
    hc595_shift(number[counter % 10])
    
    clearDisplay()
    pickDigit(1)
    hc595_shift(number[counter % 100 // 10])
    
    clearDisplay()
    pickDigit(2)
    hc595_shift(number[counter % 1000 // 100] - 0x80)
    
    clearDisplay()
    pickDigit(3)
    hc595_shift(number[counter % 10000 // 1000])

def stateChange():
    global gameState, counter, timer1
    if gameState == 0:
        counter = 0
        time.sleep(1)
        timer()
    elif gameState == 1 and timer1 is not None:
        timer1.cancel()
        time.sleep(1)
    gameState = (gameState + 1) % 2

def loop():
    global counter
    currentState = 0
    lastState = 0
    while True:
        display()
        currentState = sensorPin.value
        if (currentState == 0) and (lastState == 1):
            stateChange()
        lastState = currentState

def timer():
    global counter, timer1
    timer1 = threading.Timer(0.01, timer)
    timer1.start()
    counter += 1

try:
    loop()
except KeyboardInterrupt:
    if timer1:
        timer1.cancel()
    print('Existing...')
finally:
    pass