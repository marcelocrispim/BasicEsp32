"""
    this main script

"""
import _thread
from extras import UdpServer, UdpClient
from utime import sleep
from machine import ADC, Pin
from json import dumps


def readChannel(lixo):
    ad1 = ADC(Pin(32))
    ad2 = ADC(Pin(34))
    bt1 = Pin(0, Pin.IN)
    client = UdpClient(host='192.168.30.43')
    while True:
        client(ad1=ad1.read(), ad2=ad2.read(), bt1=bt1.value())
        sleep(1)


_thread.start_new_thread(readChannel, (0,))
serve = UdpServer()
print('Start Server')

while True:
    sleep(1)
    print(serve())
