from datetime import datetime

from pydantic import BaseModel, Field

from app.core.error_codes import ErrorCode


class ErrorDetail(BaseModel):
    field: str | None = None
    code: ErrorCode
    message: str


class APIResponse[T](BaseModel):
    status_code: int
    message: str
    error_code: str | None = None
    error_details: list[ErrorDetail] | None = None
    data: T | None = None
    meta: dict | None = None
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    path: str

    # 3
