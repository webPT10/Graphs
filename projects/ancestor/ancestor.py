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
    g = Graph()  # build graph to traverse

    for i in ancestors: # populate w verts
        g.add_vertex(i[0])
        g.add_vertex(i[1])

        g.add_edge(i[1], i[0]) # build edges

    q = Queue() # init a Q and add starting vertex as a list
    q.enqueue([starting_node])
    
    max_path = 1 # set max path and earliest ancestor -1 for return if no neighbors
    earliest = -1

    while q.size() > 0: # while the Q has elements
        path = q.dequeue() # we pull the first element into our path

        v = path[-1] # set v to the last index of path

        if(len(path) >= max_path and v < earliest) or (len(path) > max_path):
            earliest = v
            max_path = len(path)
        
        for next_item in g.verts[v]:
            copy = list(path)
            copy.append(next_item)
            q.enqueue(copy)
    
    return earliest
