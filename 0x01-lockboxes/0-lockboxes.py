#!/usr/bin/python3
"""A module for Lockbox algorithm"""

from collections import deque


def canUnlockAll(boxes):
    """Solve Lockbox using Breadth-First Search"""
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = deque([0])

    while queue:
        current = queue.popleft()
        for key in boxes[current]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
