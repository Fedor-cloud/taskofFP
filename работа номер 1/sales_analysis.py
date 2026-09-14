# Работа № 1 «Анализ продаж»



Fedos_mak_parse_csv = lambda data: (
    lambda lines: [] if not lines else (
        lambda headers: list(map(
            lambda line: dict(zip(
                headers,
                map(lambda value: value.strip(), line.split(","))
            )),
            lines[1:]
        ))
    )(list(map(lambda value: value.strip(), lines[0].split(","))))
)(list(filter(lambda line: line.strip() != "", data.splitlines())))



Fedos_mak_compute_revenue = lambda rows: sum(
    map(lambda row: float(row["quantity"]) * float(row["price"]), rows),
    0.0
)



Fedos_mak_top_item = lambda rows: (
    None if not rows else dict(
        max(rows, key=lambda row: float(row["quantity"]) * float(row["price"]))
    )
)