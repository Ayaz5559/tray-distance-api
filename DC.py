import math
import heapq
from data import *

def round_up_to_nearest_5(x):
        return math.ceil(x / 5) * 5

# === INTERACTIVE CLI ===
def build_graph(rack_coordinates, main_path, lateral_groups, tray_height):
    graph = {}
    for i, rid in enumerate(main_path):
        graph[('main', i)] = []
    for i in range(len(main_path) - 1):
        a, b = main_path[i], main_path[i + 1]
        x1, y1 = rack_coordinates[a]
        x2, y2 = rack_coordinates[b]
        dist = math.hypot(x2 - x1, y2 - y1) + TURN_ADDITION
        graph[('main', i)].append((('main', i + 1), dist))
        graph[('main', i + 1)].append((('main', i), dist))
    for i, rid in enumerate(main_path):
        main_node = ('main', i)
        bx, by = rack_coordinates[rid]
        for lrid in lateral_groups.get(rid, []):
            graph.setdefault(('rack', lrid), [])
            rx, ry = rack_coordinates[lrid]
            horizontal = math.hypot(rx - bx, ry - by)
            vertical = abs(tray_height - PANEL_HEIGHT)
            d = horizontal + vertical
            graph[('rack', lrid)].append((main_node, d))
            graph[main_node].append((('rack', lrid), d))
    return graph

def calculate_tray_distance(r1, r2,
                             rack_coordinates,
                             main_path,
                             lateral_groups,
                             tray_height):
    graph = build_graph(rack_coordinates, main_path, lateral_groups, tray_height)
    src = ('rack', r1)
    dst = ('rack', r2)
    dist_map = {src: 0.0}
    pq = [(0.0, src)]
    visited = set()

    while pq:
        curr_d, node = heapq.heappop(pq)
        if node == dst:
            return curr_d
        if node in visited:
            continue
        visited.add(node)
        for nbr, w in graph.get(node, []):
            nd = curr_d + w
            if nd < dist_map.get(nbr, float('inf')):
                dist_map[nbr] = nd
                heapq.heappush(pq, (nd, nbr))
    raise ValueError(f"Tray yolu tapılmadı: {r1} → {r2}")

# === İNTERAKTİV İSTİFADƏ ===
if __name__ == '__main__':
    while True:
        try:
            r1 = input("Başlanğıc rack kodunu daxil et: ").strip()
            r2 = input("Hədəf rack kodunu daxil et: ").strip()

            try:
                dist = calculate_tray_distance(
                    r1, r2,
                    rack_coordinates,
                    MAIN_PATH,
                    LATERAL_GROUPS,
                    TRAY_HEIGHT
                )
            except Exception as e:
                print(f"Xəta: {e}")
                continue

            print(f"Dəqiq məsafə: {dist:.2f} metr")
            print(f"Yuvarlaqlaşdırılmış: {round_up_to_nearest_5(dist)} m")

        except KeyboardInterrupt:
            print("\nÇıxış edilir…")
            sys.exit()
