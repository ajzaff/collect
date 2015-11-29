import unittest
import sort


class TestPivot(unittest.TestCase):

    def test_last_pivot_empty(self):
        l1 = []
        res = sort.last_pivot(l1)
        expect = None
        self.assertEqual(res, expect,
                         "the pivot of %s is %s expected: %s" %
                         (l1, res, expect))

    def test_last_pivot_normal(self):
        l1 = [1, 2, 3, 4, 5, 6, 7]
        res = sort.last_pivot(l1)
        expect = len(l1)-1
        self.assertEqual(res, expect,
                         "the pivot of %s is %s expected: %s" %
                         (l1, res, expect))