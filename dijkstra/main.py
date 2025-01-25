import heapq
from dataclasses import dataclass

Node = str


@dataclass
class Connection:
    node1: Node
    node2: Node
    length: float


def get_shortest_path(graph: list[Connection], start: Node, end: Node) -> float:
    # take latest node from priority queue, for each neighbour, add it to priority queue with priority equal to priority of the node + length of the connection
    # pop node from priority queue

    @dataclass
    class NodeData:
        distance: float

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
    info[start] = NodeData(0)

    while True:
        if len(queue) == 0:
            return -1

        _, node = heapq.heappop(queue)
        print(node)
        node_info = info[node]

        if node == end:
            return node_info.distance

        for conn in connections[node]:
            other = conn.node1 if conn.node2 == node else conn.node2
            other_distance = node_info.distance + conn.length

            if other not in info:
                info[other] = NodeData(other_distance)
            elif other_distance >= info[other].distance:
                continue

            heapq.heappush(queue, (other_distance, other))
            info[other].distance = other_distance
            print(f"Added {node} -> {other} ({other_distance})")


if __name__ == "__main__":
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

    print(get_shortest_path(graph, A, E))
