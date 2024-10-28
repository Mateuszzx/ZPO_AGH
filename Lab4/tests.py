import unittest
from exercise import *
import random

class TestFunctions(unittest.TestCase):
    def test_neighbors_distance_1(self):
        G = {
            1: [2, 4],
            2: [3],
            4: [5],
            5: [2, 6],
            7: [1]
        }
        
        expected_result = {2, 4}
        actual_result = neighbors(G, 1, 1)
        
        self.assertSetEqual(expected_result, actual_result)
        
    def test_neighbors_distance_2(self):
        G = {
            1: [2, 4],
            2: [3],
            4: [5],
            5: [2, 6],
            7: [1]
        }
        
        expected_result = {2, 3, 4, 5}
        actual_result = neighbors(G, 1, 2)
        
        self.assertSetEqual(expected_result, actual_result)

    def test_empty_list(self):
        self.assertEqual(quicksort([]), [])

    def test_single_element(self):
        self.assertEqual(quicksort([1]), [1])

    def test_already_sorted(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(quicksort([3, 1, 4, 1, 5, 9, 2]), [1, 1, 2, 3, 4, 5, 9])

    def test_list_with_duplicates(self):
        self.assertEqual(quicksort([3, 3, 3, 1, 1, 5, 9, 2, 5]), [1, 1, 2, 3, 3, 3, 5, 5, 9])

    def test_large_list(self):
        large_list = list(range(1000, 0, -1))
        sorted_list = list(range(1, 1001))
        self.assertEqual(quicksort(large_list), sorted_list)


LST_LEN = 1000
lst_sorted = [x for x in range(LST_LEN)]
lst_reverse_sorted = lst_sorted[::-1]
lst_equal = [1 for xx in range(LST_LEN)]
lst_random = random.sample( lst_sorted[:], LST_LEN)
lst_test = [5, 2, 3, 1, 4]

class TestFunctions2(unittest.TestCase):

    
    def test_quicksort(self):
        quick_sorted= quicksort(lst_sorted)
        quick_reverse  = quicksort(lst_reverse_sorted)
        quick_equal = quicksort(lst_equal)
        quick_random = quicksort(lst_random)
        
        self.assertListEqual(lst_sorted, quick_sorted)
        self.assertListEqual(lst_sorted,quick_reverse)
        self.assertListEqual(lst_equal, quick_equal)
        self.assertListEqual(lst_sorted, quick_random)
    