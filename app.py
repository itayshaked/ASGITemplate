import asyncio

from starlette.responses import JSONResponse
from starlette.applications import Starlette
from starlette.routing import Route


async def sleep(request):
    asyncio.sleep(10)
    return JSONResponse({"status": "done"})


routes = [Route("/", endpoint=sleep)]

starlette_app = Starlette(debug=False, routes=routes)
