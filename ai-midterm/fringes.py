from problems import Node

class Stack:
    def __init__(self):
        self.frontier = []
        
    def push(self, node: Node):  # push 
        self.frontier.append(node)
        
    def pop(self):  # pop 
        if self.is_empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node     
    
    def is_empty(self):
        return len(self.frontier) == 0

        
    def contains(self, node: Node):
        flag = False
        for state in self.frontier:
            state = state.state
            if(node.state == state):
                flag = True
        return flag
    
    def print(self):
        for i in range(len(self.frontier)):
            print(self.frontier[i].state, " ", self.frontier[i].action)

# Queue inherits from Stack 
class Queue(Stack):
    def enqueue(self, node):
        self.frontier.insert(0, node)
        
    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
    
        
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item, priority):
        pair = (priority, item)
        self.queue.append(pair)
        self.queue = sorted(self.queue, key=lambda x: x[0])

    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)[1]

    def is_empty(self):
        return len(self.queue) == 0
        
# f = Queue()
# f.add(Node((2, 1), None, None, 0))
# f.add(Node((2, 2), None, None, 0))
# f.add(Node((2, 3), None, None, 0))
# f.add(Node((2, 4), None, None, 0))

# print(f.get().state)
# print(f.is_empty())
# f.remove()
# print(f.get().state)
# print(f.contains(Node((2, 1), None, None, 0)))
# print(f.contains(Node((2, 3), None, None, 0)))
