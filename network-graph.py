from pyvis.network import Network

net = Network(notebook=True)
net.add_node(1, label="Bebang")
net.add_node(2, label="Marites")
# net.show("nodes.html")

net.add_nodes(
    [3, 4, 5, 6, 7],
    label=["Andy", "Raiza", "Bobby", "JV", "JG"],
    color=["#3da831", "#9a31a8", "#3155a8", "#FFD166", "#26547C"],
)

net.add_edge(1, 5, value=2)
net.add_edges([(2, 5, 2), (3, 4, 1), (1, 6, 3), (2, 6, 4), (3, 5, 1), (7, 5, 3), (3, 1, 2)])
net.show("edges.html")
