# Author: Hogan Lin
# Date: Jan 31st 2025
# Github: https://github.com/hogan-tech/SIT/tree/main/Computing
# Note: Upload to GitHub repo after deadline
# Description: Depth-First Search (DFS) and Breadth-First Search (BFS) implementation

from collections import deque

def dfs(graph: dict) -> None:
    """
    Performs Depth-First Search (DFS) on a directed graph using a stack.

    :param graph: Dictionary representing the graph {node: [neighbors]}
    """
    visited = set()
    nodes = sorted(graph.keys())
    
    for start in nodes:
        if start not in visited:
            stack = [start]
            while stack:
                node = stack.pop()
                if node not in visited:
                    print(node)
                    visited.add(node)
                    stack.extend(graph.get(node, []))


def bfs(graph: dict) -> None:
    """
    Performs Breadth-First Search (BFS) on a directed graph using a queue.

    :param graph: Dictionary representing the graph {node: [neighbors]}
    """
    visited = set()
    nodes = sorted(graph.keys())
    
    for start in nodes:
        if start not in visited:
            queue = deque([start])
            while queue:
                node = queue.popleft()
                if node not in visited:
                    print(node)
                    visited.add(node)
                    queue.extend(graph.get(node, []))

