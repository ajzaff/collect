def greedy_change(coins, n):
    """

    [25, 10, 5, 1]

    Preconditions =>
        coins are non-increasing
        number of coins = O(1)

    :param coins: (list[int])
    :param n: (int)
    :return: (list[int])
    """
    res = {c: 0 for c in coins}
    res[0] = 0
    i = 0
    while i < len(coins):
        c = coins[i]
        t = n // c
        if t > 0:
            res[c] = t
            res[0] += t
            n -= t * c
        i += 1
    return res


def table_change(coins, n):
    """

    Preconditions =>
        coins are non-increasing
        number of coins = O(1)

    :param coins:
    :param n:
    :return:
    """
    def get_table(coins, n):
        """

        :param coins:
        :param n:
        :return:

        rows i are coin values
        cols j are amount (n) values

        """
        table = [[0 for _ in range(n+1)] for _ in range(len(coins)+1)]
        for i in range(n+1):
            table[0][i] = i
        return table

    table = get_table(coins, n)
    for t in table:
        print t
    # for c in range(len(coins)+1):
    #     for r in range(n+1):
    #

def  minEditDist(s1, s2):
    ''' Computes the min edit distance from target to source. Figure 3.25 '''

    m=len(s1)+1
    n=len(s2)+1

    tbl = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m): tbl[i][0]=i
    for j in range(n): tbl[0][j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i][j] = min(tbl[i][j-1]+1, tbl[i-1][j]+1, tbl[i-1][j-1]+cost)

            for t in tbl:
                print t
            print '---'

    return tbl[-1][-1]


if __name__ == '__main__':
    US_COINS = [25, 15, 10, 5, 1]
    MARTIAN_COINS = [1, 3, 4]
    # for i in range(30, 51):
    #     print i, greedy_change(US_COINS, i)
    print minEditDist(s1='oiled', s2='soiling')