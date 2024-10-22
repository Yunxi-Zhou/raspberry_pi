from gpiozero import OutputDevice
import time
import threading

SDI = OutputDevice(24)
RCLK = OutputDevice(23)
SRCLK = OutputDevice(18)

placePin = [OutputDevice(pin) for pin in (10,22,27,17)]

number = (0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90)

counter = 0
timer1 = 0

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
    global counter, timer1
    timer1 = threading.Timer(1.0, timer)
    timer1.start()
    counter += 1
    print('%d' % counter)

def setup():
    global timer1
    timer1 = threading.Timer(1.0, timer)
    timer1.start()

def loop():
    global counter
    while True:
        for i in range(4):
            clearDisplay()
            pickDigit(i)

            digit = (counter // (10 ** i)) % 10
            
            hc595_shift(number[digit])
            time.sleep(0.001)

def destory():
    global timer1
    timer1.cancel()
    for device in [SDI, RCLK, SRCLK] + placePin:
        device.close()

try:
    setup()
    while True:
        loop()
except KeyboardInterrupt:
    print('Existing...')
    destory()
finally:
    pass