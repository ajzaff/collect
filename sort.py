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
    if i is None:
        i = 0
    if k is None:
        k = len(iterable)
    n = k - i
    if j is None:
        j = i + n // 2
    if n == 0:
        return None
    if n == 1:
        return 0
    a = [i, j, k-1]
    if iterable[a[0]] > iterable[a[1]]:
        swap(a, 0, 1)
    if iterable[a[1]] > iterable[a[2]]:
        swap(a, 1, 2)
    if iterable[a[0]] > iterable[a[1]]:
        swap(a, 0, 1)
    return a[1]


def ninther_pivot(iterable, begin=None, end=None):
    """

    :param iterable:
    :param begin:
    :param end:
    :return:
    """
    if begin is None:
        begin = 0
    if end is None:
        end = len(iterable)
    n = end - begin
    if n < 9:
        return three_median_pivot(iterable, i=begin, j=None, k=end)
    k1, k2 = begin + n//3, begin + 2*n//3
    a = [three_median_pivot(iterable, i=begin, j=None, k=k1),
         three_median_pivot(iterable, i=k1, j=None, k=k2),
         three_median_pivot(iterable, i=k2)]
    m = three_median_pivot(map(iterable.__getitem__, a))
    return a[m]


def partition(iterable, begin=None, end=None):
    """

    :param iterable:
    :param begin:
    :param end:
    :return:
    """
    if begin is None:
        begin = 0
    if end is None:
        end = len(iterable)
    p = ninther_pivot(iterable, begin=begin, end=end)
    pivot = iterable[p]
    i = begin
    while i < end:
        e = iterable[i]
        if i < p and e > pivot:
            swap(iterable, p, i)
            p = i
        elif i > p and e <= pivot:
            if i-p == 1:
                swap(iterable, i, p)
                p = i
            else:
                swap(iterable, i, p+1)
                swap(iterable, p, p+1)
                p += 1
        i += 1
    return p


def quick_sort(iterable, begin=None, end=None):
    """

    :param iterable:
    :param begin:
    :param end:
    :return:
    """
    if begin is None:
        begin = 0
    if end is None:
        end = len(iterable)
    n = end - begin
    if n > 1:
        p = partition(iterable, begin=begin, end=end)
        quick_sort(iterable, begin=begin, end=p)
        quick_sort(iterable, begin=p, end=end)
    return iterable


if __name__ == '__main__':
    import random, math
    # n = 10
    # j = int(n * (2 + math.log10(n)))
    # for i in range(500):
    #     l1 = range(n)
    #     random.shuffle(l1)
    #     par = partition(l1)
    #     left = l1[:par]
    #     right = l1[par+1:]
    #     print l1, '=>', str(left).ljust(j), '(%s)' % l1[par], str(right)

    n = 20
    for i in range(500):
        l1 = [random.randrange(n) for _ in range(n)]
        random.shuffle(l1)
        l1_copy = l1[:]
        res = quick_sort(l1)
        print l1_copy, '=>', res

    # l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 29, 22, 26, 25, 28, 24, 27, 30, 23]
    # begin = 10
    # end = 31
    # p = partition(l1, begin=begin, end=end)
    # print p