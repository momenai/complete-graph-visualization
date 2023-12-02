

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class StarGraphAnimation:
    def __init__(self, initial_nodes=1, frames=50, interval=100, fps=5, filename='star_graph.gif'):
        self.graph = self.create_star_graph(initial_nodes)
        self.pos = nx.spring_layout(self.graph)
        self.frames = frames
        self.interval = interval
        self.fps = fps
        self.filename = filename

        self.fig, self.ax = plt.subplots()
        self.ani = FuncAnimation(self.fig, self.update, frames=self.frames, interval=self.interval, repeat=False)

    def create_star_graph(self, n):
        G = nx.Graph()
        G.add_node(0)  # Center node
        return G

    def visualize_graph(self):
        self.ax.clear()
        nx.draw(self.graph, self.pos, node_color='skyblue', with_labels=True)

    def update(self, frame):
        i = frame + 1
        self.graph.add_node(i)
        self.graph.add_edge(0, i)
        self.pos = nx.spring_layout(self.graph)
        self.visualize_graph()

        # Change the color of the center node to orange
        nx.draw_networkx_nodes(self.graph, self.pos, nodelist=[0], node_color='orange', ax=self.ax)

    def save_animation(self):
        self.ani.save(self.filename, writer='pillow', fps=self.fps)
        print(f'Animation saved as {self.filename}')

    def show_animation(self):
        plt.show()

star_graph = StarGraphAnimation(filename="star_graph.gif")
star_graph.save_animation()
