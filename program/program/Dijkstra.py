from collections import defaultdict
from heapq import heappop, heappush  # Додано імпорт heapq


def session_catalog_routing(edges, f, t):
    """
    Реалізація маршрутизації на основі каталогів для сеансів.
    """
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    session_catalog = {}

    if (f, t) in session_catalog:
        print("Каталог:", session_catalog)  # Додано для перегляду каталогу
        return session_catalog[(f, t)]

    q, seen = [(0, f, ())], set()
    while q:
        cost, v1, path = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t:
                norm_path = reconstruct_path(path, [])
                session_catalog[(f, t)] = norm_path
                print("Каталог після оновлення:", session_catalog)  # Каталог після додавання маршруту
                return norm_path

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))

    print("Каталог після завершення:", session_catalog)  # Якщо маршрут не знайдено
    return []


def reconstruct_path(path, norm_path):
    """
    Відновлення маршруту з вкладеної структури.
    """
    if path[1] != ():
        norm_path.append(path[0])
        reconstruct_path(path[1], norm_path)
    else:
        norm_path.append(path[0])
        norm_path.reverse()
    return norm_path


# Приклад використання
edges = [
    ("A", "B", 1),
    ("B", "C", 2),
    ("A", "C", 2),
    ("C", "D", 1)
]

start = "A"
end = "D"
print(session_catalog_routing(edges, start, end))
