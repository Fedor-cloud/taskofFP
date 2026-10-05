from dataclasses import dataclass
from enum import Enum
from typing import Generic, TypeVar, Union

T = TypeVar("T")
E = TypeVar("E")

class FedosMakLoadState(Enum):
    LOADING = "loading"
    SUCCESS = "success"
    ERROR = "error"

@dataclass(frozen=True)
class FedosMakUser:
    name: str
    age: int
    email: str

@dataclass(frozen=True)
class FedosMakSuccess(Generic[T]):
    value: T

@dataclass(frozen=True)
class FedosMakFailure(Generic[E]):
    error: E

FedosMakResult = Union[FedosMakSuccess[T], FedosMakFailure[E]]

def fedos_mak_load_users() -> FedosMakResult[list[FedosMakUser], str]:
    return (
        lambda users: (
            FedosMakSuccess(
                list(
                    map(
                        lambda user: FedosMakUser(*user),
                        users
                    )
                )
            )
            if users
            else FedosMakFailure("Список пользователей пуст")
        )
    )(
        (
            ("Анна", 20, "anna@example.com"),
            ("Иван", 25, "ivan@example.com"),
            ("Мария", 22, "maria@example.com")
        )
    )

print("Состояния загрузки:", list(FedosMakLoadState))
print("Результат загрузки:", fedos_mak_load_users())

"""cee045e9ebfb99b520cd2e4b4629b282""" 