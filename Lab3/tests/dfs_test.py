import unittest
from DFS.dfs import *

G1 = {
1: [2, 3, 5],
2: [1, 4, 6],
3: [1, 7],
4: [2],
5: [1, 6],
6: [2, 5],
7: [3]
}
G2 = {
1: [2, 3, 5],
2: [1, 4, 6],
3: [1, 7],
4: [2],
5: [1, 6],
6: [2, 5],
7: [3]
}

result1 = [1, 2, 4, 6, 5, 3, 7]
result2 = [1, 2, 4, 6, 5, 3, 7]

class TestFunctions2(unittest.TestCase):

    def test_dfs_recursive(self):
        self.assertListEqual(dfs_recursive(G2,1), result1)

    
    def test_dfs_iterative(self):
        self.assertListEqual(dfs_iterative(G2,1), result2)

    