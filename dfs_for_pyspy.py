from bfs import bfs

graph = {
    'A': ['B', 'I'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['G'],
    'F': ['H'],
    'G': ['K'],
    'H': ['K'],
    'I': ['J'],
    'J': ['K'],
    'K': []
}

for _ in range(100000):
    bfs(graph, 'A', 'B')
    bfs(graph, 'A', 'I')
    bfs(graph, 'A', 'K')
