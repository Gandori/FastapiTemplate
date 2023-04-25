import pathlib

import pydantic
import uvicorn


class Server(pydantic.BaseSettings):
    host: str = 'localhost'
    port: int = 8080
    log_level: str = 'info'
    reload: bool = False
    workers: int = 1
    backlog: int = 2048
    limit_max_requests: int | None = None
    limit_concurrency: int | None = None
    timeout_keep_alive: int = 5
    server_header: bool = False
    date_header: bool = False

    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        uvicorn.run(
            app='src:app',
            host=self.host,
            port=self.port,
            log_level=self.log_level,
            reload=self.reload,
            workers=self.workers,
            backlog=self.backlog,
            limit_max_requests=self.limit_max_requests,
            limit_concurrency=self.limit_concurrency,
            timeout_keep_alive=self.timeout_keep_alive,
            server_header=self.server_header,
            date_header=self.date_header,
            log_config=f'{pathlib.Path(__file__).parent.resolve()}/log.ini',
        )
