import pydantic
from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette_session import SessionMiddleware


class Middleware(pydantic.BaseSettings):
    secret_key: str = 'secret-key'
    cookie_name: str = 'cookie_name'
    allowed_hosts: str = '*'

    def __init__(self) -> None:
        super().__init__()

    def setup(self, app: FastAPI) -> None:
        app.add_middleware(
            middleware_class=SessionMiddleware,
            secret_key=self.secret_key,
            cookie_name=self.cookie_name,
        )
        allowed_hosts: list = self.allowed_hosts.split(',')
        app.add_middleware(TrustedHostMiddleware, allowed_hosts=allowed_hosts)
