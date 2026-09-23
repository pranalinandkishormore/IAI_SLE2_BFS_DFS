# SLE-2: Profiling Report – BFS vs DFS

## Course
02AML204 – Introduction to Artificial Intelligence

## Student Details

- Name: Pranali Nandkishor More
- PRN: 25UAM132
- Division: B

## Project Title

Empirical Performance Analysis of BFS and DFS

## 1. Introduction

This project is part of SLE-2 for the course Introduction to Artificial Intelligence.

The purpose of this project is to perform empirical performance analysis of two uninformed search algorithms:

1. Breadth First Search (BFS)
2. Depth First Search (DFS)

Both algorithms are tested on the same search problem so that their performance can be compared fairly.

## 2. Objective

The main objectives of this project are:

- To implement BFS and DFS.
- To measure the actual execution time of both algorithms.
- To count the number of nodes expanded.
- To compare the performance of BFS and DFS.
- To analyse the experimental results.
- To understand the practical performance of search algorithms.

## 3. Algorithms Used

### Breadth First Search (BFS)

BFS explores a graph level by level. It first visits the starting node and then explores its neighbouring nodes before moving to the next level.

### Depth First Search (DFS)

DFS explores a graph by going as deep as possible along one path before backtracking to explore other paths.

## 4. Problem Used

A small graph/search problem is used for the experiment.

The same graph and search conditions are provided to both BFS and DFS to ensure a fair comparison.

## 5. Profiling Method

The performance of the algorithms is measured using Python time measurement/profiling methods.

The following measurements are collected:

- Execution time
- Number of nodes expanded

Each algorithm is executed multiple times and the average execution time is calculated.

## 6. Project Files

| File | Description |
|---|---|
| bfs.py | Implementation of Breadth First Search |
| dfs.py | Implementation of Depth First Search |
| profile_bfs.py | Profiling of BFS |
| profile_dfs.py | Profiling of DFS |
| bfs_profile.svg | BFS profiling visualization |
| dfs_profile.svg | DFS profiling visualization |
| AI_Contribution_Log.md | AI contribution record |

## 7. Performance Comparison

The actual experimental results are recorded after running the profiling programs.

| Metric | BFS | DFS |
|---|---:|---:|
| Average Time (ms) | ______ | ______ |
| Nodes Expanded | ______ | ______ |

## 8. Analysis

The performance of BFS and DFS is compared using the measured execution time and number of nodes expanded.

The conclusion is based on the actual experimental results obtained from the profiling process.

## 9. AI Contribution

AI tools were used to understand BFS and DFS, understand profiling methods, improve the implementation, and prepare the documentation.

The student performed the actual program execution, profiling experiments, collection of results, and analysis.

## 10. Conclusion

This project helps in understanding the practical performance of BFS and DFS. By measuring execution time and nodes expanded, the theoretical concepts of search algorithms can be compared with actual experimental results.

## 11. Course Information

Course Code: 02AML204  
Course: Introduction to Artificial Intelligence  
Activity: SLE-2 – Profiling Report
