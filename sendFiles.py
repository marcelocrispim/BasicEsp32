from serial import Serial
from ampy.pyboard import Pyboard
from ampy.files import Files
from time import sleep, time, ctime
from serial.tools.list_ports import comports

porta = [port.device for port in comports() if port.vid == 4292 and port.pid == 60000][0] or 'COM3'

listOffiles = [
    'lista.json',
    'extras.py',
    'main.py',
    'boot.py',
]

s = Serial(porta)
print('stop internal script ', end='')
print('.', end='')
s.write(b'\x03')
sleep(1)
print('.', end='')
s.write(b'\x03')
print('.', end='')
s.write(b'\x03\x04')
print('.', end='')
s.write(b'\x03')
print('.', end='')
s.write(b'\x03')
print('.', end='')
s.write(b'\x03')
print('\n')
s.close()

p = Pyboard(porta)
f = Files(p)

for y in listOffiles:
    print(f'send - {y}', end='  ')
    f.put(y, open(y).read())
    print(f'ok..')
    sleep(1)
p.close()
sleep(1)

s = Serial(porta)
s.write('\x03\x04'.encode('utf-8'))
s.close()
print(f'Soft Reboot')
