class Graph:
    def __init__(self):
        self.verticies = {}
    def add_vertices(self, vertex_id):
        self.verticies[vertex_id] = set()
    def Add_edge(self, v1, v2):
        if v1 in self.verticies and v2 in self.verticies:
            self.verticies[v1].add(v2)
            self.verticies[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")
    def Add_directed_edge(self, v1, v2):
        if v1 in self.verticies and v2 in self.verticies:
            self.verticies[v1].add(v2)
        else:
            raise IndexError("That vertec does not exist")

# bfs = Queue
# implement the queue, and enque the starting Vertex Id
  def bfs(self, starting_vertex_id)
# create a queue
    q = Queue()
# create a set to store verticies
    visited = set()

# While the queue is not empty it will run.
    While q.size() > 0
    # Dequeue the first vertex
        v = q.dequeue
    # If thath vertex has not been visited:
        if
        # Mark it as visited
        print(v)
        visited.add(v)
        # Add all of its neighbors to the back of the queue
          