import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

edges = [
    (1, 2, 1), (1, 4, 1),
    (2, 3, 1), (2, 13, 1),
    (3, 5, 1),
    (4, 11, 0.5), (4, 24, 1),
    (5, 6, 1),
    (6, 7, 1),
    (7, 8, 1), (7, 3, 1),
    (8, 9, 1), (8, 15, 1),
    (9, 14, 1),
    (10, 4, 0.5), (10, 11, 1),
    (11, 1, 1),
    (12, 10, 1),
    (13, 18, 1),
    (14, 13, 1), (14, 17, 1),
    (15, 14, 1), (15, 16, 1),
    (16, 17, 1),
    (17, 13, 1), (17, 22, 1),
    (18, 8, 1), (18, 21, 1),
    (19, 18, 1), (19, 12, 1),
    (20, 19, 1),
    (21, 20, 0.5),
    (22, 21, 1), (22, 23, 1),
    (23, 16, 1),
    (24, 2, 0.5)
]

G.add_weighted_edges_from(edges)

def obtenir_pes(node_origen, node_desti):
    try:
        return G[node_origen][node_desti]['weight']
    except KeyError:
        return None

def cami_mes_curt(origen, desti):
    try:
        cami = nx.dijkstra_path(G, source=origen, target=desti, weight='weight')
        distancia = nx.dijkstra_path_length(G, source=origen, target=desti, weight='weight')
        return cami, distancia
    except nx.NetworkXNoPath:
        return None, float('inf')

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(12, 10))
nx.draw(G, pos, with_labels=True, node_size=800, node_color='skyblue', font_weight='bold', arrows=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Graf de nodes amb pesos", fontsize=16)
plt.axis('off')
plt.show()

# Exemple
pes = obtenir_pes(1, 2)
cami, dist = cami_mes_curt(1, 11)
print("Pes de 1 a 2:", pes)
print("Camí més curt de 1 a 11:", cami)
print("Distància total:", dist)
