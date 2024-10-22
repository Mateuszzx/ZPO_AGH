import unittest
import random
from exercise import bubblesort,quicksort



LST_LEN = 1000
lst_sorted = [x for x in range(LST_LEN)]
lst_reverse_sorted = lst_sorted[::-1]
lst_equal = [1 for xx in range(LST_LEN)]
lst_random = random.sample( lst_sorted[:], LST_LEN)
lst_test = [5, 2, 3, 1, 4]

class TestFunctions(unittest.TestCase):
    def test_bubblesort(self):
        bub_sorted, comp_sorted = bubblesort(lst_sorted)
        bub_reverse, comp_reverse  = bubblesort(lst_reverse_sorted)
        bub_equal, comp_equal = bubblesort(lst_equal)
        bub_random, comp_random = bubblesort(lst_random)
        _, comp_test = bubblesort(lst_test)
        self.assertListEqual(lst_sorted, bub_sorted)
        self.assertListEqual(lst_sorted,bub_reverse)
        self.assertListEqual(lst_equal, bub_equal)
        self.assertListEqual(lst_sorted, bub_random)
        self.assertEqual(comp_sorted, LST_LEN-1)
        self.assertEqual(comp_equal, LST_LEN-1)
        self.assertEqual(comp_test, 10)
        self.assertEqual(comp_reverse, LST_LEN*(LST_LEN-1)/2)
        self.assertLessEqual(comp_random, LST_LEN*(LST_LEN-1)/2)
        self.assertGreaterEqual(comp_random, 0)

    
    def test_quicksort(self):
        quick_sorted= quicksort(lst_sorted)
        quick_reverse  = quicksort(lst_reverse_sorted)
        quick_equal = quicksort(lst_equal)
        quick_random = quicksort(lst_random)
        
        self.assertListEqual(lst_sorted, quick_sorted)
        self.assertListEqual(lst_sorted,quick_reverse)
        self.assertListEqual(lst_equal, quick_equal)
        self.assertListEqual(lst_sorted, quick_random)
    