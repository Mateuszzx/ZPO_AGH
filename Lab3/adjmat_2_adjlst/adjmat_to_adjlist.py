from typing import List, Dict


def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    dct = {}
    for i,row in enumerate(adjmat):
        for j,elem in enumerate(row):
            if elem:
                if(corner := dct.get(i+1)) is None:
                    dct[i+1] = corner = []
                
                corner.extend([(j+1) for x in range(elem)])      
    return dct
