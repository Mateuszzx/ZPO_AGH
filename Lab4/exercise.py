from typing import List, Set, Dict
from collections import deque
from enum import Enum

class Colour(Enum):
    WHITE   = 0
    GREY    = 1
    BLACK   = 2


# Pomocnicza definicja podpowiedzi typu reprezentującego etykietę
# wierzchołka (liczba 1..n).
VertexID = int
 
# Pomocnicza definicja podpowiedzi typu reprezentującego listę sąsiedztwa.
AdjList = Dict[VertexID, List[VertexID]]
 
Distance = int


 
def neighbors(adjlist: AdjList, start_vertex_id: VertexID,
              max_distance: Distance) -> Set[VertexID]:
    colors = dict(zip(adjlist.keys(), [[Colour.WHITE, None] for x in adjlist.keys()]))
    colors[start_vertex_id] = [Colour.GREY, 0]
    Q = deque([start_vertex_id])
    neighbours = []
    while Q:
        u = Q.popleft()
        if colors[u][1] == max_distance:
            break
        
        for v in adjlist.get(u, []):
            if c := colors.get(v, []):
                if c[0] == Colour.WHITE:
                    colors[v][0] = Colour.GREY
                    colors[v][1] = colors[u][1] + 1
                    Q.append(v)
            neighbours.append(v)
        colors[u][0] = Colour.BLACK


    return set(neighbours)



def quicksort(in_array: List[int]) -> List[int]:

    len_in_array = len(in_array)
    out_array = in_array[:]
    quick_help_bfs(in_array=out_array, start=0, end = len_in_array-1)
    return out_array

def quick_help_bfs(in_array: List[int], start: int, end: int):
    
    Q = deque([(start, end)])

    while Q:
        start, end = Q.popleft()

        if start - end > 0:
            continue
        
        pivot = in_array[(start + end) // 2]
        i, j = start, end
        
        while i <= j:
            while in_array[i] < pivot:
                i += 1
            while in_array[j] > pivot:
                j -= 1

            if i <= j:
                in_array[i], in_array[j] = in_array[j], in_array[i]
                i += 1
                j -= 1
                
        if start < j:
            Q.append((start, j))
        if i < end:
            Q.append((i, end))