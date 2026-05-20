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

def checkCover(matrix, vertices):
    