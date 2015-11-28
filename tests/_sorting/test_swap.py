import unittest
import sort


class TestSwap(unittest.TestCase):
    """Tests swap function code. """

    def test_swap_empty(self):
        """Expects IndexError.

        :return:
        """
        with self.assertRaises(IndexError):
            sort.swap([], 0, 1)

    def test_swap_same_index(self):
        """Swap same index gracefully.

        :return:
        """
        l1 = [5]
        l2 = sort.swap(l1, 0, 0)
        self.assertEqual(l1, l2, "swap [x], 0, 0 does not equal [x]")

    def test_swap_legal(self):
        """

        :return:
        """
        l1 = [1, 2]
        l2 = sort.swap(l1, 0, 1)
        self.assertEqual(l1, [2, 1],
                         "swap [x, y], 0, 1 does not equal [y, x]")

    def test_swap_except(self):
        """

        :return:
        """
        l1 = [1, 2]
        with self.assertRaises(IndexError):
            sort.swap(l1, 0, 2)

