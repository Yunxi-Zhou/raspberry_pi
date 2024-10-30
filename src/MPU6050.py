import smbus
import math
from time import sleep

# power management registers
# power management = pm
pm_1 = 0x6b
pm_2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr + 1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + val)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a) + (b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

bus = smbus.SMBus(1)
address = 0x68

bus.write_byte_data(address, pm_1, 0)

try:
    while True:
        sleep(0.1)
        x = read_word_2c(0x43)
        y = read_word_2c(0x45)
        z = read_word_2c(0x47)
        
        print(f'gyro_xout : {x}, scaled: {(x/131)}')
        print(f'gyro_yout : {y}, scaled: {(y/131)}')
        print(f'gyro_zout : {z}, scaled: {(z/131)}')
        
        ax = read_word_2c(0x3b)
        ay = read_word_2c(0x3d)
        az = read_word_2c(0x3f)
        
        axs = ax/16384.0
        ays = ay/16384.0
        azs = az/16384.0
        
        print(f'accel_xout: {ax}, scaled: {axs}')  
        print(f'accel_yout: {ay}, scaled: {ays}')        
        print(f'accel_zout: {az}, scaled: {azs}')
        
        print(f'x rotation: {get_x_rotation(axs,ays,azs)}')
        print(f'y rotation: {get_y_rotation(axs,ays,azs)}')
        
        sleep(1)
except KeyboardInterrupt:
    print('Existing...') 
finally:
    pass       
              