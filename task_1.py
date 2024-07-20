import networkx as nx
import matplotlib.pyplot as plt

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

# Аналіз основних характеристик
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print("Degree of each node:")
for node, degree in G.degree():
    print(f"{node}: {degree}")
