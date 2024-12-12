from collections import defaultdict
from heapq import heappop, heappush


def session_catalog_routing(edges, f, t):

    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    session_catalog = {}

    if (f, t) in session_catalog:
        print("Catalog:", session_catalog)
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
                print("Catalog after update:", session_catalog)
                return norm_path

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))

    print("Catalog after finish:", session_catalog)
    return []


def reconstruct_path(path, norm_path):

    if path[1] != ():
        norm_path.append(path[0])
        reconstruct_path(path[1], norm_path)
    else:
        norm_path.append(path[0])
        norm_path.reverse()
    return norm_path






