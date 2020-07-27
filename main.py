"""
    this main script

"""

from extras import UdpServer
from utime import sleep

serve = UdpServer()
print('Start Server')
while True:
    sleep(1)
    print(serve())
