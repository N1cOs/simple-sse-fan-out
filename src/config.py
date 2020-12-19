import os


class BaseConfig:
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
    LOG_FORMAT = "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s"

    BASE_URI = "/api/v1"
    SSE_PING_INTERVAL = int(os.environ.get("SSE_PING_INTERVAL", 2))
