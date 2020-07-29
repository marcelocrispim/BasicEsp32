"""
    this main script

"""
import _thread
from extras import UdpServer, UdpClient
from utime import sleep_ms
from machine import ADC, Pin



def readChannel(lixo):
    ad1 = ADC(Pin(32))
    ad1.atten(ADC.ATTN_11DB)
    ad1.width(ADC.WIDTH_9BIT)
    ad2 = ADC(Pin(34))
    ad2.atten(ADC.ATTN_11DB)
    ad2.width(ADC.WIDTH_9BIT)
    bt1 = Pin(0, Pin.IN)
    client = UdpClient(host='192.168.30.43')
    while True:
        send1 = ad1.read()
        sleep_ms(1)
        send2 = ad2.read()
        sleep_ms(1)
        send3 = bt1.value()
        sleep_ms(1)
        client(ad1=send1, ad2=send2, bt1=send3)
        sleep_ms(10)


_thread.start_new_thread(readChannel, (0,))
serve = UdpServer()
print('Start Server')

while True:
    sleep_ms(1000)
    print(serve())
