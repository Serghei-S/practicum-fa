from typing import List, Tuple

from celery.result import AsyncResult

from app.core.core import app
from app.services.tsp import dijkstra


@app.task
def dijkstra_task(nodes: List[int], edges: List[List[float]], start: int, end: int) -> Tuple[List[int], float]:
    return dijkstra(nodes, edges, start, end)


def dijkstra_result(task_id: str):
    return AsyncResult(task_id, app=app)
