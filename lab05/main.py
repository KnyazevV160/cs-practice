"""Два прохода по журналу без загрузки всего файла в память."""
from pathlib import Path
from logstats import count_levels, top_errors, format_report


def main():
    path = Path(input().strip())
    if not path.is_absolute() and not path.exists():
        path = Path(__file__).parent / path
    with open(path, encoding='utf-8') as log:
        counts = count_levels(log)
    with open(path, encoding='utf-8') as log:
        errors = top_errors(log, 3)
    report = Path(__file__).parent / 'report.txt'
    with open(report, 'w', encoding='utf-8', newline='\n') as output:
        output.write(format_report(counts, errors))
    print(sum(counts.values()))
    print(counts.get('ERROR', 0))
    print(counts.get('BROKEN', 0))


if __name__ == '__main__':
    main()
