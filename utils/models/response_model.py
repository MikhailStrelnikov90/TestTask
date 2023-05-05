class ResponseModel:
    def __init__(self, status: int, response: dict = None) -> None:
        self.status = status
        self.response = response
