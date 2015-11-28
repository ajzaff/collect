from base_sort import SubSortTestMixin
import unittest
import sort
import random


class TestMergeInPlace(unittest.TestCase):
    """Test merge of sub-lists n-place. """

    sort_test = SubSortTestMixin('merge', sort.merge_in_place)

    def test_merge_empty(self):
        type(self).sort_test._test_empty(self)

    def test_merge_singleton(self):
        type(self).sort_test._test_empty(self)

    def test_pair(self):
        type(self).sort_test._test_pair(self)

    def test_small(self, small_list=None):
        if not small_list:
            small_list = type(self).sort_test._small_list()
            middle = len(small_list) // 2
            small_list = sorted(small_list[:middle]) + sorted(small_list[middle:])
        small_list_copy = small_list[:]
        res = type(self).sort_test.sort_func(small_list)
        expect = sorted(small_list)
        self.assertEqual(res, expect, '%s on %s does not return sorted list: %s' %
                       (type(self).sort_test.alg_name, small_list_copy, res))
        type(self).sort_test._test_in_place(self, small_list, res, True)

    def test_random_small(self, n=100):
        choices = range(100)
        for i in range(n):
            seq = [random.choice(choices) for i in range(10)]
            seq = sorted(seq[:5]) + sorted(seq[5:])
            self.test_small(small_list=seq)

