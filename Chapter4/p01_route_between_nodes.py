import unittest

from Chapter3.Chapter3_qp4 import Queue


# VISUAL OF TEST GRAPH:

# A -- B
# |    |
# C -- D
# |
# E -- F -- G -- H
#      | \
#      O   I -- J -- K
#               |
#               L

# P -- Q
# |  /
# R


def is_route(graph, start, end):
    # sets
    # lets connect all possible path from A to anywhere
    # and see if the connection lasts
    # dfs
    start_set = set()
    start_set.add(start)

    def dfs(node):
        for edge in graph[node]:
            if edge not in start_set:
                start_set.add(edge)
                dfs(edge)
        return

    for edge in graph[start]:
        if edge not in start_set:
            start_set.add(edge)
            dfs(edge)

    return end in start_set


def is_route_bfs(graph, start, end):
    queue = []
    start_set = set()

    queue.append(start)

    while queue:
        curr_node = queue.pop(0)

        for edge in graph[curr_node]:
            if edge not in start_set:
                start_set.add(edge)
                queue.append(edge)

    return end in start_set



class Test(unittest.TestCase):

    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["B", "C"],
        "E": ["C", "F"],
        "F": ["E", "O", "I", "G"],
        "G": ["F", "H"],
        "H": ["G"],
        "I": ["F", "J"],
        "O": ["F"],
        "J": ["K", "L", "I"],
        "K": ["J"],
        "L": ["J"],
        "P": ["Q", "R"],
        "Q": ["P", "R"],
        "R": ["P", "Q"],
    }

    tests = [
        ("A", "L", True),
        ("A", "B", True),
        ("H", "K", True),
        ("L", "D", True),
        ("P", "Q", True),
        ("Q", "P", True),
        ("Q", "G", False),
        ("R", "A"
              ""
              ""
              ""
              "", False),
        ("P", "B", False),
    ]

    def test_is_route(self):
        for [start, end, expected] in self.tests:
            actual = is_route(self.graph, start, end)
            assert actual == expected

    def test_is_route_bfs(self):
        for [start, end, expected] in self.tests:
            actual = is_route_bfs(self.graph, start, end)
            assert actual == expected
    #
    # def test_is_route_bidirectional(self):
    #     for [start, end, expected] in self.tests:
    #         actual = is_route_bidirectional(self.graph, start, end)
    #         assert actual == expected


if __name__ == "__main__":
    unittest.main()