import unittest
from tests import TestFunctions
import exercise


if __name__ == '__main__':

    G = {
            1: [2, 4],
            2: [3],
            4: [5],
            5: [2, 6],
            7: [1]
        }
        

    print(exercise.neighbors(G,1,2))
    unittest.main()
