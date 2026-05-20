from starlette.middleware.base import BaseHTTPMiddleware


class StudentIDMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):
        response = await call_next(request)

        response.headers["X-Student-ID"] = "BSCS23179"

        return response