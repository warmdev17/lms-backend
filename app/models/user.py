from enum import StrEnum
import uuid

from sqlalchemy import String, Enum as SQLEnum, text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class UserRole(StrEnum):
    ADMIN = "ADMIN"
    TEACHER = "TEACHER"


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        default=uuid.uuid6, primary_key=True, server_default=text("gen_random_uuid()")
    )

    email: Mapped[str] = mapped_column(
        String(255), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole),
        default=UserRole.TEACHER,
        nullable=False,
        server_default=text("'TEACHER'"),
    )
    is_active: Mapped[bool] = mapped_column(default=True, server_default=text("true"))
