# -*- coding: utf-8 -*-
import random

if __name__ == '__main__':
    f = open('_sorting/big_list.json', 'w')
    list = range(1, 1001)
    random.shuffle(list)
    s = str(list)
    f.write(s)
    f.close()
