import heapq
from dataclasses import dataclass

Node = str


@dataclass
class Connection:
    node1: Node
    node2: Node
    length: float

    def __str__(self) -> str:
        return f"({self.node1} -> {self.node2})"


def get_shortest_path(
    graph: list[Connection],
    start: Node,
    end: Node,
) -> tuple[float, list[Connection]]:
    # take latest node from priority queue, for each neighbour, add it to priority queue with priority equal to priority of the node + length of the connection
    # pop node from priority queue

    @dataclass
    class NodeData:
        distance: float
        path: list[Connection]

    connections: dict[Node, list[Connection]] = {}

    for conn in graph:
        if conn.node1 not in connections:
            connections[conn.node1] = []
        if conn.node2 not in connections:
            connections[conn.node2] = []

        connections[conn.node1].append(conn)
        connections[conn.node2].append(conn)

    queue = []
    info: dict[Node, NodeData] = {}

    heapq.heappush(queue, (0, start))
    info[start] = NodeData(0, [])

    while True:
        if len(queue) == 0:
            return -1, []

        _, node = heapq.heappop(queue)
        node_info = info[node]

        if node == end:
            return node_info.distance, node_info.path

        for conn in connections[node]:
            other = conn.node1 if conn.node2 == node else conn.node2
            other_distance = node_info.distance + conn.length
            other_path = node_info.path + [conn]

            if other not in info:
                info[other] = NodeData(other_distance, other_path)
            elif other_distance >= info[other].distance:
                continue

            heapq.heappush(queue, (other_distance, other))
            info[other].distance = other_distance
            info[other].path = other_path


if __name__ == "__main__":
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

    distance, path = get_shortest_path(graph, A, E)
    print(f"Distance: {distance}")
    print("Path: {}".format(" ".join([str(conn) + " " for conn in path])))
