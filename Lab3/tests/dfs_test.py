import unittest
from DFS.dfs import *

class TestFunctions2(unittest.TestCase):
    G = {
    1: [2, 3, 5],
    2: [1, 4, 6],
    3: [1, 7],
    4: [2],
    5: [1, 6],
    6: [2, 5],
    7: [3]
    }

    result = [1, 2, 4, 6, 5, 3, 7]
    def test_dfs_recursive(self):
        self.assertListEqual(dfs_recursive(self.G,1), self.result)

    
    def test_dfs_iterative(self):
        self.assertListEqual(dfs_iterative(self.G,1), self.result)
