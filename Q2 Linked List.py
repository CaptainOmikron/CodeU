
'''
Returns the Kth to last value in a linked list.
There was a discussion on Slack and
apparently we can expect k and l
to be valid input.
______________________________________________
Idea: Follow the links while keeping the last
k+1 values cached. 
So when we hit the end (A node pointing to None)
the value that we are looking for is the 
"oldest" value in the cache
''' 
def getKthToLast(l, k):
    cache = Cache(k+1)
    currentNode = l.first
    cache.add(currentNode)
    while (currentNode.next != None):
        currentNode = currentNode.next
        cache.add(currentNode) 
    return cache.get().data

'''
A simple FIFO fixed size queue.
Curiously, I could not find anything
like this in any library.
'''
class Cache:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity

    def add(self, x): #FIFO
        if len(self.data) < self.capacity:
            self.data.append(x)
        else:
            del self.data[0]
            self.data.append(x)
    def get(self): #FIFO
        return self.data[0]

'''
A simple structure for linked lists.
It wasn't asked for, but I wanted to
run a few examples :) 
'''
class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class linked_list: 
    def __init__(self, firstValue = None):
        self.first = node(data = firstValue)

    # add at the beginning
    def add(self, data):
        new_node = node(data, self.first) 
        self.first = new_node 


