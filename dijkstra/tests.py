import unittest

from dijkstra.main import Connection, Node, get_shortest_path


class ProgramTests(unittest.TestCase):
    def test_simple_graph(self):
        A = Node("A")
        B = Node("B")
        C = Node("C")
        D = Node("D")
        E = Node("E")

        graph = [
            Connection(A, B, 1),
            Connection(A, C, 2),
            Connection(B, D, 3),
            Connection(C, D, 4),
            Connection(C, E, 4),
            Connection(D, E, 3),
        ]

        self.assertEqual(get_shortest_path(graph, A, E), 6)

    def test_two_nodes(self):
        A = Node("A")
        B = Node("B")

        graph = [
            Connection(A, B, 1),
        ]

        self.assertEqual(get_shortest_path(graph, A, B), 1)

    def test_graph_with_equal_distances(self):
        A = Node("A")
        B = Node("B")
        C = Node("C")
        D = Node("D")
        E = Node("E")

        graph = [
            Connection(A, B, 1),
            Connection(A, C, 1),
            Connection(B, D, 1),
            Connection(C, D, 1),
            Connection(C, E, 40),
            Connection(D, E, 30),
        ]

        self.assertEqual(get_shortest_path(graph, A, E), 32)

    def test_disconnected_graph(self):
        A = Node("A")
        B = Node("B")
        C = Node("C")
        D = Node("D")
        E = Node("E")

        graph = [
            Connection(A, B, 1),
            Connection(C, D, 2),
            Connection(C, E, 4),
            Connection(D, E, 3),
        ]

        self.assertEqual(get_shortest_path(graph, A, E), -1)
