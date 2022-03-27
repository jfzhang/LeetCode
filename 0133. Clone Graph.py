"""
Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.
"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: 'Node') -> 'Node':
    visited = {}

    def dfs(node) -> 'Node':
        if not node:
            return node

        if node in visited:
            return visited[node]

        new_node = Node(node.val, [])
        visited[node] = new_node

        if node.neighbors:
            new_node.neighbors = [dfs(x) for x in node.neighbors]

        return new_node

    return dfs(node)
