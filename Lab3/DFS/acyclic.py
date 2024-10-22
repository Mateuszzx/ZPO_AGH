#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Dict
from DFS.dfs import dfs_iterative

def is_acyclic(G: Dict[int, List[int]]) -> bool:
    
    def cyclic(G: Dict[int, List[int]], v: int, visited: List[int]) -> bool:
        visited.append(v)
        if v in G.keys():
            for vertex in G[v]:
                if vertex in visited:
                    return True
                elif cyclic(G, vertex, visited[:]):
                    return True
        return False

    
    for key in G.keys():
        if cyclic(G, key, []):
            return False
    return True

