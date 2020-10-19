# looking for earliest ancestor so need a DFS
# need a Queue and Graph class

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

class Graph():
    def __init__(self):
        self.verts = {} # adj list (dictionary) of vertices mapping labels to edges

    def add_vertex(self, vertex_id):
        if vertex_id not in self.verts:
            self.verts[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.verts and v2 in self.verts:
            self.verts[v1].add(v2)


def earliest_ancestor(ancestors, starting_node):
    pass