from typing import Any, Dict, List, Set
from collections import deque
class Graph:  
    def __init__(self): 
        self.adj: Dict[Any, List[Any]] = {} 
    def add_vertex(self, v: Any) -> None:
        self.adj.setdefault(v, [])
    def add_edge(self, u: Any, v: Any, directed: bool = False) -> None:
        self.add_vertex(u); self.add_vertex(v)
        self.adj[u].append(v)
        if not directed: self.adj[v].append(u)
    def neighbors(self, v: Any) -> List[Any]:
        return self.adj.get(v, [])
    def bfs(self, start: Any) -> List[Any]:
        if start not in self.adj: return []
        visited: Set[Any] = set([start]); q = deque([start]); order = []
        while q:
            node = q.popleft(); order.append(node)
            for nb in self.adj.get(node, []):
                if nb not in visited:
                    visited.add(nb); q.append(nb)
        return order
    def dfs(self, start: Any) -> List[Any]:
        visited: Set[Any] = set(); out = []
        def _dfs(node):
            visited.add(node); out.append(node)
            for nb in self.adj.get(node, []):
                if nb not in visited: _dfs(nb)
        if start in self.adj: _dfs(start)
        return out
    def __repr__(self):
        return '\n'.join(f"{k}: {v}" for k, v in self.adj.items())
