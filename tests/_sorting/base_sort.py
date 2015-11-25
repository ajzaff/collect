import json
from tests.resources import get_res


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
    def _big_list(cls):
        """Returns a new big list for use in _sorting.

        :return: (list)
        """
        return list(cls._big_iter_json)


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
        tc.assertEqual(l1, [5], '%s [x] does not return [x]' % self.alg_name)
        self._test_in_place(tc, l1, res, True)

    def _test_small(self, tc):
        """

        :param tc: (unittest.TestCase)
        :return:
        """
        small_list = self._small_list()
        res = self.sort_func(small_list)
        tc.assertEqual(res, type(self)._small_sorted,
                       '%s does not return sorted list: %s' % (self.alg_name, res))
        self._test_in_place(tc, small_list, res, True)

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

    def _test_in_place(self, tc, iterable, res, print_res=True):
        """

        :param tc: (unittest.TestCase)
        :param iterable: (iterable) original iterable
        :param res: (iterable) result from sorting
        :return:
        """
        if print_res:
            tc.assertIs(iterable, res,
                        "%s does not sort in-place: %s" % (self.alg_name, res))
        else:
            tc.assertIs(iterable, res, "%s does not sort in-place: %s" % self.alg_name)


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

    def _test_begin_slice(self, tc):
        """

        :param tc: (unittest.TestCase)
        :return:
        """
        k = 4
        small_list = self._small_list()
        res = self.sort_func(small_list, end=k)
        expect = sorted(small_list[:k]) + small_list[k:]
        tc.assertEqual(res, expect,
                       '%s beginning slice %s does not return expected result: %s' %
                       (self.alg_name, small_list[:k], expect))
        self._test_in_place(tc, small_list, res, print_res=True)

    def _test_middle_slice(self, tc):
        """

        :param tc: (unittest.TestCase)
        :return:
        """
        i = 3
        k = 7
        small_list = self._small_list()
        res = self.sort_func(small_list, begin=i, end=k)
        expect = small_list[:i] + sorted(small_list[i:k]) + small_list[k:]
        tc.assertEqual(res, expect,
                       '%s middle slice %s does not return expected result: %s' %
                       (self.alg_name, small_list[i:k], expect))
        self._test_in_place(tc, small_list, res, True)

    def _test_end_slice(self, tc):
        """

        :param tc: (unittest.TestCase)
        :return:
        """
        i = 4
        small_list = self._small_list()
        res = self.sort_func(small_list, begin=i)
        expect = small_list[:i] + sorted(small_list[i:])
        tc.assertEqual(res, expect,
                       '%s end slice %s does not return expected result: %s' %
                       (self.alg_name, small_list[i:], expect))
        self._test_in_place(tc, small_list, res, True)