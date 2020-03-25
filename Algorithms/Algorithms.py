from Sort.BubbleSort import BubbleSort
from Sort.QuickSort import QuickSort
from Sort.MergeSort import MergeSort
from PathFinding.AStar import AStar

# region Sorting algorithms

#bs = BubbleSort(9,8,7,6,5,4,3,2,1)
#print(bs)
#bs.Sort()
#print(bs)

#qs = QuickSort(9,8,7,6,5,4,3,2,1)
#print(qs)
#qs.Sort()
#print(qs)

qs = MergeSort(6,3,4,7)
print(qs)
qs.Sort()
print(qs)

# endregion

#region Path finder algorithm
#def getMatrix(n):
#    return [[' ' for col in range(n)] for row in range(n)]

#def setObstacles(obstacles, matrix):
#    for obstacle in obstacles:
#        i, j = obstacle
#        matrix[i][j] = '█'

#    return matrix

#def setStartAndEnd(matrix, start, end):
#    i,j = start
#    matrix[i][j] = 'S'
#    i,j = end
#    matrix[i][j] = 'E'
#    return matrix

#def printMatrix(matrix):
#    for i in range(len(matrix)):
#        print(matrix[i])

#n=10
#matrix = getMatrix(n)

## set the obstacles
#obstacles = [(3,1), (3,2), (3,3), (3,4), (4,4), (5,4),(6,4), (7,4), (7,5), (7,6), (7,7), (7,8)]

#matrixWithObstacles = setObstacles(obstacles, matrix)

#print("original matrix:\n")
#printMatrix(matrix)

#print("matrix with obstacles:\n")
#printMatrix(matrixWithObstacles)

#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#[0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
#[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
#[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
#[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
#[0, 0, 0, 0, 1, 1, 1, 1, 1, 0]
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# setting up start and end
#startPoint = (0,1)
#endPoint = (9,9)

#finalMatrix = setStartAndEnd(matrixWithObstacles, startPoint, endPoint)
#print("final matrix:\n")
#printMatrix(finalMatrix)

#print("Using A* to find the shortest path from the starting point('S') to the ending point('E'), avoiding the obstacles ('█')\n")

#aStar = AStar(finalMatrix, startPoint, endPoint)
#aStar.findPath()
#print("\nThe best path is:\n")
#for el in aStar.closed:
#    print(el.point)

##endregion


#for i in range(100):
#    if i%3==0 and i%5==0:
#        print("FizzBuzz")
#    elif i%3==0:
#        print("Fizz")
#    elif i%5==0:
#        print("Buzz")
#    else:
#        print(i)