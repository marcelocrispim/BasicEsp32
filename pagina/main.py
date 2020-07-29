from sanic import Sanic
from sanic.response import json, file

app = Sanic(__name__)


@app.route("/")
async def index(request):
    return file('cd vuepage')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
