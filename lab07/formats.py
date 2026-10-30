"""Преобразования учебных CSV, YAML и JSON."""
import csv
import io
import json


def csv_to_records(text: str) -> list[dict]:
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    reader = csv.reader(io.StringIO('\n'.join(lines)))
    headers = [value.strip() for value in next(reader)]
    return [dict(zip(headers, (value.strip() for value in row))) for row in reader]


def _scalar(value):
    value = value.strip()
    if value.lower() in ('true', 'yes'):
        return True
    if value.lower() in ('false', 'no'):
        return False
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value


def parse_settings(lines: list[str]) -> dict:
    settings, current = {}, None
    for raw in lines:
        line = raw.split('#', 1)[0].strip()
        if not line:
            continue
        if line.startswith('- ') and current is not None:
            settings[current].append(_scalar(line[2:]))
        elif ':' in line:
            key, value = (part.strip() for part in line.split(':', 1))
            if value:
                settings[key] = _scalar(value)
                current = None
            else:
                settings[key] = []
                current = key
    return settings


def merge_by_key(rows: list[dict], extra: dict, key: str = 'id') -> list[dict]:
    return [{**extra.get(row.get(key), {}), **row} for row in rows]


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, sort_keys=True, indent=2)
