import networkx as nx
import matplotlib.pyplot as plt
import csv
import random
import math
#from itertools import permutations
import itertools

class Node:
    def __init__(self, name, cap, xtime, lat, long):
        # Name, latitude, longitude, resource capacity, time to extract, default colour (1-5), empty list of neighbours
        self.name = name
        self.lat = lat
        self.long = long
        self.cap = cap
        self.xtime = xtime
        self.colour = 1
        self.neighbours = []

   
        
    def add_neighbour(self, neighbour):
      # Adds a neighbour (node object) after checking to see if it was there already
      if neighbour not in self.neighbours:
        self.neighbours.append(neighbour)
        
    
        
    

class Edge:
  def __init__(self, place1, place2, dist, time):
    # Two places (order unimportant), distance in km, time in mins, default colour (1-5)
    self.place1 = place1
    self.place2 = place2
    self.dist = dist
    self.time = time
    self.colour = 2

class Graph:
  def __init__(self):
    # List of edge objects and node objects
    self.edges = []
    self.nodes = []
    self.colour_dict = {0: "black", 1: "blue", 2: "red", 3: "green", 4: "yellow", 5:"lightblue"}

  def load_data(self):
    # Reads the CSV files you are provided with and creates node/edges accordingly.
    # You should not need to change this function.

    # Read the nodes, create node objects and add them to the node list.
    with open("nodes.csv", 'r', encoding='utf-8-sig') as csvfile:
      csv_reader = csv.reader(csvfile)
      for row in csv_reader:
        name = row[0]
        cap = int(row[1])
        xtime = int(row[2])
        lat = float(row[3])
        long = float(row[4])
        node = Node(name, cap, xtime, lat, long)
        self.nodes.append(node)
        
    # Read the edges, create edge objects and add them to the edge list.
    with open("edges.csv", "r", encoding='utf-8-sig') as csvfile:
      csv_reader = csv.reader(csvfile)
      for row in csv_reader:
        place1 = row[0]
        place2 = row[1]
        dist = int(row[2])
        time = int(row[3])
        edge = Edge(place1, place2, dist, time)
        self.edges.append(edge)
        
        for node in self.nodes:
          if node.name == place1:
            node.add_neighbour(place2)
          if node.name == place2:
            node.add_neighbour(place1)
    
  def get_time(self,place1,place2):
    # Returns the time between two place names (strings) if an edge exists,
    # otherwise returns -1.
    for edge in self.edges:
      if edge.place1 == place1 and edge.place2 == place2:
        return edge.time
      if edge.place1 == place2 and edge.place2 == place1:
        return edge.time
    return -1
  
  def get_x_time(self,place):
    for node in self.nodes:
      if node.name == place:
        return node.xtime
    return -1
  
  def get_cap(self,place):
    for node in self.nodes:
      if node.name == place:
        return node.cap
    return -1
  
  def get_dist(self,place1,place2):
    # Returns the distance between two place names (strings) if an edge exists,
    # otherwise returns -1.
  
    for edge in self.edges:
      if edge.place1 == place1 and edge.place2 == place2:
        return edge.dist
      if edge.place1 == place2 and edge.place2 == place1:
        return edge.dist
    return -1

  
  def display(self, filename = "map.png"):
    # Displays the object on screen and also saves it to a PNG named in the argument.
    
    edge_labels = {}
    edge_colours = []
    G = nx.Graph()
    node_colour_list = []
    for node in self.nodes:
      G.add_node(node.name, pos=(node.long, node.lat))
      node_colour_list.append(self.colour_dict[node.colour])
    for edge in self.edges:
      G.add_edge(edge.place1, edge.place2)
      edge_labels[(edge.place1, edge.place2)] = edge.dist
      edge_colours.append(self.colour_dict[edge.colour])
    node_positions = nx.get_node_attributes(G, 'pos')


    plt.figure(figsize=(10, 8))
    nx.draw(G, node_positions, with_labels=True, node_size=50, node_color=node_colour_list, font_size=8, font_color='black', font_weight='bold', edge_color=edge_colours)
    nx.draw_networkx_edge_labels(G, node_positions, edge_labels=edge_labels)
    plt.title('')
    plt.savefig(filename)
    plt.show()

  

  def haversine(self, lat1, lon1, lat2, lon2):
  # Returns the distance in km between two places with given latitudes and longitudes.
  
      # Radius of the Earth in kilometers
      R = 6371.0

      # Convert latitude and longitude from degrees to radians
      lat1_rad = math.radians(lat1)
      lon1_rad = math.radians(lon1)
      lat2_rad = math.radians(lat2)
      lon2_rad = math.radians(lon2)

      # Differences in coordinates
      dlat = lat2_rad - lat1_rad
      dlon = lon2_rad - lon1_rad

      # Haversine formula
      a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
      c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

      # Calculate the distance
      distance = R * c

      return distance

 #
 #
 #
 #
 #  SOLUTION
 #
 #
 #
 #
 


  def mineroute(self,target,radius,maxtime):
  
  # Look up lat and long of target
    for node in self.nodes:
      if node.name == target:
        tlat = node.lat
        tlong = node.long
    # First find all towns within the radius
    to_mine = []
    for node in self.nodes:
      if self.haversine(tlat, tlong, node.lat, node.long) <= radius:
        to_mine.append(node.name) 

    print(f"Mining towns: {to_mine}")
    
    # Create all possible paths between these nodes of lengths from 1 to V_n

    all_perms = itertools.chain.from_iterable(itertools.permutations(to_mine, r) for r in range(1, len(to_mine) + 1))
    paths = [list(pt) for pt in all_perms]

    # Create a FW matrix to represent times
    
    V_n = len(to_mine) # Number of places to mine

    matrix = [[9999 for i in range(V_n)] for j in range(V_n)]

    print(f"Matrix: {to_mine}")

    # Set leading diagonal to zero
    for i in range(V_n):
      matrix[i][i] = 0

    # Look up edges
    for i in range(V_n):
      for j in range(V_n):
        if i != j:
          ttime = self.get_time(to_mine[i],to_mine[j])
          if ttime != -1:
            matrix[i][j] = ttime
    
    # Print original matrix
    print("Original matrix:") 
    for row in matrix:
      print(row)

    # Run FW

    for k in range(V_n):
      for i in range(V_n):
        for j in range(V_n):
          if i != j and i != k and j != k and matrix[i][k] + matrix[k][j] < matrix[i][j]:
            matrix[i][j] = matrix[i][k] + matrix[k][j]

    # Print new matrix
    print("New matrix:")
    for row in matrix:
      print(row)

    # Create dictionary to look up matrix index
    matidx = {}
    for i in range(V_n):
      matidx[to_mine[i]] = i
    


    evaluate_paths = []
    # Will contain a list containing path number, travel time, mining time and capacity

    for i in range(len(paths)):
      ttime = 0
      mining_time = 0
      cap = 0
      for j in range(len(paths[i])-1):
        ttime += matrix[matidx[paths[i][j]]][matidx[paths[i][j+1]]]
      #print(f"Path {paths[i]} has a travel time of {ttime}")
      for j in range(len(paths[i])):
        mining_time += self.get_x_time(paths[i][j])
      #print(f"Path {paths[i]} has resource mining time of {mining_time}")
      for j in range(len(paths[i])):
        cap += self.get_cap(paths[i][j])
      #print(f"Path {paths[i]} has resource mining capacity of {cap}")
      evaluate_paths.append([i,ttime,mining_time,cap])
      print(f"Path {paths[i]} has capacity {cap}, total time {ttime + mining_time} (travel {ttime} + mining {mining_time})")

    # Now go through evaluate_paths and remove paths that are over time
    
    print(f"{len(evaluate_paths)} to check.")

    accept_paths = []

    for path in evaluate_paths:
      if path[1]+path[2] > maxtime:
        print(f"{paths[path[0]]} has time {path[1]+path[2]}, removing from list.")
      else:
        print(f"{paths[path[0]]} has time {path[1]+path[2]}, keeping.")
        accept_paths.append(path)

    print(f"{len(accept_paths)} left.")
    for path in accept_paths:
      print(paths[path[0]])

    # Now find the best one
    best_cap = 0
    for path in accept_paths:
      if path[3] > best_cap:
        best_path = path
        best_cap = path[3]
    print(f"Best path within the time is {paths[path[0]]} with capacity {best_cap} taking time {path[1]+path[2]}")
    print(f"Originally considered {len(paths)} paths, but {len(accept_paths)} were within the time limit of {maxtime}")



# Create a new graph object called 'original'
original = Graph()

# Load data into that object.
original.load_data()

original.display()

# Find the best route within 100km of Shepparton with a max time of 299.
original.mineroute("Shepparton", 100,299)