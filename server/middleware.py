import asyncio
import http


from starlette.status import HTTP_504_GATEWAY_TIMEOUT
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import PlainTextResponse


class TimeoutMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, timeout=5):
        super().__init__(app)
        self._timeout = timeout

    async def dispatch(self, request, call_next):
        try:
            response = await asyncio.wait_for(call_next(request), timeout=self._timeout)
        except asyncio.TimeoutError:
            status_code = HTTP_504_GATEWAY_TIMEOUT
            detail = http.HTTPStatus(status_code).phrase
            return PlainTextResponse(f'{status_code} {detail}', status_code=status_code)
        return response
