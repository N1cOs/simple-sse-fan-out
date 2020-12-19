import asyncio

from aiohttp import web
from aiohttp_sse import sse_response

from . import streaming


class ScanHandler:
    def __init__(self, feed: streaming.StreamingFeed, ping_interval: int):
        self.feed = feed
        self.ping_interval = ping_interval

    async def scan(self, request: web.Request):
        async with self.feed.open_session() as queue:
            async with sse_response(request) as resp:
                resp.ping_interval = self.ping_interval
                while True:
                    msg = await queue.get()
                    await resp.send(msg.decode())


class DistancesHandler:
    def __init__(self, msg_queue: asyncio.Queue):
        self.msg_queue = msg_queue

    async def update(self, request: web.Request):
        body = await request.read()
        await self.msg_queue.put(body)
        return web.Response(status=200, body=body)
