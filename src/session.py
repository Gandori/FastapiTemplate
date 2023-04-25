from starlette.requests import Request


class Session:
    def __init__(self, request: Request) -> None:
        self.request: Request = request

    def update(self, key: str, data: str) -> None:
        self.request.session.update({key: data})

    def view(self) -> dict:
        return self.request.session

    def clear(self) -> None:
        self.request.session.clear()
