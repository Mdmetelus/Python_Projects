class Graph:
    def __init__(self):
        self.vertices ={}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else
            raise indexError("That vertex does not exist:")
            # could also print the response
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else
            raise indexError("That vertex does not exist:")

def debthFirstSearch(adjList, node_id):
    print(node_id)
    for child_node in adjList[node_id]:
        debthFirstSearch(adjList, child_node) # recursive call

def debthFirstSearchVisted(adjList, node_id, visited):
  # time complexity is O(n**2) = quadratic 
  # because fir each ieration (n), you will check the visited (n) = N^2
  # space complexity is
    print(node_id)
    visited.append(node_id)
    for child_node in adjList[node_id]:
        if child_node not in visited:
        debthFirstSearchVisted(adjList, child_node, visited)  # recursive call

def dft(adjList, node_id):
  # time complexity is O(n) = linear
  # space complexity is
  nodes[node_id].color = "black"
    # print(node_id)
    # visited.append(node_id)
    for child_node in adjList[node_id]:
        if nodes[node_id].color = "white":
        debthFirstSearchVisted(adjList, child_node, visited)  # recursive call

def breathFirstSearch(adjList, node_id):
    print(node_id)
    frontier = []
    frontier.append(node_id)
    while len(frontier) > 0:
        n = frontier.pop
        print(n)
        for next_node in adjList[n]:
            frontier.append(next_node)

def breathFirstSearchVisited(adjList, node_id):
  # this traversal will be O(n) = linear implimentation
    print(node_id)
    frontier = []
    frontier.append(node_id)
    visited = [] # this will helps with graph as well as 
    while len(frontier) > 0:
        n = frontier.pop
        if n not in visited
          print(n)
          visited.append(n)
          for next_node in adjList[n]:
              frontier.append(next_node)