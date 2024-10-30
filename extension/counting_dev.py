from gpiozero import OutputDevice, MotionSensor

pir = MotionSensor(26)

# Serial Data Input, Register Clock Input, Shift Register Clock Input
SDI = OutputDevice(24)
RCLK = OutputDevice(23)
SRCLK = OutputDevice(18)

# 7-segment display pins
placePin = [OutputDevice(pin) for pin in (10,22,27,17)]

number = (0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90)

counter = 0

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
    hc595_shift(number[counter % 1000 // 100])
    
    clearDisplay()
    pickDigit(3)
    hc595_shift(number[counter % 10000 // 1000])
    
def loop():
    global counter 
    # current state = 0, last state = 0
    cs = 0
    ls = 0
    while True:
        display()
        cs = 1 if pir.motion_detected else 0
        if cs == 1 and ls == 0:
            counter += 1
        ls == cs

try:
    loop()
except KeyboardInterrupt:
    SDI.off()
    SRCLK.off()
    RCLK.off()
    print('Existing...')
finally:
    pass