from gpiozero import LCD1602
import time

def setup():
    LCD1602.init(0x27,1)
    LCD1602.write(0,0,'Greetings!')
    LCD1602.write(1,1,'From Ethan')
    time.sleep(1)

try:
    setup()
except KeyboardInterrupt:
    LCD1602.clear()
finally:
    pass
