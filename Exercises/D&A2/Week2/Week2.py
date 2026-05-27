#Increasing combinations of vertices.
def allVertexCombinations(n):
    combinations = [[]]

    for i in range(1,n+1):
        #Get all subsets from the already existing ones, which have a length
        #of one element shorter than the ones that we want to make
        temp = [subset for subset in combinations if len(subset) == i - 1]
        #For each index(number or numbers in the set), I want to go 
        # through all numbers and generate a combination with index 
        # number of items inside
        for j in range(1,n+1):
            for k in range(0,len(temp)):
                #checks if the previous subset is an empty set and also
                #checks if the element to be added to the previous subset 
                # is bigger than the elements which are already in the subsets 
                # preventing subsets like (2,1) or (1,1) and equivalet from being created.
                if temp[k] == [] or j > temp[k][-1]:
                    combinations.append(temp[k] + [j])
    
    return combinations
            
# print(allVertexCombinations(4))

#Increasing-size Vertex Cover
import sys
sys.path.append('../Week1')
from Week1 import checkCover


def findCoverByIncreasing(matrix):
    allIncreasingCombinations = allVertexCombinations(len(matrix))

    for combination in allIncreasingCombinations:
        if checkCover(matrix, combination):
            return combination
            
    return []

matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]
# print(findCoverByIncreasing(matrix, 4))