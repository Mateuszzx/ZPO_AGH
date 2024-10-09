#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Dict, Optional

def dfs_recursive(G: Dict[int, List[int]], s: int, visited: Optional[List[int]] = None) -> List[int]:
    if visited is None:
        visited = []
    visited.append(s)
    print(visited)
    print(len(visited), len(G.keys()))
    if len(visited) == len(G.keys()):
        return visited
    for vertex in G[s]:
        if vertex not in visited:
            dfs_recursive(G=G, s=vertex, visited=visited)


def dfs_iterative(G: Dict[int, List[int]], s: int) -> List[int]:
    pass
