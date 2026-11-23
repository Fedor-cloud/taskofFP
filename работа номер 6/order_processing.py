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
ORDER_TOTALS = lambda orders: list(map(lambda order: order["total"], orders))
# уровень 3—поиск заказа по id и получение суммы
# если заказ не найден next вернёт None
FIND_ORDER = lambda orders, order_id: next(
    filter(lambda order: order["id"] == order_id, orders), None
)
ORDER_TOTAL = lambda orders, order_id: (
    OptionalBox(FIND_ORDER(orders, order_id)).map(lambda order: order["total"]).value
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
print("Суммы:", ORDER_TOTALS(ORDERS))

# проверка уровня 2
print("map для 10:", OptionalBox(10).map(lambda value: value + 1).value)
print("map для None:", OptionalBox(None).map(lambda value: value + 1).value)

# проверка уровня 3
print("Заказ 2:", FIND_ORDER(ORDERS, 2))
print("Заказ 99:", FIND_ORDER(ORDERS, 99))
print("Сумма заказа 2:", ORDER_TOTAL(ORDERS, 2))
print("Сумма заказа 99:", ORDER_TOTAL(ORDERS, 99))
