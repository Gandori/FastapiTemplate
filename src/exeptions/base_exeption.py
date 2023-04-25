from starlette.responses import JSONResponse


class BaseExeption(Exception):
    status_code: int
    message: str

    def __init__(self):
        super().__init__()

    def response(self) -> JSONResponse:
        return JSONResponse(
            status_code=self.status_code, content={'message': self.message}
        )
