import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class BipartiteGraphAnimation:
    def __init__(self, initial_nodes=3, frames=23, interval=100, fps=5, filename='bipartite_graph.gif'):
        self.graph = self.create_bipartite_graph(initial_nodes)
        self.pos = nx.spring_layout(self.graph)
        self.frames = frames
        self.interval = interval
        self.fps = fps
        self.filename = filename

        self.fig, self.ax = plt.subplots()
        self.ani = FuncAnimation(self.fig, self.update, frames=self.frames, interval=self.interval, repeat=False)

    def create_bipartite_graph(self, n):
        G = nx.Graph()
        for i in range(n):
            G.add_node(f'A{i}', bipartite=0)  # Nodes in set A
            G.add_node(f'B{i}', bipartite=1)  # Nodes in set B
        return G

    def visualize_graph(self):
        self.ax.clear()
        pos = nx.bipartite_layout(self.graph, align='horizontal')  # Align nodes in two rows
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=700,
                font_size=10, font_color='black', ax=self.ax)

        # List nodes on each side
        nodes_a = [node for node in self.graph.nodes if self.graph.nodes[node]['bipartite'] == 0]
        nodes_b = [node for node in self.graph.nodes if self.graph.nodes[node]['bipartite'] == 1]

        self.ax.text(0.5, 1.05, f'Set A: {nodes_a}', transform=self.ax.transAxes, horizontalalignment='center')
        self.ax.text(0.5, -0.05, f'Set B: {nodes_b}', transform=self.ax.transAxes, horizontalalignment='center')

    def update(self, frame):
        i = frame + 3  # Start from node 3
        node_a = f'A{i}'
        node_b = f'B{i}'
        self.graph.add_node(node_a, bipartite=0)
        self.graph.add_node(node_b, bipartite=1)

        # Add an edge between nodes in different sets
        if i > 3:
            j = i - 3
            existing_node_a = f'A{j}'
            existing_node_b = f'B{j}'
            self.graph.add_edge(node_a, existing_node_b)
            self.graph.add_edge(node_b, existing_node_a)

        self.visualize_graph()

    def save_animation(self):
        self.ani.save(self.filename, writer='pillow', fps=self.fps)
        print(f'Animation saved as {self.filename}')

    def show_animation(self):
        plt.show()

bipartite_graph = BipartiteGraphAnimation(filename="bipartite_graph.gif")
bipartite_graph.show_animation()
