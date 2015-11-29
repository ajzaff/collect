import json
from tests.resources import get_res
import random


class BaseSortTestMixin(object):
    """Base class methods for sort test mixin. """

    _small_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    _small_iter = [2, 4, 10, 6, 8, 1, 9, 3, 7, 5]
    _small_size = len(_small_iter)

    with open(get_res('big_list.json', '_sorting'), 'rb') as f:
        _big_iter_json = json.load(f)
        _big_sorted = sorted(_big_iter_json)

    def __init__(self, alg_name, sort_func):
        """Initialized a _sorting tests.

        :param alg_name: (str) the name of this sorting algorithm
        :param sort_func: (function(iterable)) a sorting function
        """
        self.alg_name = alg_name
        self.sort_func = sort_func

    @classmethod
    def _small_list(cls):
        """Returns a new small list for use in _sorting.
        :return: (list)
        """
        return list(cls._small_iter)

    @classmethod
    def _random_small_list(cls, n=None, k=None):
        """Returns a new small list for use in _sorting.
        :return: (list)
        """
        if n is None:
            n = 10
        if k is None:
            k = n
        return [random.randrange(k) for i in range(n)]

    @classmethod
    def _big_list(cls):
        """Returns a new big list for use in _sorting.

        :return: (list)
        """
        return list(cls._big_iter_json)

    def _test_in_place(self, tc, iterable, res, print_res=True):
        """

        :param tc: (unittest.TestCase)
        :param iterable: (iterable) original iterable
        :param res: (iterable) result from sorting
        :return:
        """
        if print_res:
            tc.assertIs(iterable, res,
                        "%s is not In-place: %s" % (self.alg_name, res))
        else:
            tc.assertIs(iterable, res, "%s is not In-place: %s" % self.alg_name)


class SortTestMixin(BaseSortTestMixin):
    """Provides _sorting tests features. """

    def _test_empty(self, tc):
        """

        :param tc: (unittest.TestCase)
        :return:
        """
        l1 = []
        res = self.sort_func(l1)
        tc.assertEqual(res, [], '%s [] does not return []' % self.alg_name)
        self._test_in_place(tc, l1, res, True)

    def _test_singleton(self, tc):
        """

        :param tc: (unittest.TestCase)
        :return:
        """
        l1 = [5]
        res = self.sort_func(l1)
        tc.assertEqual(l1, l1, '%s [x] does not return [x]' % self.alg_name)
        self._test_in_place(tc, l1, res, True)

    def _test_pair(self, tc):
        """

        :param tc:
        :return:
        """
        l1 = [2, 1]
        l2 = [1, 2]
        l1_copy, l2_copy = l1[:], l2[:]
        res, res2 = self.sort_func(l1), self.sort_func(l2)
        expect, expect2 = sorted(l1), sorted(l2)
        tc.assertEqual(res, expect, '%s pair %s does not return expected: %s' %
                       (self.alg_name, l1_copy, expect))
        tc.assertEqual(res2, expect2, '%s pair %s does not return expected: %s' %
                       (self.alg_name, l2_copy, expect))
        self._test_in_place(tc, l1, res, print_res=True)
        self._test_in_place(tc, l2, res2, print_res=True)

    def _test_small(self, tc, small_list=None):
        """

        :param tc: (unittest.TestCase)
        :return:
        """
        if not small_list:
            small_list = self._small_list()
        small_list_copy = small_list[:]
        res = self.sort_func(small_list)
        expect = sorted(small_list)
        tc.assertEqual(res, expect, '%s on %s does not return sorted list: %s' %
                       (self.alg_name, small_list_copy, res))
        self._test_in_place(tc, small_list, res, True)

    def _test_random_small(self, tc, n=100):
        """

        :param tc:
        :return:
        """
        choices = range(100)
        for i in range(n):
            seq = [random.choice(choices) for i in range(10)]
            self._test_small(tc, small_list=seq)

    def _test_big(self, tc):
        """

        :param tc: (unittest.TestCase)
        :return:
        """
        big_list = self._big_list()
        res = self.sort_func(big_list)
        tc.assertEqual(res, type(self)._big_sorted,
                       '%s does not return sorted list' % self.alg_name)
        self._test_in_place(tc, big_list, res)


class SubSortTestMixin(SortTestMixin):
    """Mixin for sorts involving sub-sort slices. """

    def _test_empty_slice(self, tc):
        """

        :param tc: (unittest.TestCase)
        :return:
        """
        l1 = self._small_list()
        res = self.sort_func(l1, begin=2, end=2)
        tc.assertEqual(res, l1, '%s empty slice does not return original list' % self.alg_name)
        self._test_in_place(tc, l1, res, print_res=True)

    def _test_singleton_slice(self, tc):
        """

        :param tc: (unittest.TestCase)
        :return:
        """
        l1 = self._small_list()
        res = self.sort_func(l1, begin=2, end=3)
        tc.assertEqual(res, l1, '%s singleton slice does not return original list' % self.alg_name)
        self._test_in_place(tc, l1, res, print_res=True)

    def _test_begin_slice(self, tc, k=None):
        """

        :param tc: (unittest.TestCase)
        :return:
        """
        small_list = self._random_small_list()
        small_list_copy = small_list[:]
        if k is None:
            k = random.randrange(len(small_list))
        res = self.sort_func(small_list, end=k)
        expect = sorted(small_list_copy[:k]) + small_list_copy[k:]
        tc.assertEqual(res, expect,
                       '%s beginning slice %s[:%d] does not return expected result: %s' %
                       (self.alg_name, small_list_copy, k, expect))
        self._test_in_place(tc, small_list, res, print_res=True)

    def _test_random_begin_slice(self, tc, k=None):
        """

        :param tc: (unittest.TestCase)
        :return:
        """
        for i in range(100):
            self._test_begin_slice(tc)

    def _test_middle_slice(self, tc, i=None, k=None):
        """

        :param tc: (unittest.TestCase)
        :return:
        """
        small_list = self._random_small_list()
        small_list_copy = small_list[:]
        if i is None:
            i = random.randrange(len(small_list))
        if k is None:
            k = i + random.randrange(len(small_list)-i)
        res = self.sort_func(small_list, begin=i, end=k)
        expect = small_list_copy[:i] + sorted(small_list_copy[i:k]) + small_list_copy[k:]
        tc.assertEqual(res, expect,
                       '%s middle slice %s[%d:%d] does not return expected result: %s' %
                       (self.alg_name, small_list_copy, i, k, expect))
        self._test_in_place(tc, small_list, res, True)

    def _test_random_middle_slice(self, tc):
        """

        :param tc: (unittest.TestCase)
        :return:
        """
        for i in range(100):
            self._test_middle_slice(tc)

    def _test_end_slice(self, tc, i=None):
        """

        :param tc: (unittest.TestCase)
        :return:
        """
        small_list = self._random_small_list()
        small_list_copy = small_list[:]
        if i is None:
            i = random.randrange(len(small_list))
        res = self.sort_func(small_list, begin=i)
        expect = small_list_copy[:i] + sorted(small_list_copy[i:])
        tc.assertEqual(res, expect,
                       '%s end slice %s does not return expected result: %s' %
                       (self.alg_name, small_list_copy[i:], expect))
        self._test_in_place(tc, small_list, res, True)

    def _test_random_end_slice(self, tc):
        """

        :param tc: (unittest.TestCase)
        :return:
        """
        i = 4
        small_list = self._small_list()
        small_list_copy = small_list[:]
        res = self.sort_func(small_list, begin=i)
        expect = small_list_copy[:i] + sorted(small_list_copy[i:])
        tc.assertEqual(res, expect,
                       '%s end slice %s does not return expected result: %s' %
                       (self.alg_name, small_list_copy[i:], expect))
        self._test_in_place(tc, small_list, res, True)