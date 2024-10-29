from gpiozero import OutputDevice, InputDevice
import time

class DHT11():
    MAX_DELAY_COUINT = 100
    BIT_1_DELAY_COUNT = 10
    BITS_LEN = 40
    
    def __init__(self, pin, pull_up=False):
        self._pin = pin
        self._pull_up = pull_up
    
    def read_data(self):
        bit_count = 0
        delay_count = 0
        bits = ""
    
        # send start
        gpio = OutputDevice(self._pin)
        gpio.off()
        time.sleep(0.02)

        # wait response
        while gpio.value == 1:
            pass
        
        # read data
        while bit_count < self.BITS_LEN:
            while gpio.value == 0:
                pass
            
            # st = time.time()
            while gpio.value == 1:
                delay_count += 1
                
                if delay_count > self.MAX_DELAY_COUINT:
                    break
            if delay_count > self.BIT_1_DELAY_COUNT:
                bits += "1"
            else:
                bits += "0"
                
            delay_count = 0
            bit_count += 1
    
        hum_int = int(bits[0:8], 2)
        hum_dec = int(bits[8:16], 2)
        temp_int = int(bits[16:24], 2)
        temp_dec = int(bits[24:32], 2)
        check_sum = int(bits[32:40], 2)
        
        _sum = hum_int + hum_dec + temp_int + temp_dec
        
        if check_sum != _sum:
            hum = 0.0
            temp = 0.0
        else:
            hum = float(f'{hum_int}.{hum_dec}')
            temp = float(f'{temp_int}.{temp_dec}')
        return hum, temp

if __name__ == '__main__':
    dht11 = DHT11(17)
    
    while True:
        hum, temp = dht11.read_data()
        print(f'{time.time():.3f} temperature: {temp}C humidity: {hum}%')
        time.sleep(2)
            
        