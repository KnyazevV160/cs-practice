"""Прочитать журнал со стандартного ввода и напечатать сводку."""
import sys
from stats import average_by_city, read_valid, warmest_city


def main():
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)
    broken = sum(bool(line.strip()) for line in lines) - len(records)
    averages = average_by_city(records)
    print(len(records))
    print(broken)
    print(f'{averages.get(warmest_city(records), 0):.1f}')


if __name__ == '__main__':
    main()
