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


def earliest_ancestor(ancestors, starting_node):
    pass