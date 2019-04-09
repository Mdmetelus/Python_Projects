class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
           
   # Debth first traversal with recusion
    def dft_r(self, start_vert, visited = None):
        if visited is None:
            visited = set()
        visited.add(start_vert)
        print(start_vert)
        for child_vert in self.vertices(start_vert):
            if child_vert not in visited:
                self.dft_r(child_vert, visted) # recusive call

# breath first search with path returned at the end (no recursion possible)
    def bfs_path(self, starting_vertex_id, target_value):
      q = Queue()
      q.enqueue([starting_vertex_id])
      visited = set()
      while q.size() > 0:
          path = q.dequeue()
          v = path[-1]
          if v not in visited:
              if v == target_value:
                  return path
              visited.add(v)
              for next_vert in self. vertices[v]
                  new_path = list(path)
                  # or new_path = path.copy()
                  new_path.append(next_vert)
                  q.enqueue(new_path)
      return None

# 
    def dfs_r_path(self, start_vert, target_value, visited = None, path = none):
        if visited is None:
           visited = set()
        if path = None:
            path = []
        visited.add(start_vert) # being used as argument and not being assessed so non brackets needed around start_vert here.
        path = path + [start_vert]
        if start_vert == target_value:
            return path
        for child_vert in self.vertices[start_vert]:
            if child_vert not in visited:
                new_path = self.dfs_r_path(child_vert, target_value, visited, path)
                if new_path:
                    return new_path
        return None


        