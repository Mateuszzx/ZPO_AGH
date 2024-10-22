#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Dict, Optional

def dfs_recursive(G: Dict[int, List[int]], s: int) -> List[int]:
    def DFS_recursive(G: Dict[int, List[int]], s: int, visited: List[int]) -> List[int]:
        visited.append(s)
        
        for vertex in G.get(s,[]):
            if vertex not in visited:
                DFS_recursive(G=G, s=vertex, visited=visited)

    visited = []
    DFS_recursive(G,s,visited)
    return visited

def dfs_iterative(G: Dict[int, List[int]], s: int) -> List[int]:
    stack  =  [s]
    visited = []
    while stack:
        v = stack.pop(0)
        if v not in visited:
            visited.append(v)
            stack = [s for s in G[v] if s in G.keys() and s not in visited] + stack
    return visited
