import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Створення графа
G = nx.Graph()

# Додавання вузлів (вершин)
G.add_node("A", pos=(0, 0))
G.add_node("B", pos=(1, 2))
G.add_node("C", pos=(2, 1))
G.add_node("D", pos=(3, 0))
G.add_node("E", pos=(3, 3))

# Додавання ребер (доріг)
G.add_edge("A", "B", weight=2)
G.add_edge("A", "C", weight=4)
G.add_edge("B", "C", weight=1)
G.add_edge("B", "D", weight=7)
G.add_edge("C", "D", weight=3)
G.add_edge("C", "E", weight=5)
G.add_edge("D", "E", weight=2)

# Отримання позицій вузлів для візуалізації
pos = nx.get_node_attributes(G, 'pos')

# Візуалізація графа
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, font_color="black",
        edge_color="gray")

# Додавання ваг ребер
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Transport Network")
plt.show()


# Алгоритм DFS
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


# Алгоритм BFS
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


# Пошук шляхів від A до E
dfs_path = list(dfs_paths(G, "A", "E"))
bfs_path = list(bfs_paths(G, "A", "E"))

print("DFS Path:", dfs_path)
print("BFS Path:", bfs_path)


# Алгоритм Дейкстри для знаходження найкоротших шляхів між усіма вершинами графа
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]
    shortest_path_tree = {start: None}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, data in graph[current_node].items():
            weight = data['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path_tree[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, shortest_path_tree


# Відновлення шляху
def reconstruct_path(shortest_path_tree, start, goal):
    path = []
    current_node = goal
    while current_node is not None:
        path.append(current_node)
        current_node = shortest_path_tree[current_node]
    path.reverse()
    return path


# Знаходження найкоротших шляхів між усіма вершинами
shortest_paths = {}
shortest_path_lengths = {}
for node in G.nodes:
    distances, tree = dijkstra(G, node)
    shortest_paths[node] = {target: reconstruct_path(tree, node, target) for target in G.nodes}
    shortest_path_lengths[node] = distances

# Виведення найкоротших шляхів
print("\n")
for start_node, paths in shortest_paths.items():
    for end_node, path in paths.items():
        print(f"Shortest path from {start_node} to {end_node}: {path}")

# Виведення відстаней найкоротших шляхів між усіма вершинами
print("\n")
for start_node, lengths in shortest_path_lengths.items():
    for end_node, length in lengths.items():
        print(f"Shortest path length from {start_node} to {end_node}: {length}")

# Аналіз основних характеристик
print("\n")
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print("Degree of each node:")
for node, degree in G.degree():
    print(f"{node}: {degree}")
