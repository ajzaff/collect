# -*- coding: utf-8 -*-
import gc


def bubble_sort(iterable):
    """Sort the iterable In-place.

    :param iterable: (iterable) an iterable to sort
    :return (iterable): the original object
    """
    def bubble_pairs():
        """Yields bubble-pairs for bubble _sorting.

        :param iterable: (iterable) an iterable
        :return (tuple(int,int)): bubble pair tuple indexes
        """
        for i in range(len(iterable)-1):
            yield i, i+1

    # Loop through all bubble pairs
    # Until ordered.
    unordered = True
    while unordered:
        unordered = False
        for i, j in bubble_pairs():
            if iterable[j] < iterable[i]:
                swap(iterable, i, j)
                unordered = True

    return iterable


def swap(iterable, i, j):
    """Swap In-place.

    :param iterable: (iterable) an iterable
    :param i: (int) the first index
    :param j: (int) the second index
    :return (iterable): the original object
    :throws IndexError: i, j index out of range
    """
    t = iterable[i]
    iterable[i] = iterable[j]
    iterable[j] = t
    return iterable


def merge_sort(iterable, begin=None, end=None):
    """Merge-sort In-place.

    :param iterable: (iterable) iterable object to sort
    :param begin:
    :param end:
    :return: (iterable) the sorted iterable object
    """
    def rec_split(i, k):
        """

        :param i:
        :param k:
        :return:
        """
        if k - i < 2:
            return
        m = (k-i) // 2

    if begin is None:
        begin = 0
    if end is None:
        end = len(iterable)
    rec_split(begin, end)
    return iterable


def merge_in_place(iterable, begin=None, end=None):
    """Merges sorted sub-lists into one sorted list In-place.

    :param iterable: (iterable)
    :param begin:
    :param end:
    :return:
    """
    if begin is None:
        begin = 0
    if end is None:
        end = len(iterable)
    if end - begin > 1:
        middle = (end-begin) // 2
        b = []
        i = begin
        j = middle
        gc.disable()
        while i < middle and j < end:
            if iterable[i] <= iterable[j]:
                b.append(iterable[i])
                i += 1
            else:
                b.append(iterable[j])
                j += 1
        gc.enable()
        if middle - i > 0:
            b.append(iterable[i])
        elif end - j > 0:
            b.append(iterable[j])
        iterable[begin:end] = b
    return iterable


def insertion_sort(iterable, begin=None, end=None):
    """Insertion sort In-place, O(N) space.

    :param iterable: (iterable) an iterable to sort
    :param begin: (int) begin index; default: 0
    :param end: (int) end index; default: len(iterable)
    :return: (iterable) the sorted object
    """
    if begin is None:
        begin = 0
    if end is None:
        end = len(iterable)
    if end-begin > 1:
        for i, e in enumerate(iterable[:end-1]):
            j = i + 1
            while j > begin and iterable[j-1] > iterable[j]:
                swap(iterable, j, j-1)
                j -= 1
    return iterable

if __name__ == '__main__':
    x = [0, 3, 5, 7, 0, 4, 6, 9]
    merge_in_place(x)
    print x