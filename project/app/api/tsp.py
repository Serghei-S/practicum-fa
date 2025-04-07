from fastapi import APIRouter, HTTPException
from app.schemas.graph import GraphRequest, PathResult
from app.services.tsp import dijkstra

router = APIRouter()

@router.post("/shortest-path/", response_model=PathResult)
def shortest_path(request: GraphRequest):
    nodes = request.graph.nodes
    edges = request.graph.edges
    path, total_distance = dijkstra(nodes, edges, request.start, request.end)
    if not path:
        raise HTTPException(status_code=404, detail="Путь не найден")
    return {"path": path, "total_distance": float(total_distance)}
