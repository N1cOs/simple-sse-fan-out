import argparse
import asyncio
import logging

from aiohttp import web

import app

DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 80


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="feed app")

    parser.add_argument(
        "--host",
        default=DEFAULT_HOST,
        help=f"host of http server; default {DEFAULT_HOST}",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=DEFAULT_PORT,
        help=f"port of http server; default {DEFAULT_PORT}",
    )

    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    application = loop.run_until_complete(app.get_app())

    info = f"Http server started on: {args.host}:{args.port}"
    log = logging.getLogger(app.LOGGER_NAME)
    web.run_app(
        application,
        host=args.host,
        port=args.port,
        print=lambda a: log.info(info),
    )
