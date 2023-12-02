import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class CompleteGraphAnimation:
    def __init__(self, initial_nodes=3, frames=23, interval=100, fps=5, filename='graph.gif'):
        self.graph = self.create_complete_graph(initial_nodes)
        self.pos = nx.circular_layout(self.graph)
        self.frames = frames
        self.interval = interval
        self.fps = fps
        self.filename = filename

        self.fig, self.ax = plt.subplots()
        self.ani = FuncAnimation(self.fig, self.update, frames=self.frames, interval=self.interval, repeat=False)

    def create_complete_graph(self, n):
        G = nx.complete_graph(n)
        return G

    def visualize_graph(self):
        self.ax.clear()
        nx.draw(self.graph, self.pos, with_labels=True, node_color='skyblue', node_size=700,
                font_size=10, font_color='black', ax=self.ax)

    def update(self, frame):
        i = frame + 3  # Start from node 3
        self.graph.add_node(i)
        self.graph.add_edges_from([(i, j) for j in range(i)])
        self.pos = nx.circular_layout(self.graph)
        self.visualize_graph()

    def save_animation(self):
        self.ani.save(self.filename, writer='pillow', fps=self.fps)
        print(f'Animation saved as {self.filename}')

    def show_animation(self):
        plt.show()

complete_graph = CompleteGraphAnimation()
complete_graph.show_animation()


#Save as gif
complete_graph = CompleteGraphAnimation( filename= "complete_graph.gif")
complete_graph.save_animation()
