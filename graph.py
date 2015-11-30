class GraphNode(set):
    """Representation of a graph as objects and pointers. """
    def __init__(self, label, value=None):
        set.__init__(self)
        self.label = label
        self.value = value

    def __hash__(self):
        return (self.label, self.value,
                tuple(map(lambda e: (e.label, e.value), self))).__hash__()

    def dfs(self, label=None, value=None, search_value=False):
        """

        :param label:
        :param value:
        :param search_value:
        :return:
        """
        visited = set()
        nodes = [self]
        res = None
        search_value |= value is not None
        while len(nodes) > 0:
            node = nodes.pop()
            if node in visited:
                print 'visiting [#%s]' % node.label
                continue
            print 'visiting #%s' % node.label
            visited.add(node)
            if node.label == label:
                res = node
                break
            if search_value and node.value == value:
                res = node
                break
            for n in nodes:
                if n not in visited:
                    nodes.append(n)
        return res

    def bfs(self, label=None, value=None, search_value=False):
        """

        :param label:
        :param value:
        :param search_value:
        :return:
        """
        visited = set()
        nodes = [self]
        res = None
        search_value |= value is not None
        while len(nodes) > 0:
            node = nodes.pop(0)
            if node in visited:
                print 'visiting [#%s]' % node.label
                continue
            print 'visiting #%s' % node.label
            visited.add(node)
            if node.label == label:
                res = node
                break
            if search_value and node.value == value:
                res = node
                break
            for n in node:
                if n not in visited:
                    nodes.append(n)
        return res


if __name__ == '__main__':
    nodes = [GraphNode(i, value=i) for i in range(13)]
    nodes[0].update([nodes[1], nodes[4]])
    nodes[1].update([nodes[0], nodes[5], nodes[2]])
    nodes[2].update([nodes[1], nodes[6], nodes[3]])
    nodes[3].update([nodes[2], nodes[7]])
    nodes[4].update([nodes[0], nodes[8]])
    nodes[5].update([nodes[1], nodes[6], nodes[10]])
    nodes[6].update([nodes[2], nodes[5], nodes[11]])
    nodes[7].update([nodes[3], nodes[12]])
    nodes[8].update([nodes[4], nodes[9]])
    nodes[9].update([nodes[8], nodes[10]])
    nodes[10].update([nodes[9], nodes[5], nodes[11]])
    nodes[11].update([nodes[10], nodes[6], nodes[12]])
    nodes[12].update([nodes[11], nodes[7]])
    nodes[5].bfs()




