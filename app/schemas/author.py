from pydantic import BaseModel, Field
from typing import Optional


class AuthorBase(BaseModel):
    name: str = Field(title="Псевдоним исполнителя")
    tracks: list = Field(title="Треки исполнителя")
    description: Optional[str] = Field(title="Описание исполнителя")


class Author(AuthorBase):
    id: int = Field(title="Идентификатор исполнителя")
    info: dict = Field(title="Информация о исполнителе")

