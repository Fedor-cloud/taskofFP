from collections import namedtuple

# уроень  2—OptionalBox с методом map
class OptionalBox(namedtuple("OptionalBox", ["value"])):
    __slots__ = ()  # без дополнительных атрибутов

    # None пропускаем, результат кладём в новый контейнер
    map = lambda self, function: OptionalBox(
        None if self.value is None else function(self.value)
    )

ORDERS = [
    {"id": 1, "total": 1500, "status": "new"},
    {"id": 2, "total": 3200, "status": "paid"},
    {"id": 3, "total": 0, "status": "cancelled"}
]

# уровень 1—суммы заказов через map
# суммы вычисляются только при переборе
ORDER_TOTALS = lambda orders: map(lambda order: order["total"], orders)
# уровень 3—поиск заказа по id и получение суммы
# если заказ не найден next вернёт None
# первый вызов запоминает orders, второй запускает поиск
FIND_ORDER = lambda orders: lambda order_id: next(
    filter(lambda order: order["id"] == order_id, orders), None
)
ORDER_TOTAL = lambda orders: lambda order_id: (
    OptionalBox(FIND_ORDER(orders)(order_id)).map(lambda order: order["total"]).value
)
# уровень 4—законы тождества и композиции
IDENTITY = lambda value: value
F = lambda value: value + 1
G = lambda value: value * 2

print(
    "Тождество:",
    OptionalBox(10).map(IDENTITY) == OptionalBox(10)
    and OptionalBox(None).map(IDENTITY) == OptionalBox(None)
)
# G(F(value)):сначала F, потом G
print(
    "Композиция:",
    OptionalBox(10).map(F).map(G) == OptionalBox(10).map(lambda value: G(F(value)))
    and OptionalBox(None).map(F).map(G) == OptionalBox(None).map(lambda value: G(F(value)))
)

# проверка уровня 1
print("Суммы:", *ORDER_TOTALS(ORDERS))

# проверка уровня 2
print("map для 10:", OptionalBox(10).map(lambda value: value + 1).value)
print("map для None:", OptionalBox(None).map(lambda value: value + 1).value)

# проверка уровня 3
# сохраняем функции, поиск пока не выполняется

FIND_BY_ID = FIND_ORDER(ORDERS)
TOTAL_BY_ID = ORDER_TOTAL(ORDERS)


# передаём id и запускаем вычисление
print("Заказ 2:", FIND_BY_ID(2))
print("Заказ 99:", FIND_BY_ID(99))
print("Сумма заказа 2:", TOTAL_BY_ID(2))
print("Сумма заказа 99:", TOTAL_BY_ID(99))
print("Заказ 94:", FIND_BY_ID(94))
# ab 6 зачтено 48b5bc5ea82bc934d927592d90184fc92774217df3e4122cfd69c0b414ca915e