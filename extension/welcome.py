from gpiozero import LED, MotionSensor, Servo, TonalBuzzer
from time import sleep

ledPin = LED(6)
pirPin = MotionSensor(21)
buzPin = TonalBuzzer(27)

myCorrection = 0.45
maxPW = (2.0 + myCorrection) / 1000
minPW = (1.0 - myCorrection) / 1000

servoPin = Servo(25, min_pulse_width=minPW, max_pulse_width=maxPW)

tune = [('C#4', 0.2), ('D4', 0.2), (None, 0.2),
        ('Eb4', 0.2), ('E4', 0.2), (None, 0.6),
        ('F#4', 0.2), ('G4', 0.2), (None, 0.6),
        ('Eb4', 0.2), ('E4', 0.2), (None, 0.2),
        ('F#4', 0.2), ('G4', 0.2), (None, 0.2),
        ('C4', 0.2), ('B4', 0.2), (None, 0.2),
        ('F#4', 0.2), ('G4', 0.2), (None, 0.2),
        ('B4', 0.2), ('Bb4', 0.5), (None, 0.6),
        ('A4', 0.2), ('G4', 0.2), ('E4', 0.2),
        ('D4', 0.2), ('E4', 0.2)]


def setAngle(angle):
    value = float(angle / 180)
    servoPin.value = value
    sleep(0.001)

def doorbell():
    for note, duration in tune:
        buzPin.play(note)
        sleep(float(duration))
    buzPin.stop()

def closedoor():
    ledPin.off()
    for i in range(180, -1, -1):
        setAngle(i)
        sleep(0.001)
    sleep(1)

def opendoor():
    ledPin.on()
    for i in range(0, 181):
        setAngle(i)
        sleep(0.001)
    sleep(1)
    doorbell()
    closedoor()

def loop():
    while True:
        if pirPin.motion_detected:
            opendoor()
        sleep(0.1)

try:
    loop()
except KeyboardInterrupt:
    buzPin.stop()
    ledPin.off()
    print('Existing...')
finally:
    pass