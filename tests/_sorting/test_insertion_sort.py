from base_sort import SubSortTestMixin
import unittest
import sorting


class TestInsertionSort(unittest.TestCase):
    """Test sorting method. """

    sort_test = SubSortTestMixin('insertion sort', sorting.insertion_sort)

    def test_empty(self):
        type(self).sort_test._test_empty(self)

    def test_singleton(self):
        type(self).sort_test._test_singleton(self)

    def test_pair(self):
        type(self).sort_test._test_pair(self)

    def test_small(self):
        type(self).sort_test._test_small(self)

    def test_random_small(self):
        type(self).sort_test._test_random_small(self)

    def test_big(self):
        type(self).sort_test._test_big(self)

    def test_empty_slice(self):
        type(self).sort_test._test_empty_slice(self)

    def test_singleton_slice(self):
        type(self).sort_test._test_singleton_slice(self)

    def test_begin_slice(self):
        type(self).sort_test._test_begin_slice(self)

    def test_middle_slice(self):
        type(self).sort_test._test_middle_slice(self)

    def test_end_slice(self):
        type(self).sort_test._test_end_slice(self)