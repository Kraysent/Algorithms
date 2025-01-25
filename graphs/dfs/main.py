Node = str


def has_connection(graph: dict[Node, list[Node]], node1: Node, node2: Node) -> bool:
    """
    For a given directional `graph`, determines whether `node1` and `node2` are connected.
    """

    path = dfs(graph, node1, node2)
    return len(path) != 0


def dfs(graph: dict[Node, list[Node]], node: Node, target: Node) -> list[Node]:
    if node == target:
        return [node]

    if node not in graph:
        return []

    children = graph[node]

    for child in children:
        path = dfs(graph, child, target)

        if len(path) != 0:
            return [child] + path

    return []


if __name__ == "__main__":
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

    print(has_connection(graph, A, E))
