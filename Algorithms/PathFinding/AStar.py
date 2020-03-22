class AStar(object):
    """
    Implementation of A* path finder algorithm
    matrix elements:
        o: free path
        X: obstacles
        S: starting point
        E: ending point
    """
    open = []
    closed = []

    def __init__(self, matrix, startingPoint, endingPoint, obstacle = '█'):
        self.matrix = matrix
        self.start = startingPoint
        self.end = endingPoint
        self.obstacle = obstacle
    
    def calculateH(self, startPoint, endPoint):
        # Euclidian distance
        return (sum([(a - b) ** 2 for a, b in zip(startPoint, endPoint)]))**0.5

    def getNeighborList(self, matrix, node):
        x, y = node.point
        neighborList = []

        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]) and (i,j) != (x,y) and matrix[i][j] != self.obstacle:
                    # gCost
                    # | 14 | 10 | 14 |    | x-1, y-1 | x, y-1 | x+1, y-1 |
                    # | 10 | X  | 10 | => |  x-1, y  |  x, y  |  x+1, y  |
                    # | 14 | 10 | 14 |    | x-1, y+1 | x, y+1 | x+1, y+1 |
                    gCost = (14 if i != x and j != y else 10)
                    hCost = self.calculateH((i,j), self.end)
                    neighbor = Node((i,j), matrix[i][j], gCost, hCost, node)
                    neighborList.append(neighbor)
        return neighborList

    def checkElementInList(self, list, element, cost):
        for e in list:
            if e == element and cost < element.gCost:
                return True
        return False

    def printMatrix(self, matrix):
        for i in range(len(matrix)):
            print(matrix[i])

    def findPath(self):
        x,y = self.start
        startNode = StartNode(self.start, hCost=self.calculateH(self.start, self.end), value='S')
        x,y = self.end
        endNode = EndNode(self.end, value='E')
        self.open.append(startNode)

        while len(self.open) != 0:
            self.open.sort(key=lambda x: x.fCost)
            q = self.open[0]
            print(f"current Node is ({q.point} with G: {q.gCost}, H: {q.hCost}, and F: {q.fCost})")
            self.matrix[q.point[0]][q.point[1]] = '*'
            self.printMatrix(self.matrix)

            if q.value == endNode.value:
                # The algorithm found the ending point, the path is contained in the list of closed nodes
                return

            self.open.pop(0)
            self.closed.append(q)

            neighborList = self.getNeighborList(self.matrix, q)

            for neighbor in neighborList:
                
                for inClosed in self.closed:
                    if inClosed == neighbor:
                        continue

                cost = q.gCost + neighbor.gCost
                inOpen = self.checkElementInList(self.open, neighbor, cost)
                inClosed = self.checkElementInList(self.closed, neighbor, cost)

                if inOpen:
                    self.open.remove(neighbor)
                if inClosed:
                    self.closed.remove(neighbor)

                if not inOpen and not inClosed:
                    self.open.append(neighbor)

class Node():
    gCost = 0
    hCost = 0
    fCost = 0
    parent = None

    def __init__(self, point, value='*', gCost=0, hCost=0, parent=None):
        self.gCost = gCost
        self.hCost = hCost
        self.fCost = gCost+hCost
        self.point = point
        self.parent = parent
        self.value = value

    def __eq__(self, other): 
        if not isinstance(other, Node):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.gCost == other.gCost and self.hCost == other.hCost and self.fCost == other.fCost and self.point == other.point and self.parent == other.parent and self.value == other.value 

class StartNode(Node):
    def __init(self, point, hCost, value):
        Node.__init__(self, point, value)
        self.fCost = 0

class EndNode(Node):
    def __init(self, point, value):
        Node.__init__(self, point, value)