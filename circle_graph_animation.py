
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class CircularRingGraphAnimation:
    def __init__(self, initial_nodes=1, frames=25, interval=100, fps=5, filename='circular_ring_graph.gif'):
        self.graph = self.create_circular_ring_graph(initial_nodes)
        self.pos = nx.circular_layout(self.graph)
        self.frames = frames
        self.interval = interval
        self.fps = fps
        self.filename = filename

        self.fig, self.ax = plt.subplots()
        self.ani = FuncAnimation(self.fig, self.update, frames=self.frames, interval=self.interval, repeat=False)

    def create_circular_ring_graph(self, n):
        G = nx.Graph()
        for i in range(n):
            G.add_node(i)
            if i != 0:
                G.add_edge(i, (i + 1) % n)  # Connect each node to its adjacent nodes in a circular way
            # else:
            #     G.add_edge(i, (i + 1) % n)  # Connect each node to its adjacent nodes in a circular way

        return G

    def visualize_graph(self):
        self.ax.clear()
        nx.draw(self.graph, self.pos, node_color='skyblue', with_labels=True)

    def update(self, frame):
        i = frame + 1
        self.graph.add_node(i)
        self.graph.add_edge(i, (i - 1) % len(self.graph))  # Connect to the previous node
        self.pos = nx.circular_layout(self.graph)
        self.visualize_graph()

    def save_animation(self):
        self.graph.add_edge(0, len(self.graph) - 1)  # Connect the starting node to the last added node
        self.ani.save(self.filename, writer='pillow', fps=self.fps)
        print(f'Animation saved as {self.filename}')

    def show_animation(self):
        plt.show()

circular_ring_graph = CircularRingGraphAnimation(filename="circular_ring_graph.gif")
circular_ring_graph.save_animation()
