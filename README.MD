## Feed
Simple HTTP service, which fan-out every incoming http message
to all opened SSE sessions.

## API

### GET /api/v1/feed

Opens SSE session.

### PUT /api/v1/feed

Sends body of a request to all opened SSE sessions.
Body is sent as is without any processing.

## Run
Builds feed image:
```bash
make build
```

Starts the http server on address 0.0.0.0:8000:
```bash
make run
```

You can change bind address by specifying variables `SERVER_HOST` and
`SERVER_PORT`:
```bash
make run SERVER_HOST=192.168.1.1 SERVER_PORT=4242
```
