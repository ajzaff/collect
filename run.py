def single_buy_single_sell_naive(iterable, begin=None, end=None):
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
    buy, sell, profit = 0, 0, 0
    if n > 1:
        i = begin
        while i < end - 1:
            j = i + 1
            while j < end:
                p = iterable[j] - iterable[i]
                if p > profit:
                    buy, sell, profit = i, j, p
                j += 1
            i += 1
    return buy, sell, profit


def single_buy_single_sell_divide(iterable, begin=None, end=None):
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
    transaction = begin, begin, 0
    if n > 1:
        middle = begin + (end - begin) // 2
        left = single_buy_single_sell_divide(iterable, begin=begin, end=middle)
        right = single_buy_single_sell_divide(iterable, begin=middle, end=end)

        mi, minimum = begin, iterable[begin]
        i = begin + 1
        while i < middle:
            e = iterable[i]
            if e < minimum:
                mi = i
                minimum = e
            i += 1

        ma, maximum = middle, iterable[middle]
        i = middle + 1
        while i < end:
            e = iterable[i]
            if e > maximum:
                ma = i
                maximum = e
            i += 1

        across = mi, ma, maximum - minimum
        transaction = sorted([left, right, across], key=lambda e: e[2])[2]
    return transaction


def single_buy_single_sell_optimal_divide(iterable, begin=None, end=None):
    """

    :param iterable:
    :param begin:
    :param end:
    :return:
    """
    def rec(_begin, _end):
        """

        :param _begin:
        :param _end:
        :return:
        """
        n = _end - _begin
        # ........... buy  | sell | min  | max  | profit
        b, s, mi, ma, p = _begin, _begin, _begin, _begin, 0
        if n > 1:
            middle = _begin + n // 2
            left = rec(_begin, middle)
            right = rec(middle, _end)
            new_min = left[2] if iterable[left[2]] <= iterable[right[2]] else right[2]
            new_max = left[3] if iterable[left[3]] > iterable[right[3]] else right[3]
            across = left[2], right[3], new_min, new_max, iterable[right[3]] - iterable[left[2]]
            best = sorted([left, right, across], key=lambda e: e[4])[2]
            b, s, mi, ma, p = best[0], best[1], new_min, new_max, best[4]
        return b, s, mi, ma, p

    if begin is None:
        begin = 0
    if end is None:
        end = len(iterable)
    buy, sell, minimum, maximum, profit = rec(begin, end)
    return buy, sell, profit


def single_buy_single_sell_table(iterable, begin=None, end=None):
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
    buy, sell, profit = begin, begin, 0
    if n > 1:
        m, minimum = begin, iterable[begin]
        i = begin + 1
        while i < end:
            e = iterable[i]
            if e < minimum:
                m, minimum = i, e
            p = e - minimum
            if p > profit:
                buy, sell, profit = m, i, p
            i += 1
    return buy, sell, profit


if __name__ == '__main__':
    l1 = [1, 5, 3, 2, 4, 8, 3, 0, 0, 5]
    print single_buy_single_sell_naive(l1)
    print single_buy_single_sell_divide(l1)
    print single_buy_single_sell_optimal_divide(l1)
    print single_buy_single_sell_table(l1)

