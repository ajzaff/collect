# -*- coding: utf-8 -*-


def bubble_sort(iterable, begin=None, end=None):
    """Sort the iterable In-place.

    :param iterable: (iterable) an iterable to sort
    :param begin:
    :param end:
    :return (iterable): the original object
    """
    if begin is None:
        begin = 0
    if end is None:
        end = len(iterable)
    while True:
        do_loop = False
        i = begin
        while i < end-1:
            if iterable[i] > iterable[i+1]:
                swap(iterable, i, i+1)
                do_loop = True
            i += 1
        if not do_loop:
            break

    return iterable


def swap(iterable, i, j):
    """Swap In-place.

    :param iterable: (iterable) an iterable
    :param i: (int) the first index
    :param j: (int) the second index
    :return (iterable): the original object
    :throws IndexError: i, j index out of range
    """
    iterable[i], iterable[j] = iterable[j], iterable[i]
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
        end = len(iterable)
    if begin+1 < end:
        middle = begin + (end - begin) // 2
        merge_sort(iterable, begin=begin, end=middle)
        merge_sort(iterable, begin=middle, end=end)
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
        end = len(iterable)
    if begin+1 < end:
        middle = begin + (end - begin) // 2
        b = []
        i = begin
        j = middle
        while i < middle and j < end:
            if iterable[i] <= iterable[j]:
                b.append(iterable[i])
                i += 1
            else:
                b.append(iterable[j])
                j += 1
        while i < middle:
            b.append(iterable[i])
            i += 1
        while j < end:
            b.append(iterable[j])
            j += 1
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
    if begin+1 < end:
        for i, e in enumerate(iterable[:end-1]):
            j = i + 1
            while j > begin and iterable[j-1] > iterable[j]:
                swap(iterable, j, j-1)
                j -= 1
    return iterable


def quick_sort(iterable, begin=None, end=None):
    """

    5   4   {3}  [2]  1
    5*  4   {3}   1* [2]
    1   4*  {3}   5  [2]*
    1  [2]  {3}*  5   4

    :param iterable:
    :param begin:
    :param end:
    :return:
    """
    """
    if begin is None:
        begin = 0
    if end is None:
        end = len(iterable)
    p = begin + (end - begin) // 2
    pivot = iterable[p]
    i = begin
    while i < end:
        if i != p:
            if iterable[i] <
        i += 1
    """

#def partition(iterable, begin=None, end=None):


#def three_partition(iterable, begin=None, end=None):
#    pass


#if __name__ == '__main__':
#    print merge_sort([5, 4, 3, 2, 1])

def last_pivot(iterable):
    """

    :param iterable:
    :return:
    """
    n = len(iterable)
    if n == 0:
        return None
    else:
        return n-1


def three_median_pivot(iterable, i=None, j=None, k=None):
    """

    :param iterable:
    :param i:
    :param j:
    :param k:
    :return:
    """
    n = len(iterable)
    if n == 0:
        return None
    if n == 1:
        return 0
    if i is None:
        i = 0
    if j is None:
        j = n // 2
    if k is None:
        k = n-1
    a = {0: (iterable[i], i),
         1: (iterable[j], j),
         2: (iterable[k], k)}
    if a[0][0] > a[1][0]: swap(iterable, 0, 1)
    if a[1][0] > a[2][0]: swap(iterable, 1, 2)
    if a[0][0] > a[1][0]: swap(iterable, 0, 1)
    return a[1][1]


def ninther_pivot(iterable):
    n = len(iterable)
    if n < 9:
        return three_median_pivot(iterable)
