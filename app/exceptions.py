"""애플리케이션 예외 정의."""


class AppException(Exception):
    """애플리케이션 전역에서 사용하는 기본 예외."""

    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(message)
