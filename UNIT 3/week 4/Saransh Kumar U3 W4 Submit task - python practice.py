import matplotlib
import random
import math
import matplotlib.pyplot as plt
import networkx as nx

class Edge:
    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight

class Node:
    def __init__(self, name):
        self.name = name
        self.neighours = []
    
    def add_neigbour(self, neighour):
        if neighour not in self.neighours:
            self.neighours.append(self.neighour)

nodes = ["Home", "Park", "Shops", "School", "Station"]
class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
    
    def add_node(self, node_name):
        new_node = Node(node_name)
        self.nodes.append(new_node)
    
    def add_edge(self, src, dst, weight):
        new_edge = Edge(self, src, dst, weight)
        self.edges.append(new_edge)
    
        for node in self.nodes:
            if node.name == src:
                node.add_neighbour(dst)
            if node.name == dst:
                node.add_neighbour(src)
    
    def print_properties(self):
        for node in self.nodes:
            print (f"{node.name} goes to {node.neighbours}")
        for edge in self.edges:
            print (f"The taken to travel between {edge.src} and {edge.dst} is {edge.weight} minutes.")
    
    def display(self):
        G = nx.Graph()

        for node in my_graph.nodes:
            G.add_node(node.name)

        for edge in my_graph.edges:
            G.add_edge(edge.src, edge.dst, weight=edge.weight)
  

        edge_weights = {edge: G[edge[0]][edge[1]]['weight'] for edge in G.edges()}

        pos = nx.spring_layout(G, seed=42)  
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black', font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')


        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='gray', width=2.0)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights, font_size=10)

        plt.title("Network with 5 locations of a small suburb with time taken between them in minutes")
        plt.axis('off')
        plt.show()
        
my_graph = Graph()
my_graph.print_properties()