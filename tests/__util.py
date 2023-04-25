import dotenv
import httpx
from httpx import Response
from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = 'localhost'
    port: int = 10000
    prefix: str = ''


class Request:
    def __init__(self) -> None:
        dotenv.load_dotenv()
        settings = Settings()
        self.host: str = settings.host
        self.port: int = settings.port
        self.prefix: str = settings.prefix
        self._url: str = f'http://{self.host}:{self.port}{self.prefix}'

    def get(self, route: str) -> Response:
        return httpx.get(url=f'{self._url}{route}')

    def post(self, json: dict, route: str) -> Response:
        return httpx.post(url=f'{self._url}{route}', json=json)

    def put(self, json: dict, route: str) -> Response:
        return httpx.put(url=f'{self._url}{route}', json=json)

    def delete(self, route: str) -> Response:
        return httpx.delete(url=f'{self._url}{route}')
