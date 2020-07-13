"""
    script for install last stable ESP32 firmware

"""

import tempfile
import os
import wget

linkFirmware = 'http://micropython.org/resources/firmware/esp32-idf3-20191220-v1.12.bin'
serialPort = 'COM3'

temp = tempfile.gettempdir()
wget.download(url=linkFirmware,
              out=temp + '/esp32Firmware.bin')

print(os.system(f'python -m esptool --port {serialPort} erase_flash', ))
print(os.system(
    f'python -m esptool --chip esp32 --port {serialPort} write_flash -z 0x1000 {temp + "/esp32Firmware.bin"}'))

os.remove(temp + '/esp32Firmware.bin')
