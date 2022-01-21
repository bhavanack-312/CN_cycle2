# distance vector routing using 

from collections import defaultdict
import math

class Graph:
  def __init__(self, vertices):
    self.vertices = vertices
    self.edges = defaultdict(list)
    self.nodes = set()

  def addnode(self, node):
    self.nodes.add(node)
  
  def addedge(self, from_node, to_node, distance):
    self.edges[(from_node, to_node)] = distance

def bellman_ford(graph, startnode):
  dist = {i: math.inf for i in graph.nodes}
  dist[startnode] = 0

  for i in range(graph.vertices):
    for key in graph.edges.keys():
      start, end = key
      distance = graph.edges[key]
      if dist[start] != math.inf and dist[start] + distance < dist[end]:
        dist[end] = dist[start] + distance
  
  return dist

def main():
  graph = Graph(5)
  graph.addnode('A')
  graph.addnode('B')
  graph.addnode('C')
  graph.addnode('D')
  graph.addnode('E')

  graph.addedge("A", "C", 6)
  graph.addedge("A", "D", 6)
  graph.addedge("B", "A", 3)
  graph.addedge("C", "D", 1)
  graph.addedge("D", "C", 2)
  graph.addedge("D", "B", 1)
  graph.addedge("E", "B", 4)
  graph.addedge("E", "D", 2)

  dist = bellman_ford(graph, 'E')
  for key in ['A', 'B', 'C', 'D', 'E']:
    print('{} -> {}'.format(key, dist[key]))

main()
