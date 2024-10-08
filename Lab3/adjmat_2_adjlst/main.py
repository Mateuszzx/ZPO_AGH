#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from adjmat_test import TestFunctions
from adjmat_to_adjlist import *

if __name__ == '__main__':
    A = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 2, 0]
            ]
    B = [
        [0, 1],
        [0, 0]
    ]
    print(adjmat_to_adjlist(A))
    print(adjmat_to_adjlist(B))
    unittest.main()
    