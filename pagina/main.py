import socketio
from sanic import Sanic
from sanic.response import file
import asyncio
from json import loads
import logging
from sanic_compress import Compress
from aiofile import AIOFile
from dateutil.parser import parse
from datetime import datetime
import extras

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s:%(message)s')
sio = socketio.AsyncServer(async_mode='sanic', cors_allowed_origins='*', json=extras)
app = Sanic(__name__)
app.config['COMPRESS_LEVEL'] = 9
app.config['COMPRESS_MIN_SIZE'] = 1
Compress(app)
sio.attach(app)


class EchoServerProtocol:
    def __init__(self, q):
        self.q = q

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        # print('msg ', message)
        self.q.put_nowait(message)


async def mainUdp(q):
    logging.info("Starting UDP server")
    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: EchoServerProtocol(q),
        local_addr=('0.0.0.0', 6666))

    try:
        while True:
            await asyncio.sleep(3600)  # Serve for 1 hour.
    except Exception as e:
        logging.error('UDP error' + e.__str__())
        transport.close()


async def background_task(q):
    logging.info('Starting BackGround Task')
    async with AIOFile("devices.json") as afp:
        devices = loads(await afp.read())
    [d1.update({'update': parse(d1['update']), 'startTime': parse(d1['startTime'])}) for d1 in devices]
    logging.info('devices = ' + devices.__str__())
    while True:
        try:
            try:
                msg = loads(await asyncio.wait_for(q.get(), timeout=5))
                [d2.update({'online': True, 'update': datetime.now()}) for d2 in devices if d2['mac'] == msg['device']]
                [d2.update({'startTime': datetime.now()}) for d2 in devices if
                 d2['mac'] == msg['device'] and d2['ligado'] == False and msg['data']['bt1'] == True]

                [d2.update({'timeOn': (datetime.now() - d2['startTime']).__str__().split('.')[0]}) for d2 in devices if
                 d2['mac'] == msg['device'] and msg['data']['bt1'] == True]
                [d2.update({'ligado': msg['data']['bt1']}) for d2 in devices if d2['mac'] == msg['device']]

            except asyncio.TimeoutError:
                logging.error('Timeout ERROR')

        except Exception as e:
            logging.error('Queue error ' + e.__str__())
        [d3.update({'online': False}) for d3 in devices if
         (datetime.now() - d3['update']).seconds > 10]

        await sio.emit('event', devices)


@app.listener('before_server_start')
async def before_server_start(sanic, loop):
    q = asyncio.Queue()
    sio.start_background_task(background_task, (q))
    sio.start_background_task(mainUdp, (q))


app.static('/', './vuepage/dist/')


async def index(request, ):
    return await file('./vuepage/dist/index.html')


app.add_route(index, '/')
app.add_route(index, '/about')

if __name__ == "__main__":
    app.run(host=["::", "0.0.0.0"], port=8000, )
2
