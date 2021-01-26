
def wordSearch(r, c, g, d): # see comment below for explanation
    words = set() # use set to avoid duplicates
    for ri in range(r): #rowindex
        for ci in range(c): # columnindex
            words = words | findWords(r, c, g, d, ri, ci, list = set()) # finds words that start at this cell (ri, ci)
    return words

def findWords(r, c, g, d, rowIndex, columnIndex, currentString = '', alreadyVisited = None, list = set()): # called by wordSearch and itself
    # see comment below 
    if alreadyVisited == None:
        alreadyVisited = [[False for i in range(c)] for i in range(r)]
    alreadyVisited[rowIndex][columnIndex] = True
    currentString += g[rowIndex][columnIndex]
    if d.isWord(currentString):
        list.add(currentString)
    for rowI in (rowIndex-1, rowIndex, rowIndex+1):
        for colI in (columnIndex-1, columnIndex, columnIndex+1):
            if not (rowI<0 or colI<0 or rowI>=r or colI>=c):
                if not alreadyVisited[rowI][colI]:
                    if d.isPrefix(currentString + g[rowI][colI]):
                        list = list | findWords(r, c, g, d, rowI, colI, currentString, alreadyVisited, list)
                        alreadyVisited [rowI] [colI] = False
    return list

'''
r is the number of rows and c is the 
number of columns.
g is the grid that we want to search.
It's a 2d array. I now want to define 
what rows and columns are. This is not
mandatory since the problem is symmetric
but I find that it makes the code easier 
to read:
I want to adress the grid like a matrix. 
So
a b c
d e f
g h i
would translate to 
gr = [[a,b,c],[d,e,f],[g,h,i]] 
(plus quotation marks)
That way gr[0][2] == c
So the first index gives me the row and
the second one the column.

Now d - the dictionary - is a bit more 
complicated. The way I understand the
question is:
The dictionary is an object of a class 
that doesn't give us direct access to 
the dictionary. We can however ask if
a specific word or prefix is in the 
dictionary via the member functions
isWord() and isPrefix()
In the appendix-section of this code 
I give a quick implementation( with
horrible complexity, but that's not
the point :D) to clarify what d looks 
like.

wordSearch() traverses the grid and 
calls the findWords() function from 
every cell. findWords() finds all 
words, that start at this cell.
It does this by checking with isPrefix()
if one or more neighbours are 
potential candidates to form a word
and then calls itself with all of 
these candidates. The recursion ends
when all neighbours are either non-existent,
already visited or none of them can 
create a prefix.
findWords() uses the 2d-array of 
bools called alradyVisited that has 
the same dimensions as the grid and 
tells us whether or not we have 
already used the letter of a cell 
while building the current word.
'''

############
# Appendix:
# you can just skip anything below this unless you're interested :)
############

class dict(): # inefficient but its just there to run examples 
    def __init__(self, dict):
        self.__dict = dict

    def isWord(self, s):
        for i in self.__dict:
            if s == i:
                return True
        return False

    def isPrefix(self, p):
        for i in self.__dict:
            currentPrefix = ''
            for j in i:
                currentPrefix += j
                if currentPrefix == p:
                    return True
        return False


###############
# Primitive Tests:
# the first test for wordSearch is the example case
###############

# Test the dictionary class
d = ['car', 'card', 'cart', 'cat']
dObject = dict(d)
p = ['c', 'ca', 'car', 'card', 'cart', 'cat']
for i in d:
    assert(dObject.isWord(i))
for j in p:
    assert(dObject.isPrefix(j))

# test wordSearch
grid1 = [['a', 'a', 'r'], ['t', 'c', 'd']]
dictionary1 = dict(['car', 'card', 'cart', 'cat'])
assert(set(wordSearch(2, 3, grid1, dictionary1)) == set(['cat', 'card', 'car']))

grid2 = [['a', 'f', 'b', 'x', 'o'], ['p', 'k', 'e', 'd', 'n'], ['l', 'y', 'n', 'm', 'a']]
dictionary2 = dict(['feynman'])
assert(set(wordSearch(3, 5, grid2, dictionary2)) == set(['feynman']))

grid3 = [['t', 'h', 'a', 'o'],['a', 'c', 'x', 's'], ['f', 'f', 'x', 'x']]
dictionary3 = dict(['cat', 'chaos', 'caff', 'xxxxxxxxxxx', 'covfefe'])
assert(set(wordSearch(3, 4, grid3, dictionary3)) == set(['cat', 'chaos', 'caff']))

