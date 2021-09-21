import smbus
import time
bus = smbus.SMBus(2)
multiplier = 0.0078125

data = [0xBA,0x83]
bus.write_i2c_block_data(0x48, 0x01, data)
time.sleep(0.5)

while True:
        data = bus.read_i2c_block_data(0x48, 0x00, 2)
        results = data[0] * 256 + data[1]
        #if results > 32767:
                #results -= 65535

        mV =  results * multiplier
        O2 = (21/10.3) * mV
        O2 = round(O2)

        print('Reading: {}' .format(results))
        print('miliVolt: {:.2f}mV' .format(mV))
        print('O2: {:.0f}%' .format(O2))
        print('----------------')
        time.sleep(1)
