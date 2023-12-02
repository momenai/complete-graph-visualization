import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class DAGAnimation:
    def __init__(self, initial_nodes=3, frames=10, interval=100, fps=5, filename='graph.gif'):
        self.graph = self.create_dag(initial_nodes)
        self.pos = nx.spring_layout(self.graph)
        self.frames = frames
        self.interval = interval
        self.fps = fps
        self.filename = filename

        self.fig, self.ax = plt.subplots()
        self.ani = FuncAnimation(self.fig, self.update, frames=self.frames, interval=self.interval, repeat=False)

    def create_dag(self, n):
        G = nx.DiGraph()
        for i in range(n):
            G.add_node(i)
        return G

    def visualize_graph(self):
        self.ax.clear()
        nx.draw(self.graph, self.pos, with_labels=True, node_color='skyblue', node_size=700,
                font_size=10, font_color='black', ax=self.ax, arrowsize=10, connectionstyle="arc3,rad=0.1")

    def update(self, frame):
        i = frame + 3  # Start from node 3
        self.graph.add_node(i)
        for existing_node in self.graph.nodes():
            self.graph.add_edge(i, existing_node)
        self.pos = nx.spring_layout(self.graph)
        self.visualize_graph()

    def save_animation(self):
        self.ani.save(self.filename, writer='pillow', fps=self.fps)
        print(f'Animation saved as {self.filename}')

    def show_animation(self):
        plt.show()

dag_graph = DAGAnimation(filename="dag_graph.gif")
dag_graph.show_animation()

dag_graph.save_animation()
