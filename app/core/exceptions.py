from fastapi import status

from app.core.error_codes import ErrorCode


class AppException(Exception):
    def __init__(self, status_code: int, message: str, error_code: str):
        self.status_code = status_code
        self.message = message
        self.error_code = error_code


class NotFoundException(AppException):
    def __init__(
        self,
        status_code: int = status.HTTP_404_NOT_FOUND,
        message: str = "Không tìm thấy",
        error_code: str = ErrorCode.NOT_FOUND,
    ):
        super().__init__(status_code, message, error_code)
