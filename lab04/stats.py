"""Разбор и агрегирование наблюдений."""
def parse_record(line: str) -> dict:
    fields = line.strip().split(';')
    if len(fields) != 3:
        raise ValueError('Ожидались город, температура и дата')
    city, temperature, date = (part.strip() for part in fields)
    if not city or not date:
        raise ValueError('Город и дата не могут быть пустыми')
    try:
        temperature = float(temperature.replace(',', '.'))
    except ValueError as error:
        raise ValueError('Температура должна быть числом') from error
    return {'city': city, 'temperature': temperature, 'date': date}

def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records

def _means(records):
    totals, counts = {}, {}
    for record in records:
        city = record['city']
        totals[city] = totals.get(city, 0) + record['temperature']
        counts[city] = counts.get(city, 0) + 1
    return {city: total / counts[city] for city, total in totals.items()}

def average_by_city(records: list[dict]) -> dict:
    return {city: round(value, 1) for city, value in _means(records).items()}

def warmest_city(records: list[dict]) -> str:
    averages = _means(records)
    return min(averages, key=lambda city: (-averages[city], city), default='')
