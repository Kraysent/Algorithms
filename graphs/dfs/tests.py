import unittest
from graphs.dfs.main import Node, has_connection


class ProgramTests(unittest.TestCase):
    def test_simple_graph(self):
        A = Node("A")
        B = Node("B")
        C = Node("C")
        D = Node("D")
        E = Node("E")

        graph = {
            A: [B, C],
            B: [C],
            D: [E],
        }

        self.assertEqual(has_connection(graph, A, B), True)
        self.assertEqual(has_connection(graph, A, E), False)

    def test_graph_with_cycles(self):
        A = Node("A")
        B = Node("B")
        C = Node("C")
        D = Node("D")

        graph = {
            A: [B, C],
            B: [C],
            C: [D],
            D: [A],
        }
        self.assertEqual(has_connection(graph, A, D), True)
