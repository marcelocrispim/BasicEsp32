import socketio
from sanic import Sanic
from sanic.response import file

sio = socketio.AsyncServer(async_mode='sanic')

app = Sanic(__name__)
sio.attach(app)


async def background_task():
    """Example of how to send server generated events to clients."""
    count = False
    while True:
        await sio.sleep(10)
        count = not count
        await sio.emit('event', {'l3': count})


@app.listener('before_server_start')
async def before_server_start(sanic, loop):
    sio.start_background_task(background_task)


app.static('/', './vuepage/dist/')


@app.route("/about")
async def index2(request, ):
    return await file('./vuepage/dist/index.html')


@app.route("/")
async def index(request, ):
    return await file('./vuepage/dist/index.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
