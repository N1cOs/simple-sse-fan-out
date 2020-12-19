## Scanner
Simple HTTP service, which fan-out every incoming http message
to all opened SSE sessions.

## API

### GET /api/v1/scan

Opens SSE session.

### POST /api/v1/distances

Sends body of a request to all open SSE sessions.
Request body is sent as is without any processing.
