# Implement a Union Find Data Structure in Python
# For integer values

class QuickUnionFind:

    def __init__(self, uf_size):
        self._id = list(range(uf_size))
        self._sz = [1 for val in range(uf_size)]

    def _root(self, i):
        while i != self._id[i]:
            self._id[i] = self._id[self._id[i]]
            i = self._id[i]
        return i

    def is_connected(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p, q):
        i = self._root(p)
        j = self._root(q)

        if i == j:
            return

        if self._sz[i] < self._sz[j]:
            self._id[i] = j
            self._sz[j] += self._sz[i]
        else:
            self._id[j] = i
            self._sz[i] += self._sz[j]


uf = QuickUnionFind(6)
print(uf.is_connected(0, 5))
uf.union(0, 5)
print(uf.is_connected(0, 5))
