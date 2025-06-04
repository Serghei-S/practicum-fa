import heapq
from typing import List, Dict, Tuple


def dijkstra(nodes: List[int], edges: List[List[float]], start: int, end: int) -> Tuple[List[int], float]:
    graph: Dict[int, List[Tuple[int, float]]] = {node: [] for node in nodes}
    for u, v, w in edges:
        graph[u].append((v, w))

    distances = {node: float('inf') for node in nodes}
    previous = {node: None for node in nodes}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))

    # Восстановление пути
    path = []
    current = end
    if distances[end] == float('inf'):
        return [], float('inf')
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path, distances[end]
