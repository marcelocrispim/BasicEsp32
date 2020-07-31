import socketio
from sanic import Sanic
from sanic.response import file
import asyncio
from json import loads
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s:%(message)s')
sio = socketio.AsyncServer(async_mode='sanic', cors_allowed_origins='*')
app = Sanic(__name__)
sio.attach(app)


class EchoServerProtocol:
    def __init__(self, q):
        self.q = q

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
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
    while True:
        try:
            msg = loads(await q.get())
            await sio.emit('event', msg['data'])
        except Exception as e:
            logging.error('Queue error ' + e.__str__())
            pass


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
    app.run(host="0.0.0.0", port=8000, )
