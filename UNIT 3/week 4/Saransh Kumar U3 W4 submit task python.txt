import matplotlib
import random
import math
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
  def __init__(self):
    self.nodes = []
    self.edges = []
  
  def add_node(self, node_name):
    new_node = Node(node_name)
    self.nodes.append(new_node)
    
  def add_edge(self, src, dst, weight):
    new_edge = Edge(src, dst, weight)
    self.edges.append(new_edge)
    
    for node in self.nodes:
      if node.name == src:
        node.add_neighbour(dst)
      if node.name == dst:
        node.add_neighbour(src)  

  def print_properties(self): 
    for node in self.nodes:
      print(f"{node.name} has roads to and from {node.neighbours}")
    for edge in self.edges:
      print(f"Travelling from {edge.src} to {edge.dst} takes {edge.weight} minutes")

  def display(self):
    G = nx.Graph() 

    for node in my_graph.nodes:
      G.add_node(node.name)

    for edge in self.edges:
      G.add_edge(edge.src, edge.dst, weight=edge.weight)
  
    edge_weights = {edge: G[edge[0]][edge[1]]['weight'] for edge in G.edges()}

    pos = nx.spring_layout(G, seed=42) 
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black', font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='gray', width=2.0)

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights, font_size=10)

    plt.title("Undirected graph of a small suburb and time taken between important places.")
    plt.axis('off')
    plt.show()


class Edge:
  def __init__(self, src, dst, weight):
    self.src = src
    self.dst = dst
    self.weight = weight
    
    
class Node:
  def __init__(self, name):
    self.name = name
    self.neighbours = []

  def add_neighbour(self, neighbour):
    if neighbour not in self.neighbours:
      self.neighbours.append(neighbour)


my_graph = Graph()

node_list = ["School","Home","Shops","Station","Park"]

for i in node_list:
  my_graph.add_node(i)
  
for i in node_list:
  for j in node_list:
    if i != j:
        chance = random.randint(1,3)
        if chance == 1:
            my_graph.add_edge(i,j,random.randint(3,10))
        
my_graph.print_properties()
my_graph.display()