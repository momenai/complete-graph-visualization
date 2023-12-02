import networkx as nx
import matplotlib.pyplot as plt

class StarGraphVisualization:
    def __init__(self, n):
        self.n = n
        self.G = nx.star_graph(n - 1)
        self.pos = nx.spring_layout(self.G)
        self.central_node = 0
        self.node_colors = ['orange' if node == self.central_node else 'skyblue' for node in self.G.nodes]

    def visualize_graph(self):
        nx.draw(self.G, self.pos, with_labels=True, node_color=self.node_colors,
                node_size=700, font_size=10, font_color='black', font_weight='bold')
        plt.title(f'Star Graph with {self.n} nodes')
        plt.show()

    def save_graph_image(self, filename='star_graph.png'):
        nx.draw(self.G, self.pos, with_labels=True, node_color=self.node_colors,
                node_size=700, font_size=10, font_color='black', font_weight='bold')
        plt.title(f'Star Graph with {self.n} nodes')
        plt.savefig(filename)
        print(f'Graph image saved as {filename}')

star_graph_instance = StarGraphVisualization(49)
# Visualize the graph
star_graph_instance.visualize_graph()
# Save the graph image
star_graph_instance.save_graph_image('star_graph.gif')
