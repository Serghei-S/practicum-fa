from fastapi import APIRouter
from app.schemas.graph import GraphRequest
from app.tasks.tasks import dijkstra_result, dijkstra_task

router = APIRouter()


@router.post("/shortest-path/")
def shortest_path(request: GraphRequest):
    nodes = request.graph.nodes
    edges = request.graph.edges

    task = dijkstra_task.delay(nodes, edges, request.start, request.end)
    return {"task_id": task.id}


@router.get("/shortest-path/{task_id}/status")
async def shortest_path_status(task_id: str):
    result = dijkstra_result(task_id)
    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result if result.successful() else None
    }
