import time, smbus

address = 0x48

bus = smbus.SMBus(1)

while 1:
	bus.write_byte(address,0)
	value = bus.read_byte(address)
	print(value)
	time.sleep(0.1)
