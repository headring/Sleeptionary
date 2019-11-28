import smbus
import time
address = 0x69
bus = smbus.SMBus(1)
CONT_H_RES_MODE     = 0x10
CONT_H_RES_MODE2    = 0x11
CONT_L_RES_MODE     = 0x13
ONETIME_H_RES_MODE  = 0x20
ONETIME_H_RES_MODE2 = 0x21
ONETIME_L_RES_MODE  = 0x23

while True:
	bus.write_byte(address,A0)
	luxBytes = bus.read_i2c_block_data(address, CONT_H_RES_MODE, 2)
	lux = int.from_bytes(luxBytes, byteorder='big')
	print('{0} lux'.format(lux))
	time.sleep(1)