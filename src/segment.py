from gpiozero import OutputDevice
from time import sleep

SDI = OutputDevice(17)
RCLK = OutputDevice(18)
SRCLK = OutputDevice(27)

segCode = [
    0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d,
    0x07, 0x7f, 0x6f, 0x77, 0x7c, 0x39, 0x5e, 0x79, 0x71
]

def hc595_shift(data):
    for bit in range(8):
        SDI.value = 0x80 & (data << bit)
        SRCLK.on()
        sleep(0.001)
        SRCLK.off()
    RCLK.on()
    sleep(0.001)
    RCLK.off()

def display_all_on():
    all_on_code = 0x3f
    hc595_shift(all_on_code)
    print('Displaying all segments on')

try:
    while True:
        for code in segCode:
            hc595_shift(code)
            print(f'Displaying segCode[{segCode.index(code)}]: 0x{code:02X}')
            sleep(0.5)
except KeyboardInterrupt:
    print('Existing...')
finally:
    pass