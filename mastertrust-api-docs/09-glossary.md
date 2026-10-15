# Glossary

## Conventions

- All responses are in JSON format.
- All request parameters are mandatory unless explicitly marked as `[optional]`.

## Status Codes

All status codes are standard HTTP status codes. The ones below are used in this API.

- `2XX` — Success of some kind
- `4XX` — Error occurred on the client's part
- `5XX` — Error occurred on the server's part

| Status Code | Description |
| --- | --- |
| 200 | OK |
| 400 | Bad request |
| 401 | Authentication failure |
| 403 | Forbidden |
| 404 | Resource not found |
| 405 | Method Not Allowed |
| 500 | Internal Server Error |
| 503 | Service Unavailable |
