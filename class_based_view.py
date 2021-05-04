#https://sanicframework.org/en/guide/advanced/class-based-views.html#why-use-them
#  Dont do this
@app.get("/foo")
async def foo_get(request):
    ...

@app.post("/foo")
async def foo_post(request):
    ...

@app.put("/foo")
async def foo_put(request):
    ...

@app.route("/bar", methods=["GET", "POST", "PATCH"])
async def bar(request):
    if request.method == "GET":
        ...
    elif request.method == "POST":
        ...
    elif request.method == "PATCH":
        ...


#  Do this
from sanic.views import HTTPMethodView


class FooBar(HTTPMethodView):
    async def get(self, request):
        ...

    async def post(self, request):
        ...

    async def put(self, request):
        ...


app.add_route(FooBar.as_view(), "/foobar)

