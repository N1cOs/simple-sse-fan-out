import asyncio
import contextlib
import logging
from typing import AsyncContextManager, Generator


class StreamingFeed:
    MAX_SESSION_ID = 10 * 6

    def __init__(
        self,
        log: logging.Logger,
        msg_queue: asyncio.Queue,
    ):
        self.log = log
        self.msg_queue = msg_queue

        self.sessions = []
        self.session_id_iter = iter(self._next_id())

    async def start(self):
        await asyncio.gather(self._fan_out())

    @contextlib.asynccontextmanager
    async def open_session(self) -> AsyncContextManager[asyncio.Queue]:
        session_id = next(self.session_id_iter)
        self.log.info(f"Creating client session: session_id={session_id}")

        out = asyncio.Queue()
        self.sessions.append(out)

        self.log.info(f"Successfully created client session: session_id={session_id}")

        try:
            yield out
        finally:
            self.log.info(f"Closing client session: session_id={session_id}")
            self.sessions.remove(out)
            self.log.info(
                f"Successfully closed client session: session_id={session_id}"
            )

    async def _fan_out(self):
        while True:
            try:
                msg = await self.msg_queue.get()
                for q in self.sessions:
                    await q.put(msg)
            except asyncio.CancelledError:
                self.log.info("Canceled fan-out client messages")
                break
            except:
                self.log.error("Fan-out critical error", exc_info=True)

    def _next_id(self) -> Generator[int, None, None]:
        id_ = 0
        while True:
            if id_ > self.MAX_SESSION_ID:
                id_ = 1
            else:
                id_ += 1
            yield id_
