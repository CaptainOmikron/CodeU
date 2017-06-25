
'''
-   Takes a grid g of booleans, that represent land (=1) and water (=0)
    and its dimensions (r is the number of rows, c the number of coloumns)
-   Returns the number of disjoint islands
'''
def countIslands(r, c, grid):
    islands = [] # array of sets of tuples. Each set represents an island. It contains the coordinates of all its landtiles
    # now traverse the grid and find and merge islands
    for ri in range(r): # rowindex
        for ci in range(c): # coloumnindex
            if grid[ri][ci] == True:
                neighbours = getRelevantNeighbours(r, c, ri, ci) # because we traverse the grid left to right and up to down, we only need the neighbours above and left
                assigned = False # flags if we already assigned the current tile to an island
                # now go through neighbours and search for islands:
                for n in neighbours:
                    for i in islands:
                        if n in i:
                            if assigned == True: # if we already assigned the tile to an island, we want to merge:
                                i.add((ri, ci))
                                mergedIsland = i|assignedIsland
                                islands.remove(i)
                                if i != assignedIsland:
                                    islands.remove(assignedIsland)
                                islands.append(mergedIsland)
                                assignedIsland = mergedIsland
                            else: # if we havent assigned the tile to an island before, we can simply add it
                                i.add((ri, ci))
                                assigned = True
                                assignedIsland = i
                if assigned == False: 
                    # we land here if the tile doesnt have any known islands as neighbours
                    # so we create a new island for our landtile:
                    newIsland = set()
                    newIsland.add((ri, ci))
                    islands.append(newIsland) # The set/tupel-syntax doesnt allow me to write it all in one line
    return len(islands)

'''
-   Takes number of rows and coloums (r, c) + row and coloumn index (ri, ci)
-   Returns the neighbours (only up and left, because they are relevant in this context)
    but only if they exist (by checking whith the dimensions of the grid)
'''
def getRelevantNeighbours(r, c, ri, ci): # number of rows and coloumns (r, c) + row and coloumn index (ri, ci)
    neighbours = []
    if (ri != 0):
        neighbours.append((ri-1, ci)) # up
    ''' We dont need these anymore:
    if (ri != r-1):
        neighbours.append((ri+1, ci)) # down
    if (ci != c-1):
        neighbours.append((ri, ci+1)) # right
    '''
    if (ci != 0):
        neighbours.append((ri, ci-1)) # left
    return neighbours



#######
# Primitive tests:
grid = [[0,0,0], [0,1,0], [0,0,0]]
r = 3
c = 3
assert ((countIslands(r, c, grid))==1)

grid = [[0,1,0,1], [1,1,0,0], [0,0,1,0], [0,0,1,0]]
r = 4
c = 4
assert((countIslands(r,c,grid))==3)

grid = [[0,0,0,0], [0,0,0,0],[0,0,0,0],[0,0,0,0]]
r = 4
c = 4
assert((countIslands(r,c,grid))==0)

grid = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
r = 4
c = 4
assert((countIslands(r,c,grid))==1)
