from gpiozero import Motor
from time import sleep

motor = Motor(forward=17,backward=27,enable=22)

try:
    actions = {'CW':motor.forward, 'CCW':motor.backward, 'STOP':motor.stop}
    
    while True:
        for action in ['CW','STOP','CCW','STOP']:
            actions[action]()
            print(f'{action}')
            sleep(5)
except KeyboardInterrupt:
    print('Existing...')
finally:
    pass
