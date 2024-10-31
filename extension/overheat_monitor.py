import LCD1602
from gpiozero import LED, Buzzer, Button
import ADC0834
import time
import math

Joy_BtnPin = Button(22)
buzzPin = Buzzer(23)
ledPin = LED(24)

upperTem = 40

ADC0834.setup()
LCD1602.init(0x27, 1)

def get_joystick_value():
    x_val = ADC0834.getResult(1)
    y_val = ADC0834.getResult(2)
    
    if x_val > 200:
        return 1
    elif x_val < 50:
        return -1
    elif y_val > 200:
        return -10
    elif y_val < 50:
        return 10
    else:
        return 0

def upper_tem_setting():
    global upperTem
    LCD1602.write(0, 0, 'Upper Adjust: ')
    change = int(get_joystick_value())
    upperTem += change
    strUpperTem += str(upperTem)
    LCD1602.write(0, 1, strUpperTem)
    LCD1602.write(len(strUpperTem), 1, '          ')
    time.sleep(0.1)

def temperature():
    analogVal = ADC0834.getResult()
    Vr = 5 * float(analogVal) / 255
    Rt = 10000 * Vr / (5 - Vr)
    temp = 1 / (((math.log(Rt / 10000)) / 3950) + (1 / (273.15 + 25)))
    c = temp - 273.15
    return (c, 2)

def monitoring_temp():
    global upperTem
    c = temperature()
    LCD1602.write(0, 0, 'Temp: ')
    LCD1602.write(0, 1, 'Upper: ')
    LCD1602.write(6, 0, str(c))
    LCD1602.write(7, 1, str(upperTem))
    time.sleep(0.1)
    if c >= upperTem:
        buzzPin.on()
        ledPin.on()
    else:
        buzzPin.off()
        ledPin.off()

try:
    lastState = 1
    stage = 0
    while True:
        currentState = Joy_BtnPin.value
        if currentState == 1 and lastState == 0:
            stage = (stage + 1) % 2
            time.sleep(0.1)
            LCD1602.clear()
        lastState = currentState
        if stage == 1:
            upper_tem_setting()
        else:
            monitoring_temp()
except KeyboardInterrupt:
    LCD1602.clear()
    ADC0834.destory()
    print('Existing...')
finally:
    pass