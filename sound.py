import spidev

spi = spidev.SpiDev()
spi.open(0,0)

def analog_read(channel):
    r=spi.xfer2([1, (8+channel)<<4,0])
    adc_out = ((r[1]&3)<<8) + r[2]
    return adc_out

while True:
    reading=analog_read()
    print(reading)
    time.sleep(1)


