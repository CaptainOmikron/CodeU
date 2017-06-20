
'''
Returns the Kth to last value in a linked list l.
There was a discussion on Slack and
apparently we can expect l to actually be a 
linked list and k to be smaller than len(l).
So we don't have to do input handling.
______________________________________________
Idea: Follow the links while keeping the last
k+1 values cached. 
So when we hit the end (A node pointing to None)
the value that we are looking for is the 
"oldest" value in the cache
______________________________________________
COMPLEXITY:
A) SPACE:
I might be missing something, but I think this 
should just be k since thats how much we cache
at any point.
B) TIME:
Let L be the length of the linked list.
We will have to perform L "cache.add"s. The
add-function might (in a best case scenario) 
only have to append something( if the capacity
is not yet used up). But most of the time
(worst case) it will have to append (O(1)) and
delete the first item (O(K)).
So I think the complexity should on average/
worst case be O(L*K). 
(Best Case: O(L). This happens if K=L. But then
our cache will contain all elements in the 
linked list, so our space complexity will be 
at its worst)
But it does feel like I'm missing something :D
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


