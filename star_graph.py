# # import networkx as nx
# # import matplotlib.pyplot as plt

# # class StarGraphVisualization:
# #     def __init__(self, n):
# #         self.n = n
# #         self.G = nx.star_graph(n - 1)
# #         self.pos = nx.spring_layout(self.G)
# #         self.central_node = 0
# #         self.node_colors = ['orange' if node == self.central_node else 'skyblue' for node in self.G.nodes]

# #     def visualize_graph(self):
# #         nx.draw(self.G, self.pos, with_labels=True, node_color=self.node_colors,
# #                 node_size=700, font_size=10, font_color='black', font_weight='bold')
# #         plt.title(f'Star Graph with {self.n} nodes')
# #         plt.show()

# #     def save_graph_image(self, filename='star_graph.png'):
# #         nx.draw(self.G, self.pos, with_labels=True, node_color=self.node_colors,
# #                 node_size=700, font_size=10, font_color='black', font_weight='bold')
# #         plt.title(f'Star Graph with {self.n} nodes')
# #         plt.savefig(filename)
# #         print(f'Graph image saved as {filename}')

# # star_graph_instance = StarGraphVisualization(49)
# # # Visualize the graph
# # star_graph_instance.visualize_graph()
# # # Save the graph image
# # star_graph_instance.save_graph_image('star_graph.png')


# import networkx as nx
# import matplotlib.pyplot as plt

# # Create an empty graph
# G = nx.Graph()

# # Add the center node
# G.add_node(0)

# # Draw the graph with the center node in red
# colors = ['r']
# nx.draw(G, node_color=colors, with_labels=True)

# # Display the graph
# plt.show()

# # Add new nodes with each iteration
# for i in range(1, 6):
#     G.add_node(i)
#     G.add_edge(0, i)

#     # Draw the updated graph with the new node in blue
#     colors.append('b')
#     nx.draw(G, node_color=colors, with_labels=True)

#     # Display the graph
#     plt.show()

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class StarGraphAnimation:
    def __init__(self, initial_nodes=1, frames=25, interval=100, fps=5, filename='star_graph.gif'):
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
