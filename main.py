from fastapi import FastAPI
from pydantic import BaseModel

# FastAPI tətbiqi yaradırıq
app = FastAPI()
class RackRequest(BaseModel):
    rack1: str
    rack2: str

# Serveri işə salmaq üçün (Terminaldan)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


import math
import heapq
rack_coordinates = {
    # CR3
    'CR3 601': (0.8, 18.8),  'CR3 602': (1.6, 18.8),  'CR3 603': (2.4, 18.8),  'CR3 604': (3.2, 18.8),
    'CR3 605': (4.0, 18.8),  'CR3 606': (4.8, 18.8),  'CR3 607': (5.6, 18.8),  'CR3 608': (6.4, 18.8),
    'CR3 501': (0.8, 16.8),  'CR3 502': (1.6, 16.8),  'CR3 503': (2.4, 16.8),  'CR3 504': (3.2, 16.8),
    'CR3 505': (4.0, 16.8),  'CR3 506': (4.8, 16.8),  'CR3 507': (5.6, 16.8),  'CR3 508': (6.4, 16.8),
    'CR3 401': (0.6, 12.3),  'CR3 402': (1.2, 12.3),  'CR3 403': (2.0, 12.3),  'CR3 404': (2.8, 12.3),
    'CR3 405': (3.6, 12.3),  'CR3 406': (4.4, 12.3),  'CR3 407': (5.2, 12.3),  'CR3 408': (6.0, 12.3),
    'CR3 409': (6.8, 12.3),  'CR3 410': (7.6, 12.3),
    'CR3 301': (0.6, 10.35), 'CR3 302': (1.2, 10.35), 'CR3 303': (2.0, 10.35), 'CR3 304': (2.8, 10.35),
    'CR3 305': (3.6, 10.35), 'CR3 306': (4.4, 10.35), 'CR3 307': (5.2, 10.35), 'CR3 308': (6.0, 10.35),
    'CR3 309': (6.8, 10.35), 'CR3 310': (7.6, 10.35),
    'CR3 201': (0.6, 5.8),   'CR3 202': (1.2, 5.8),   'CR3 203': (2.0, 5.8),   'CR3 204': (2.8, 5.8),
    'CR3 205': (3.6, 5.8),   'CR3 206': (4.4, 5.8),   'CR3 207': (5.2, 5.8),   'CR3 208': (6.0, 5.8),
    'CR3 209': (6.8, 5.8),   'CR3 210': (7.6, 5.8),
    'CR3 101': (0.6, 3.65),  'CR3 102': (1.2, 3.65),  'CR3 103': (2.0, 3.65),  'CR3 104': (2.8, 3.65),
    'CR3 105': (3.6, 3.65),  'CR3 106': (4.4, 3.65),  'CR3 107': (5.2, 3.65),  'CR3 108': (6.0, 3.65),
    'CR3 109': (6.8, 3.65),  'CR3 110': (7.6, 3.65),

    # CR1
    'CR1 706': (1.7, 22),    'CR1 707': (3.2, 22),    'CR1 708': (3.8, 22),    'CR1 709': (5.0, 22),
    'CR1 710': (6.3, 22),    'CR1 701': (1.7, 24.5),  'CR1 702': (3.2, 24.5),  'CR1 703': (3.8, 24.5),
    'CR1 704': (5.0, 24.5),  'CR1 705': (6.3, 24.6),  'CR1 606': (1.7, 26.5),  'CR1 607': (3.2, 26.5),
    'CR1 608': (3.8, 26.5),  'CR1 609': (5.0, 26.5),  'CR1 610': (6.3, 26.5),  'CR1 601': (1.7, 29),
    'CR1 602': (3.2, 29),    'CR1 603': (3.8, 29),    'CR1 604': (5.0, 29),    'CR1 605': (6.3, 29),
    'CR1 506': (1.7, 31),    'CR1 507': (3.2, 31),    'CR1 508': (3.8, 31),    'CR1 509': (5.0, 31),
    'CR1 510': (6.3, 31),    'CR1 501': (1.7, 33.5),  'CR1 502': (3.2, 33.5),  'CR1 503': (3.8, 33.5),
    'CR1 504': (5.0, 33.5),  'CR1 505': (6.3, 33.5),  'CR1 406': (1.7, 35.5),  'CR1 407': (3.2, 35.5),
    'CR1 408': (3.8, 35.5),  'CR1 409': (5.0, 35.5),  'CR1 410': (6.3, 35.5),  'CR1 401': (1.7, 38),
    'CR1 402': (3.2, 38),    'CR1 403': (3.8, 38),    'CR1 404': (5.0, 38),    'CR1 405': (6.3, 38),

    # CR2
    'CR2 101': (14.8, 24),   'CR2 102': (15.8, 24),   'CR2 103': (16.6, 24),   'CR2 104': (17.4, 24),
    'CR2 105': (18.2, 24),   'CR2 106': (18.2, 26.5), 'CR2 107': (17.4, 26.5), 'CR2 108': (16.6, 26.5),
    'CR2 109': (15.8, 26.5), 'CR2 110': (14.8, 26.5),'CR2 201': (14.8, 29.5), 'CR2 202': (15.8, 29.5),
    'CR2 203': (16.6, 29.5), 'CR2 204': (17.4, 29.5), 'CR2 205': (18.2, 29.5), 'CR2 206': (18.2, 32),
    'CR2 207': (17.4, 32),   'CR2 208': (16.6, 32),   'CR2 209': (15.8, 32),   'CR2 210': (14.8, 32),
    'CR2 301': (14.8, 35),   'CR2 302': (15.8, 35),   'CR2 303': (16.6, 35),   'CR2 304': (17.4, 35),
    'CR2 305': (18.2, 35),   'CR2 306': (18.2, 37.5), 'CR2 307': (17.4, 37.5), 'CR2 308': (16.6, 37.5),
    'CR2 309': (15.8, 37.5), 'CR2 310': (14.8, 37.5),
}
# Tray and panel heights (meters) and turn addition (meters)
TRAY_HEIGHT = 3.15
PANEL_HEIGHT = 2.0
TURN_ADDITION = 0.2

LATERAL_GROUPS = {
    # CR3
    'CR3 602': ['CR3 601','CR3 602','CR3 603','CR3 604','CR3 605','CR3 606','CR3 607','CR3 608'],
    'CR3 502': ['CR3 501','CR3 502','CR3 503','CR3 504','CR3 505','CR3 506','CR3 507','CR3 508'],
    'CR3 402': ['CR3 401','CR3 402','CR3 403','CR3 404','CR3 405','CR3 406','CR3 407','CR3 408','CR3 409','CR3 410'],
    'CR3 302': ['CR3 301','CR3 302','CR3 303','CR3 304','CR3 305','CR3 306','CR3 307','CR3 308','CR3 309','CR3 310'],
    'CR3 202': ['CR3 201','CR3 202','CR3 203','CR3 204','CR3 205','CR3 206','CR3 207','CR3 208','CR3 209','CR3 210'],
    'CR3 102': ['CR3 101','CR3 102','CR3 103','CR3 104','CR3 105','CR3 106','CR3 107','CR3 108','CR3 109','CR3 110'],
    # CR1
    'CR1 405': ['CR1 404','CR1 405','CR1 403','CR1 402','CR1 401'],
    'CR1 410': ['CR1 410','CR1 409','CR1 408','CR1 407','CR1 406'],
    'CR1 505': ['CR1 504','CR1 503','CR1 502','CR1 501','CR1 505'],
    'CR1 510': ['CR1 509','CR1 508','CR1 507','CR1 506','CR1 510'],
    'CR1 605': ['CR1 604','CR1 603','CR1 602','CR1 601','CR1 605'],
    'CR1 610': ['CR1 609','CR1 608','CR1 607','CR1 606','CR1 610'],
    'CR1 705': ['CR1 704','CR1 703','CR1 702','CR1 701','CR1 705'],
    'CR1 710': ['CR1 709','CR1 708','CR1 707','CR1 706','CR1 710'],
    # CR2
    'CR2 101': ['CR2 101','CR2 102','CR2 103','CR2 104','CR2 105'],
    'CR2 110': ['CR2 109','CR2 108','CR2 107','CR2 106','CR2 110'],
    'CR2 201': ['CR2 201','CR2 202','CR2 203','CR2 204','CR2 205'],
    'CR2 210': ['CR2 209','CR2 208','CR2 207','CR2 206','CR2 210'],
    'CR2 301': ['CR2 301','CR2 302','CR2 303','CR2 304','CR2 305'],
    'CR2 310': ['CR2 309','CR2 308','CR2 307','CR2 306','CR2 310'],
}
# — Main tray path including CR1 707 —
MAIN_PATH = [
    'CR3 102',
    'CR3 202',
    'CR3 302',
    'CR3 402',
    'CR3 502',
    'CR3 602',
    'CR1 707',  # added here
    'CR1 710',
    'CR1 705', 'CR1 610','CR1 605','CR1 510','CR1 505','CR1 410','CR1 405',
    'CR2 110', 'CR2 101', 'CR2 201', 'CR2 210', 'CR2 301', 'CR2 310'
]

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

@app.post("/tray_yolu/")
async def tray_yolu_hesabla(request: RackRequest):
    try:
        dist = calculate_tray_distance(
            request.rack1,
            request.rack2,
            rack_coordinates,
            MAIN_PATH,
            LATERAL_GROUPS,
            TRAY_HEIGHT
        )
        return {
            "tray_yolu": f"{request.rack1} → {request.rack2} məsafə: {dist:.2f} m",
            "yuvarlaq": f"{math.ceil(dist / 5) * 5} m"
        }
    except Exception as e:
        return {"xeta": str(e)}

