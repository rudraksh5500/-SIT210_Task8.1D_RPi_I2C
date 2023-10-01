import smbus
import time

BH1750 = 0x23 
CONTINUOUS_HIGH_RES_MODE_1 = 0x10

bus = smbus.SMBus(1)

def ReadBH1750(device_address):
  # Read data from I2C interface
  data = bus.read_i2c_block_data(device_address,CONTINUOUS_HIGH_RES_MODE_1)
  result=(data[1] + (256 * data[0])) / 1.2
  return result

## program ##
try:
	while 1:
            LightLevel=ReadBH1750(BH1750)
            if LightLevel < 5:
                print ("Too Dark")
            elif LightLevel < 10:
                print ("Dark")
            elif LightLevel < 20:
                print ("Medium")
            elif LightLevel < 25:
                print ("Bright")
            else:
                print ("Too Bright")
            time.sleep(1)
                
except KeyboardInterrupt:
	GPIO.cleanup()