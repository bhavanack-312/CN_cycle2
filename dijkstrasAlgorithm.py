# dijkstra algorithm

from collections import defaultdict

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}
  
  def addnode(self, node):
    self.nodes.add(node)
      
  def addedge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.distances[(from_node, to_node)] = distance
   
def dijkstras(graph, startnode):
  visited = {startnode: 0}
  path = defaultdict(list)
  nodes = list(graph.nodes)
    
  while len(nodes) != 0:
    minnode = None
    for node in nodes:
      if node in visited.keys():
        if minnode == None:
          minnode = node
        elif visited[node] < visited[minnode]:
          minnode = node
        # print(minnode)
    if minnode == None:
      break
    nodes.remove(minnode)
    current_weight = visited[minnode]

    for edge in graph.edges[minnode]:
      weight = current_weight + graph.distances[(minnode, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge].append(minnode)
  
  return visited, path

def main():
  graph = Graph()

  for i in range(7):
    graph.addnode(i+1)

  graph.addedge(1, 2, 2)
  graph.addedge(1, 3, 5)
  graph.addedge(2, 3, 6)
  graph.addedge(2, 4, 1)
  graph.addedge(2, 5, 3)
  graph.addedge(3, 6, 8)
  graph.addedge(4, 5, 4)
  graph.addedge(5, 7, 9)
  graph.addedge(6, 7, 7)

  print('node {} :'.format(1))
  visited, path = dijkstras(graph, 1)
  print('\ndistances: ')
  for key in visited.keys():
    print('node {} -> {}'.format(key, visited[key]))
  print('\npath: ')
  for key in path.keys():
    print('node {} -> {}'.format(key, path[key]))
    
main()
