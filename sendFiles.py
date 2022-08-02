from os import name
from serial.tools.list_ports import comports
from ampy.files import Files
from ampy.pyboard import Pyboard
from time import sleep
from subprocess import run, Popen

files = ['extras.py', 'lista.json', 'main.py', 'boot.py', 'sh1106.py']
files = ['main.py']
if name == 'nt':
    tasklist = str(run(['tasklist'], capture_output=True, text=True).stdout).split('\n')
    for task in tasklist:
        if task.__len__() > 0:
            if task.split()[0] == 'putty.exe':
                Popen('powershell taskkill /IM putty.exe /f')

sleep(1)

if [port.device for port in comports() if port.vid == 4292 and port.pid == 60000]:
    serialPort = [port.device for port in comports() if port.vid == 4292 and port.pid == 60000][0]
    espType = 'Esp32'
elif [port.device for port in comports() if port.vid == 0x1A86 and port.pid == 0x7523]:
    serialPort = [port.device for port in comports() if port.vid == 0x1A86 and port.pid == 0x7523][0]
    espType = 'Esp8266'

else:
    print(
        'Nenhum dispositivo encontrado,'
        ' certifique que o '
        'Esp esta Conectado a porta serial e se o'
        ' Firmware micropython foi instalardo'
    )
try:
    board = Pyboard(serialPort)

    _files = Files(board)

    sleep(1)
    print(f'Parando o Script em execução no {espType} .', end='')
    board.serial.write(b'\x03')
    sleep(1)
    print('.', end='')
    board.serial.write(b'\x03')
    sleep(1)
    print('.')
    board.serial.write(b'\x03')
    sleep(1)

    print(f'Enviando {len(files)} arquivos para o {espType}')
    for file in files:
        print(f'Enviado *{file}*')
        with open(file, 'rb') as f:
            _files.put(file, f.read())
            sleep(1)
    print('Arquivos enviados, enviando sinal de "Soft reboot"', end='')
    sleep(1)
    print('..')
    board.serial.write(b'\x03\x04')
    sleep(1)
    print('Abrindo o Putty')
    Popen(f"powershell putty -serial {serialPort} -sercfg 115200,8,n,1,N")
except Exception as e:
    print(f'Erro {e}')
