"""Потоковая обработка текстового журнала."""
from collections import Counter

def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3 or parts[1] not in {'DEBUG', 'INFO', 'WARNING', 'ERROR'}:
        raise ValueError('Ожидались время, известный уровень и сообщение')
    return dict(zip(('time', 'level', 'message'), parts))

def count_levels(lines) -> dict:
    counts = Counter()
    for line in lines:
        if not line.strip():
            continue
        try:
            level = parse_event(line)['level']
        except ValueError:
            level = 'BROKEN'
        counts[level] += 1
    return dict(counts)

def top_errors(lines, n: int) -> list[list]:
    counts = Counter()
    for line in lines:
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event['level'] == 'ERROR':
            counts[event['message']] += 1
    return [[message, count] for message, count in
            sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:max(0, n)]]

def format_report(counts: dict, errors: list[list]) -> str:
    lines = ['Отчёт по журналу', '']
    lines.extend(f'{level}: {counts[level]}' for level in sorted(counts))
    lines.extend(['', 'Частые ошибки:'])
    lines.extend(f'- {message} — {count}' for message, count in errors)
    return '\n'.join(lines) + '\n'
