import hashlib


class HashTable(object):

    TABLE_SIZE = 5000
    HASH_FUNCTION = hashlib.sha224

    def __init__(self):
        """

        :return:
        """
        self._cap = type(self).TABLE_SIZE
        self._repr = []
        i = 0
        while i < self._cap:
            self._repr.append(None)
            i += 1
        self._len = 0

    def __contains__(self, e):
        return self.contains(e)

    def __len__(self):
        return self._len

    def __delitem__(self, item):
        self.remove(item)

    def _get_hash(self, e):
        return long(type(self).HASH_FUNCTION(e.__str__()).hexdigest(), base=16)

    def _get_bucket(self, e):
        hsh = self._get_hash(e)
        buck = hsh % self._cap
        if self._repr[buck] is None:
            self._repr[buck] = []
        return self._repr[buck]

    def add(self, e):
        b = self._get_bucket(e)
        if not (e in b):
            self._get_bucket(e).append(e)
            self._len += 1

    def remove(self, e):
        try:
            self._get_bucket(e).remove(e)
            return e
        except ValueError:
            pass

    def contains(self, e):
        return len(self._get_bucket(e)) > 0

if __name__ == '__main__':
    ht = HashTable()

    items = {}

    def verbose_add(e):
        hash = ht._get_hash(e)
        bucket = hash % ht._cap
        if bucket in items:
            print 'collision for %s & %s [bucket=%s]' % (e, items[bucket], bucket)
            import sys
            sys.exit(0)
        else:
            print 'adding %s             [bucket=%s]' % (e, hash % ht._cap)
            ht.add(e)
            items[bucket] = e

    i = 0
    while True:
        verbose_add(i)
        i += 1