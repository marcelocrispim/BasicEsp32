try:
    import uasyncio
except:
    import upip

    upip.install('uasyncio')
    import uasyncio
from urandom import randint


async def main(numero, tempo):
    print('entrou = ', numero)
    while True:
        print('entrou = ', numero, 'tempo = ', tempo)
        await uasyncio.sleep(tempo)


loop = uasyncio.get_event_loop()
for x in range(5):
    loop.create_task(main(x, randint(4, 10)))
loop.run_forever()
