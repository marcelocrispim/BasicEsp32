import socketio
from sanic import Sanic
from sanic.response import file
import asyncio
from json import loads

sio = socketio.AsyncServer(async_mode='sanic')
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
    print("Starting UDP server")
    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: EchoServerProtocol(q),
        local_addr=('0.0.0.0', 6666))

    try:
        while True:
            await asyncio.sleep(3600)  # Serve for 1 hour.
    finally:
        transport.close()


async def background_task(q):
    while True:
        msg = loads(await q.get())
        await sio.emit('event', msg['data'])


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
    app.run(host="127.0.0.1", port=8000)
