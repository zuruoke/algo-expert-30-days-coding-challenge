from itertools import count
from operator import ne
from platform import node
from typing import Any, List


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

# depth-first-traversal


def depth_first_traversal(graph: dict, source_node: str):
    stack = [source_node]
    depth_first_traversal_list = []

    while(len(stack) > 0):
        current = stack.pop()
        depth_first_traversal_list.append(current)
        for neighbor in graph[current]:
            stack.append(neighbor)

    return depth_first_traversal_list


def depth_first_traversal_with_recursion(graph: dict, source_node: str, depth_first_traversal_list: List[str]):
    depth_first_traversal_list.append(source_node)

    for neighbor in graph[source_node]:
        depth_first_traversal_with_recursion(
            graph, neighbor, depth_first_traversal_list)

    return depth_first_traversal_list

# breadth-first-traversal


def breadth_first_traversal(graph: dict, source_node: str):
    queue = [source_node]
    breadth_first_traversal_list = []

    while (len(queue) > 0):
        current = queue.pop(0)
        breadth_first_traversal_list.append(current)
        for neighbor in graph[current]:
            queue.append(neighbor)

    return breadth_first_traversal_list


print(depth_first_traversal(graph, "a"))
print(depth_first_traversal_with_recursion(graph, "a", []))
print(breadth_first_traversal(graph, "a"))


# Ayclic graphs & Cyclic graphs
# Directed Graphs are graphs that are graphs that explictly declares it's direction
# Adjacency list
# Problems

# 0(n^2 ) time complexity or 0(e) where e = no of edges
# 0(n) space complexity  where n = no of nodes

has_path_graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": []
}


def has_path_with_dfs(graph: dict, src, dest):
    if (src == dest):
        return True
    for neighbor in graph[src]:

        if (has_path_with_dfs(graph, neighbor, dest)):
            return True
    return False


print(has_path_with_dfs(has_path_graph, "f", "j"))


def has_path_with_bfs(graph: dict, src, dest):
    queue = [src]

    while (len(queue) > 0):
        current = queue.pop(0)
        if (current == dest):
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)

    return False


print(has_path_with_bfs(has_path_graph, "f", "k"))


# Undirected Graphs are like a two way street
# Undirected paths or graphs will mostly lead to a cyclic path or graph

undirected_graph = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"]
]


def build_graph(undirected_graph: List[List[str]]):
    graph = {}

    for nodes in undirected_graph:
        [nodeA, nodeB] = nodes
        if (nodeA not in graph):
            graph[nodeA] = []
        if (nodeB not in graph):
            graph[nodeB] = []
        graph[nodeB].append(nodeA)
        graph[nodeA].append(nodeB)

    return graph


def has_path_undirected_graph(graph, src, dst, memo):
    if src == dst:
        return True
    if src in memo:
        return False
    memo.add(src)

    for neigbor in graph[src]:
        if (has_path_undirected_graph(graph, neigbor, dst, memo)):
            return True
    return False


def undirected_graph_soln(undirected_graph, nodeA, nodeB, memo):
    graph = build_graph(undirected_graph)
    return has_path_undirected_graph(graph, nodeA, nodeB, memo)


print(undirected_graph_soln(undirected_graph, "j", "o", set()))

connected_components_graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}


def explore(graph, current_node, visited):
    if (current_node in visited):
        return False
    visited.add(current_node)
    for neighbor in graph[current_node]:
        explore(graph, neighbor, visited)

    return True


def connected_components_count(graph):
    visited = set()
    count = 0
    for node in graph:
        if (explore(graph, node, visited)):
            count += 1
    return count


print(connected_components_count(connected_components_graph))


def exploreSize(graph, current_node, visited):
    if current_node in visited:
        return 0
    visited.add(current_node)
    size = 1

    for neighbor in graph[current_node]:
        size += exploreSize(graph, neighbor, visited)

    return size


def largest_component(graph):
    visited = set()
    largest = 0
    for node in graph:
        size = exploreSize(graph, node, visited)
        largest = max(largest, size)
    return largest


print(largest_component(connected_components_graph))
