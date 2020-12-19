SERVER_HOST := 0.0.0.0
SERVER_PORT := 8000

.PHONY: run
run:
	docker run \
		--rm \
		--publish $(SERVER_PORT):$(SERVER_PORT) \
		$(SCANNER_IMAGE) python main.py \
			--host $(SERVER_HOST) \
			--port $(SERVER_PORT)

SCANNER = scanner
SCANNER_IMAGE ?= $(SCANNER):1.0
SCANNER_HOST_PATH = $(shell pwd)/src

.PHONY: build
build:
	docker build \
		--tag $(SCANNER_IMAGE) $(SCANNER_HOST_PATH)
