import pytz

from datetime import datetime
from typing import Optional
from sqlalchemy.sql.sqltypes import (
    VARCHAR,
    INTEGER,
)
from sqlmodel import (
    SQLModel,
    Column,
    Field,
    Session,
)

from .config import get_session
from .utils import make_password


class Model(SQLModel):
    """
    Base class for all models.
    """
    id: int = Field(sa_column=\
            Column(
                "id",
                INTEGER,
                primary_key=True,
                autoincrement=True,
                nullable=False
            )
        )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.id}>"

    def to_dict(self):
        return self.__dict__

    def validate(self):
        pass

    async def refresh_db(self):
        session = await get_session()
        await session.refresh(self)

    async def save(self):
        self.validate()
        session: Session = await get_session()
        session.add(self)
        await session.commit()
        return self


class User(Model, table=True):
    """Built-in User model"""
    __tabelname__ = "users"

    username: str = Field(sa_column=\
            Column(
                "username",
                VARCHAR,
                unique=True,
                nullable=False
            )
        )
    password: str = Field(sa_column=\
            Column(
                "password",
                VARCHAR,
                nullable=False
            )
        )
    email: str = Field(sa_column=\
            Column(
                "email",
                VARCHAR,
                unique=True,
                nullable=False
            )
        )

    first_name: Optional[str] = Field(default=None, nullable=True)
    last_name: Optional[str] = Field(default=None, nullable=True)

    is_active: bool = Field(default=True, nullable=False)
    is_superuser: bool = Field(default=False, nullable=False)

    last_login: datetime = Field(
            default=None,
            nullable=True
        )
    date_joined: datetime = Field(
            default=datetime.now(tz=pytz.utc),
            nullable=False
        )

    def __repr__(self):
        return f"<User {self.username}>"

    def __str__(self) -> str:
        return self.username

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_id(self) -> str:
        return str(self.id)

    def validate(self):
        if not self.username:
            raise ValueError("Username is required")
        if not self.password:
            raise ValueError("Password is required")
        if not self.email:
            raise ValueError("Email is required")

    async def save(self):
        self.password = make_password(self.password)
        return await super().save()