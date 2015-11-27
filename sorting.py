# -*- coding: utf-8 -*-
import gc


def bubble_sort(iterable):
    """Sort the iterable In-place.

    :param iterable: (iterable) an iterable to sort
    :return (iterable): the original object
    """
    unordered = True
    while unordered:
        unordered = False
        for i in range(len(iterable)-1):
            if iterable[i] > iterable[i+1]:
                swap(iterable, i, i+1)
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
    if begin is None:
        begin = 0
    if end is None:
        end = len(iterable) - 1
    if begin < end:
        middle = begin + (end - begin) // 2
        merge_sort(iterable, begin=begin, end=middle)
        merge_sort(iterable, begin=middle+1, end=end)
        merge_in_place(iterable, begin=begin, end=end)
    return iterable


def merge_in_place(iterable, begin=None, end=None):
    """Merges sorted sub-lists into one sorted list In-place.

    Preconditions:
        [
        begin <= end
        m = (end-begin)//2
        ~ iterable[:m+1] is sorted
        ~ iterable[m+1:] is sorted
        ]

    :param iterable: (iterable)
    :param begin:
    :param end:
    :return:
    """
    if begin is None:
        begin = 0
    if end is None:
        end = len(iterable) - 1
    if begin < end:
        middle = begin + (end - begin) // 2
        b = []
        i = begin
        j = middle + 1
        while i <= middle and j <= end:
            if iterable[i] <= iterable[j]:
                b.append(iterable[i])
                i += 1
            else:
                b.append(iterable[j])
                j += 1
        while i <= middle:
            b.append(iterable[i])
            i += 1
        while j <= end:
            b.append(iterable[j])
            j += 1
        iterable[begin:end+1] = b
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