#All combinations of vertices

def all_combinations(vertices):
    combinations = [[]]
    n = len(vertices)

    for i in range(0, n):
        temp = combinations.copy()

        for j in range(0, len(temp)):
            temp[j] = temp[j] + [vertices[i]]

        combinations.extend(temp)

    return combinations


# test = [1,2,3,4]
# print(all_combinations(test))


#Vertex Cover check

def getAllEdges(matrix):
    allEdges = []

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 1:
                allEdges.append([i+1]+[j+1])

    return allEdges

def checkCover(matrix, vertices):
    allPairs = getAllEdges(matrix)

    for pair in allPairs[:]:
        if any(vertex in vertices for vertex in pair):
            allPairs.remove(pair)

    if len(allPairs) == 0:
        return True

    return False


# matrix = [
#     [0, 1, 1, 0, 0, 0, 0, 0, 0],
#     [1, 0, 1, 0, 0, 1, 0, 0, 0],
#     [1, 1, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 1, 1, 0, 0, 1, 0, 0],
#     [0, 1, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 1, 1, 0, 1, 1],
#     [0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0, 0],
# ]

# print(checkCover(matrix,[1,2,3]))


#Brute-force Vertex Cover
def findCover(matrix, vertices):
    allCombinations = all_combinations(vertices)
    bestCombination = [0] * 1000

    for combination in allCombinations:
        if checkCover(matrix, combination) and len(combination) < len(bestCombination):
            bestCombination = combination
            
    return bestCombination

# matrix = [
#     [0, 1, 1, 0, 0, 0, 0, 0, 0],
#     [1, 0, 1, 0, 0, 1, 0, 0, 0],
#     [1, 1, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 1, 1, 0, 0, 1, 0, 0],
#     [0, 1, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 1, 1, 0, 1, 1],
#     [0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0, 0],
# ]

# print(findCover(matrix,[1,2,3,4,5,6,7,8,9]))


def getAllPossiblePairs(vertices):
    pairs = []
    
    for vertice in vertices:
        for i in range(0, len(vertices)):
            if vertice != vertices[i]:
                pairs.append([vertice,vertices[i]])

    return pairs

import random

def should_do(p):
    return random.random() <= p

def graphGenerator(vertices, p):
    pairs = getAllPossiblePairs(vertices)
    matrix = [[0] * len(vertices) for _ in range(len(vertices))]

    for pair in pairs:
        if should_do(p):
            matrix[pair[0]-1][pair[1]-1] = 1

    return matrix

