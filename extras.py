from json import loads, dumps

import network
import urequests
import usocket as socket
import ustruct as struct
from machine import RTC
from network import WLAN
from utime import sleep_ms, localtime


def npt_br():
    NTP_DELTA = 3155673600 + (60 * 60 * 3)  # fuso de sao paulo
    host = "pool.ntp.br"
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1b
    addr = socket.getaddrinfo(host, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)
    res = s.sendto(NTP_QUERY, addr)
    msg = s.recv(48)
    s.close()
    val = struct.unpack("!I", msg[40:44])[0]
    val = val - NTP_DELTA
    tm = localtime(val)
    tm = tm[0:3] + (0,) + tm[3:6] + (0,)
    RTC().datetime(tm)


def leLista():
    with open('lista.json', 'r') as file:
        f = file.read()
    return loads(f)


def conecta():
    wlan1 = WLAN(network.STA_IF)
    wlan1.active(True)
    redesEncontradas = wlan1.scan()
    lista = leLista()
    redesConhecidas = [r['rede'] for r in lista]
    for x in redesEncontradas:
        j = x[0].decode('utf-8')
        if j in redesConhecidas:
            senha = [y['senha'] for y in lista if y['rede'] == j]
            wlan1.connect(j, senha[0])
            while not wlan1.isconnected():
                sleep_ms(100)
            sleep_ms(500)
            break


class post(object):
    def __init__(self,
                 url='http://httpbin.org/post',
                 headers={'content-type': 'application/json'}):
        self.url = url
        self.headers = headers

    def __call__(self, *args, **kwargs):
        return urequests.post(url=self.url,
                              headers=self.headers,
                              data=dumps(kwargs)).json()
