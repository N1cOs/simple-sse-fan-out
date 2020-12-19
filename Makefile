SERVER_HOST := 0.0.0.0
SERVER_PORT := 8000

.PHONY: run
run:
	docker run \
		--rm \
		--publish $(SERVER_PORT):$(SERVER_PORT) \
		$(FEED_IMAGE) python main.py \
			--host $(SERVER_HOST) \
			--port $(SERVER_PORT)

FEED = feed
FEED_IMAGE ?= $(FEED):1.0
FEED_HOST_PATH = $(shell pwd)/src

.PHONY: build
build:
	docker build \
		--tag $(FEED_IMAGE) $(FEED_HOST_PATH)
