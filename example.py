from sanic import Sanic
from sanic.response import text
from sanic.views import HTTPMethodView

from server import

# @app.get("/")
# async def hello_world(request):
#     return text("Karman Pidor")

class SimpleView(HTTPMethodView):

  def get(self, request):
      return text("I am get method")

  # You can also use async syntax
  async def post(self, request):
      return text("I am post method")

  def put(self, request):
      return text("I am put method")

  def patch(self, request):
      return text("I am patch method")

  def delete(self, request):
      return text("I am delete method")

app.add_route(SimpleView.as_view(), "/class")

from sanic.response import HTTPResponse, text
from sanic.request import Request

# type annotation
@app.get("/typed")
async def typed_handler(request: Request) -> HTTPResponse:
    return text("Done.")
