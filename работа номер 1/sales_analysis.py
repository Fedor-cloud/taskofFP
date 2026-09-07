"""Работа № 1 «Анализ продаж».

Функции для запуска:
    fedos_mak_parse_csv
    fedos_mak_compute_revenue
    fedos_mak_top_item

Решение не содержит import, def, ввода-вывода, мутации аргументов
и промежуточных присваиваний внутри вычислений.
"""


# str -> list[dict[str, str]]
fedos_mak_parse_csv = lambda data: (
    lambda lines: (
        []
        if not lines
        else (
            lambda headers: list(
                map(
                    lambda line: dict(
                        zip(
                            headers,
                            map(
                                lambda value: value.strip(),
                                line.split(","),
                            ),
                        )
                    ),
                    lines[1:],
                )
            )
        )(
            list(
                map(
                    lambda value: value.strip(),
                    lines[0].split(","),
                )
            )
        )
    )
)(
    list(
        filter(
            lambda line: line.strip() != "",
            data.splitlines(),
        )
    )
)


# list[dict[str, str]] -> float
fedos_mak_compute_revenue = lambda rows: sum(
    map(
        lambda row: float(row["quantity"]) * float(row["price"]),
        rows,
    ),
    0.0,
)


# list[dict[str, str]] -> dict[str, str] | None
fedos_mak_top_item = lambda rows: (
    None
    if not rows
    else dict(
        max(
            rows,
            key=lambda row: (
                float(row["quantity"]) * float(row["price"])
            ),
        )
    )
)
