"""Чистые функции для работы с путями и размерами."""
def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        name = path.rsplit('/', 1)[-1]
        extension = name.rsplit('.', 1)[1].lower() if '.' in name else ''
        counts[extension] = counts.get(extension, 0) + 1
    return counts

def deepest_path(paths: list[str]) -> str:
    return min(paths, key=lambda path: (-path.count('/'), path), default='')

def human_size(n_bytes: int) -> str:
    units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    size, index = n_bytes, 0
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1
    return f'{size:.0f} Б' if index == 0 else f'{size:.1f} {units[index]}'
