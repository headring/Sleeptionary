LD_FILE = boards/samd51x19-bootloader-external-flash.ld
USB_VID = 0x1209
USB_PID = 0x4D43
USB_PRODUCT = "Robo HAT MM1 M4"
USB_MANUFACTURER = "Robotics Masters"

CHIP_VARIANT = SAMD51G19A
CHIP_FAMILY = samd51

#QSPI_FLASH_FILESYSTEM = 0

SPI_FLASH_FILESYSTEM = 1
EXTERNAL_FLASH_DEVICE_COUNT = 1
EXTERNAL_FLASH_DEVICES = "W25Q64JV_IQ"
LONGINT_IMPL = MPZ

# No I2S on SAMD51G
CIRCUITPY_AUDIOBUSIO = 0
# Make room for more stuff
CIRCUITPY_DISPLAYIO = 0
CIRCUITPY_FREQUENCYIO = 0

# Include these Python libraries in firmware.
#FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_BusDevice
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_NeoPixel
#FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_INA219
#FROZEN_MPY_DIRS += $(TOP)/frozen/RoboticsMasters_CircuitPython_MPU9250
