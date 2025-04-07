from pydantic import BaseModel
from typing import List

class Graph(BaseModel):
    nodes: List[int]
    edges: List[List[float]]  # каждая грань описывается как [начало, конец, вес]

class GraphRequest(BaseModel):
    graph: Graph
    start: int
    end: int

class PathResult(BaseModel):
    path: List[int]
    total_distance: float
