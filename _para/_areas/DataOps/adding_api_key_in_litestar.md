### Adding api, add api key in litestar
### use guards
```python
def api_key_guard(
    connection: ASGIConnection,
    _: BaseRouteHandler,
) -> None:
    provided_key = connection.headers.get("x-api-key")

    if not API_KEY:
        raise RuntimeError("API_KEY is not set")

    if not provided_key:
        raise NotAuthorizedException("Missing API key")

    if not hmac.compare_digest(provided_key, API_KEY):
        raise NotAuthorizedException("Invalid API key")


```
```python
@post("/thing", guards=[api_key_guard])
async def add_thing(data: WriteRequest) -> dict:
    print(f"Received request to add thing: {data}")
    result = grabber.handle_add(data)

    return result
```
