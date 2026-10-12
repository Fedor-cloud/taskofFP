from functools import partial

fedos_mak_filter_by = (
    lambda key: lambda value: lambda items: list(
        filter(
            lambda item: key in item and item[key] == value,
            items
        )
    )
)

fedos_mak_filter_by_category = partial(
    lambda key, value: fedos_mak_filter_by(key)(value),
    "category"
)

fedos_mak_greater_than = lambda threshold: lambda x: x > threshold

print(
    "Товары категории fruit:",
    fedos_mak_filter_by_category("fruit")(
        [
            {"name": "apple", "category": "fruit"},
            {"name": "carrot", "category": "vegetable"},
            {"name": "banana", "category": "fruit"}
        ]
    )
)

print(
    "Числа больше 5:",
    list(filter(fedos_mak_greater_than(5), [1, 6, 8, 2, 9]))
)

"71cac7415394b4bc0efe0c87088731fa"
