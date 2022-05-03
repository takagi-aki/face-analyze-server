from fastapi.responses import PlainTextResponse


async def default_http_exception_handler(request, exc):
    return PlainTextResponse(f'{exc.status_code} {exc.detail}', status_code=exc.status_code)
