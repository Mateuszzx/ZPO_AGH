from typing import List, Dict


def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    dct = {}
    for i,row in enumerate(adjmat):
        for j,elem in enumerate(row):
            if elem:
                for k in range(elem):
                    dct[i].append(j) 

    return dct
