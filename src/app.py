import asyncio
import logging
import sys

from aiohttp import web

import config
import scanner

LOGGER_NAME = "scanner"
STREAMING_FEED = "streaming_feed"


async def get_app() -> web.Application:
    log = logging.getLogger(LOGGER_NAME)
    logging.basicConfig(
        level=config.BaseConfig.LOG_LEVEL,
        format=config.BaseConfig.LOG_FORMAT,
        stream=sys.stdout,
    )

    msg_queue = asyncio.Queue()
    feed = scanner.StreamingFeed(log, msg_queue)

    app = web.Application()
    app.on_startup.append(lambda app: start_listening(app, feed))
    app.on_shutdown.append(stop_listening)

    router = app.router
    log.info(f"Base URI: {config.BaseConfig.BASE_URI}")

    feed_handler = scanner.FeedHandler(feed, config.BaseConfig.SSE_PING_INTERVAL)
    router.add_get(f"{config.BaseConfig.BASE_URI}/feed", feed_handler.open_feed)

    msg_handler = scanner.MessageHandler(msg_queue)
    router.add_put(f"{config.BaseConfig.BASE_URI}/feed", msg_handler.put_message)

    return app


async def start_listening(app: web.Application, feed: scanner.StreamingFeed):
    app[STREAMING_FEED] = asyncio.create_task(feed.start())


async def stop_listening(app: web.Application):
    app[STREAMING_FEED].cancel()
    await app[STREAMING_FEED]
