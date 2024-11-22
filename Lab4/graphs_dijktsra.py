#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, NamedTuple
import networkx as nx

VertexID = int
EdgeID = int

class TrailSegmentEntry(NamedTuple):
    start_id:   VertexID
    end_id:     VertexID
    edge_id:    EdgeID
    weight:     float

 
Trail = List[TrailSegmentEntry]

def load_multigraph_from_file(filename:str) -> nx.MultiDiGraph:
    """Stwórz multigraf na podstawie danych o krawędziach wczytanych z pliku.
 
    :param filepath: względna ścieżka do pliku (wraz z rozszerzeniem)
    :return: multigraf
    """

    G = nx.MultiDiGraph()
    with open(filename, mode ='r') as f:
        nodes = f.readlines()
        for n in nodes:
            vertex = n.lstrip()
            if vertex:
                vertex = vertex.split(" ")
                vertex1 = int(vertex[0].strip())
                vertex2 = int(vertex[1].strip())
                weight = float(vertex[2].strip())

                G.add_edge(vertex1, vertex2, weight=weight)

    return G

def find_min_trail(g: nx.MultiDiGraph, v_start: VertexID, v_end: VertexID) -> Trail:
    """Znajdź najkrótszą ścieżkę w grafie pomiędzy zadanymi wierzchołkami.
 
    :param g: graf
    :param v_start: wierzchołek początkowy
    :param v_end: wierzchołek końcowy
    :return: najkrótsza ścieżka
    """
    track = []
    trail  = nx.dijkstra_path(g, v_start, v_end)
    for t in range(len(trail)-1):
        for edge in range(len(g[trail[t]][trail[t+1]])):
            current_weight = g[trail[t]][trail[t + 1]][edge]['weight']
            x = TrailSegmentEntry(trail[t], trail[t + 1], edge, current_weight)
        track.append(x)
    return track
    
def trail_to_str(trail: Trail) -> str:
    """Wyznacz reprezentację tekstową ścieżki.
 
    :param trail: ścieżka
    :return: reprezentacja tekstowa ścieżki
    """
    total_weight = 0
    print(f"{trail[0].start_id}", end=" ")
    for t in trail:
            print(f"-[{t.edge_id}: {t.weight}]-> {t.end_id}", end=" ")
            total_weight += t.weight
    print(f" (total = {total_weight})")
    