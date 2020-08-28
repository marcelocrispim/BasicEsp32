"""
    this main script

"""
import _thread
from extras import UdpServer, UdpClient
from utime import sleep_ms, time
from machine import ADC, Pin

inicio = False
startTime = time()


def evento():
    global inicio
    inicio = not inicio


bt1 = Pin(0, Pin.IN)
bt1.irq(handler=lambda e: evento(), trigger=Pin.IRQ_FALLING)


def readChannel(lixo):
    # ad1 = ADC(Pin(32))
    # ad1.atten(ADC.ATTN_11DB)
    # ad1.width(ADC.WIDTH_9BIT)
    # ad2 = ADC(Pin(34))
    # ad2.atten(ADC.ATTN_11DB)
    # ad2.width(ADC.WIDTH_9BIT)
    global inicio
    client = UdpClient(host='192.168.30.43')
    while True:
        # send1 = ad1.read()
        # sleep_ms(1)
        # send2 = ad2.read()
        # sleep_ms(1)
        # send3 = inicio
        # sleep_ms(1)
        client(bt1=inicio)
        sleep_ms(200)


_thread.start_new_thread(readChannel, (0,))
serve = UdpServer()
print('Start Server')

while True:
    sleep_ms(1000)
    # print(serve())
