from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .schemas.author import Author, AuthorBase
import typing

FAKE_AUTHOR_INFO = {
    "real_name": "Андрей Федотов",
    "country": "Россия"
}

app = FastAPI(
    version="1", title="Track Distribution Service"
)
authors: typing.Dict[int, Author] = {}


@app.post(
    "/authors", status_code=201, response_model=Author, summary="Добавляет исполнителя в базу"
)
async def add_author(author: AuthorBase) -> Author:
    result = Author(
        **author.dict(), id=len(authors) + 1, info=FAKE_AUTHOR_INFO
    )
    authors[result.id] = result
    return result


@app.get(
    "/authors", summary="Возвращает список исполнителей", response_model=list[Author]
)
async def get_authors_list() -> typing.Iterable[Author]:
    return [v for k, v in authors.items()]


@app.get(
    "/authors/{authorId}", summary="Возвращает информацию о конкретном исполнителе"
)
async def get_author_info(authorId: int) -> Author:
    if authorId in authors: return authors[authorId]
    return JSONResponse(status_code=404, content={"message": "Item not found"})


@app.put(
    "/authors/{authorId}", summary="Обновляет информацию об исполнителе"
)
async def update_author(authorId: int, author: AuthorBase) -> Author:
    if authorId in authors:
        result = Author(
            **author.dict(), id=authorId, info=FAKE_AUTHOR_INFO
        )
        authors[authorId] = result
        return authors[authorId]
    return JSONResponse(status_code=404, content={"message": "Item not found"})


@app.delete("/authors/{authorId", summary="Удаляет исполнителя из базы")
async def delete_author(authorId: int) -> Author:
    if authorId in authors:
        del authors[authorId]
        return JSONResponse(status_code=200, content={"message": "Item successfully deleted"})
    return JSONResponse(status_code=404, content={"message": "Item not found"})

