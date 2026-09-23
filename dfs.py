def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = {start}
    nodes_expanded = 0

    while stack:
        current, path = stack.pop()
        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        # Reverse order keeps the search order similar
        # to the written graph order.
        for neighbor in reversed(graph.get(current, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))

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

    path, nodes = dfs(graph, start, goal)

    print("DFS Search")
    print("Start Node:", start)
    print("Goal Node:", goal)
    print("Path:", path)
    print("Nodes Expanded:", nodes)
