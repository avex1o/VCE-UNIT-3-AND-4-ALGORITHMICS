# Reasonably sure this works but the colouring is still messed up - should work in VS Code?

import networkx as nx
import matplotlib.pyplot as plt
import random

class Node:
    def __init__(self, id):
        self.id = id
        self.visited = False
        self.neighbours = []

    def __str__(self):
        return str(self.id)
        
    def add_neighbour(self, neighbour):
      if neighbour not in self.neighbours:
        self.neighbours.append(neighbour)
        self.sort_neighbours()
        
        
    def sort_neighbours(self):
      sorted = []
      while len(self.neighbours) > 0:
        smallest = self.neighbours[0]
        for node in self.neighbours:
          if node.id < smallest.id:
            smallest = node
        sorted.append(smallest)
        self.neighbours.remove(smallest)
      self.neighbours = sorted

class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
        self.id1 = source.id
        self.id2 = target.id
        self.color = 'black'

class RandomGraph:

  def __init__(self,V_N,E_N):
    # Creates a random graph objects with V_N vertices each with E_N edges
    self.edges = []
    self.nodes = [Node(i) for i in range(1,V_N+1)]
    
    for node in self.nodes:
    
      neighbours = random.sample(self.nodes,E_N)
      for neighbour in neighbours:
        if node != neighbour and self.get_weight(node.id, neighbour.id) == -1:
          rw = random.randint(1,7)
          edge = Edge(node, neighbour, rw)
          self.edges.append(edge)
          node.add_neighbour(neighbour)
          neighbour.add_neighbour(node)
    
    self.edges_old = self.edges.copy()
    self.nodes_old = self.nodes.copy()

  def get_weight(self, node1, node2):
    # Returns the edge weight between two nodes
    for edge in self.edges:
      if edge.id1 == node1 and edge.id2 == node2:
        return edge.weight
      if edge.id2 == node1 and edge.id1 == node2:
        return edge.weight
    return -1

  def set_colour(self, id1, id2, colour):
    # Sets the edge between id1 and id2 to the stated colour
    for edge in self.edges:
      if edge.id1 == id1 and edge.id2 == id2:
        edge.color = colour
      if edge.id1 == id2 and edge.id2 == id1:
        edge.color = colour  

  def display_graph(self):
    
    self.G1 = nx.Graph()
    self.G2 = nx.Graph()
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    
    for node in self.nodes:
      self.G2.add_node(node)
    for edge in self.edges:
      self.G2.add_edge(edge.source, edge.target, weight = edge.weight)
    pos2 = nx.circular_layout(self.G2)
    nx.draw(self.G2, pos2, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black', font_weight='bold')
      
    #edge_labels = nx.get_edge_attributes(self.G, 'weight')
    edge_labels = {}
    edge_colors = []
    for edge in self.edges:
      edge_colors.append(edge.color)
      
      edge_labels[(edge.source, edge.target)]= edge.weight
    nx.draw(self.G2, pos2, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black', font_weight='bold', edge_color=edge_colors, width=2.0, ax=ax2)
    nx.draw_networkx_edge_labels(self.G2, pos2, edge_labels=edge_labels)

    for node in self.nodes_old:
      self.G1.add_node(node)
    for edge in self.edges_old:
      self.G1.add_edge(edge.source, edge.target, weight = edge.weight)
    pos1 = nx.circular_layout(self.G1)
    nx.draw(self.G1, pos1, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black', font_weight='bold')
      
    #edge_labels = nx.get_edge_attributes(self.G, 'weight')
    edge_labels_old = {}
    edge_colors_old = []
    for edge in self.edges_old:
      edge_colors_old.append(edge.color)
      edge_labels_old[(edge.source, edge.target)]= edge.weight
    nx.draw(self.G1, pos1, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black', font_weight='bold', edge_color=edge_colors_old, width=2.0, ax=ax1)
    nx.draw_networkx_edge_labels(self.G1, pos1, edge_labels=edge_labels_old, ax=ax1)



    plt.axis('off')
    plt.show()

  def list_nodes_and_edges(self):
    for node in self.nodes:
      print(f"Node: {node.id}")
    for edge in self.edges:
      print(f"Edge from {edge.id1} to {edge.id2} with weight {edge.weight} and colour {edge.color}")


  def reset_visits(self):
    for node in self.nodes:
      node.visited = False

  def change_weight(self, id1, id2, weight):
  # Sets the edge between id1 and id2 to the stated colour
    for edge in self.edges:
      if edge.id1 == id1 and edge.id2 == id2:
        edge.weight = weight
      if edge.id1 == id2 and edge.id2 == id1:
        edge.weight = weight
        
  def FloydWarshall(self):
    
    for node in self.nodes:
      edge = Edge(node, node, 0)
      edge.color = 'green'
      self.edges.append(edge)
    
    
    for k in self.nodes:
      for i in self.nodes:
        for j in self.nodes:
          # Add edges whenever a path does not exist.
          if self.get_weight(i.id, j.id) == -1 and self.get_weight(i.id, k.id) != -1 and self.get_weight(k.id, j.id) != -1:
            edge = Edge(i,j,self.get_weight(i.id, k.id) + self.get_weight(j.id, k.id))
            edge.color = 'red'
            self.edges.append(edge)
          # Now look for shorter paths
          if self.get_weight(i.id, j.id) > self.get_weight(i.id, k.id)+self.get_weight(k.id, j.id) and self.get_weight(k.id, j.id) != -1 and self.get_weight(k.id, i.id) != -1 and self.get_weight(i.id, j.id) != -1:
            self.change_weight(i.id, j.id, self.get_weight(i.id, k.id)+self.get_weight(k.id, j.id))
            self.set_colour(i.id, j.id, 'red')
RG = RandomGraph(5,1)

RG.FloydWarshall()

RG.list_nodes_and_edges()

RG.display_graph()

