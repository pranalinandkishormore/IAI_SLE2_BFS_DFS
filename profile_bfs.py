import time
import matplotlib.pyplot as plt
from bfs import bfs


# Same graph used for BFS and DFS
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


cases = {
    "Best Case": "B",
    "Average Case": "G",
    "Worst Case": "O"
}


# Number of repetitions gives more stable timing
REPEATS = 10000

results = []

print("\nBFS PROFILING RESULTS")
print("-" * 60)

for case_name, goal in cases.items():

    total_time = 0
    total_nodes = 0

    for _ in range(REPEATS):

        start_time = time.perf_counter()

        path, nodes = bfs(graph, "A", goal)

        end_time = time.perf_counter()

        total_time += end_time - start_time
        total_nodes += nodes

    average_time_ms = (total_time / REPEATS) * 1000
    average_nodes = total_nodes / REPEATS

    results.append((case_name, average_time_ms, average_nodes))

    print(
        f"{case_name:15} "
        f"Time: {average_time_ms:.6f} ms   "
        f"Nodes: {average_nodes:.2f}"
    )


# -----------------------------
# Create BFS profiling graph
# -----------------------------

case_names = [result[0] for result in results]
times = [result[1] for result in results]

plt.figure(figsize=(8, 5))

bars = plt.bar(case_names, times)

plt.title("BFS Performance Profiling")
plt.xlabel("Test Case")
plt.ylabel("Average Execution Time (ms)")
plt.grid(axis="y", linestyle="--", alpha=0.4)

for bar, value in zip(bars, times):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{value:.6f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

plt.savefig("bfs_profile.svg", format="svg")

plt.show()
