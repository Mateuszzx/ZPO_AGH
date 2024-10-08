import unittest
from adjmat_to_adjlist import *


class TestFunctions(unittest.TestCase):
    def test_adjmat_to_adjlist(self):
        A = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 2, 0]
            ]
        B = [
            [0, 1],
            [0, 0]
        ]
        self.assertDictEqual(adjmat_to_adjlist(adjmat=A), {
                                                    1: [2],
                                                    2: [3],
                                                    3: [1, 2, 2]
                                                        })
        self.assertDictEqual(adjmat_to_adjlist(adjmat=B), {1: [2]
                                                        })

                                