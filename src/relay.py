from gpiozero import OutputDevice
from time import sleep

relay = OutputDevice(17, initial_value = False)

try:
    while True:
        print('Relay open...')
        relay.on()
        sleep(1)

        print('...Relay close')
        relay.off()
        sleep(1)
except KeyboardInterrupt:
    print('Existing...')
    relay.off()
finally:
    pass