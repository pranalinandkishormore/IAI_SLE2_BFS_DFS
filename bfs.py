from collections import deque


def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    nodes_expanded = 0

    while queue:
        current, path = queue.popleft()
        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None, nodes_expanded


if __name__ == "__main__":

    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": ["H", "I"],
        "E": ["J", "K"],
        "F": ["L", "M"],
        "G": ["N", "O"],
        "H": [],
        "I": [],
        "J": [],
        "K": [],
        "L": [],
        "M": [],
        "N": [],
        "O": []
    }

    start = "A"
    goal = "G"

    path, nodes = bfs(graph, start, goal)

    print("BFS Search")
    print("Start Node:", start)
    print("Goal Node:", goal)
    print("Path:", path)
    print("Nodes Expanded:", nodes)
