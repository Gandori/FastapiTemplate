import fastapi
import pydantic


class Service(pydantic.BaseSettings):
    title: str = 'Example'
    version: str = '0.0.0'
    docs_url: str | None = None
    redocs_url: str | None = None
    prefix: str = ''

    def __init__(self) -> None:
        super().__init__()

    def create(self) -> fastapi.FastAPI:
        service: fastapi.FastAPI = fastapi.FastAPI(
            title=self.title,
            version=self.version,
            docs_url=self.docs_url,
            redoc_url=self.redocs_url,
            openapi_url=f'{self.prefix}/openapi.json',
        )

        return service
