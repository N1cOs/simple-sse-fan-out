## Feed
Simple HTTP service, which fan-out every incoming http message
to all opened SSE sessions.

## API

### GET /api/v1/feed

Opens SSE session.

### PUT /api/v1/feed

Sends body of a request to all opened SSE sessions.
Body is sent as is without any processing.
