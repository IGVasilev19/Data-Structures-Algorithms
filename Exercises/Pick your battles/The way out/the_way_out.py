


def findShortestPath(maze, startR, startC, pathLength):
    for i in range (startR, len(maze)):
        for j in range (startC, len(maze[0])):
            if maze[i][j+1] == 2:
                pathLength += 1
                return pathLength

            if maze[i][j-1] == 2:
                pathLength += 1
                return pathLength
            
            if maze[i+1][j] == 2:
                pathLength += 1
                return pathLength
            
            if maze[i-1][j] == 2:
                pathLength += 1
                return pathLength
            
            if maze[i][j+1] == 1 and visited.count(maze[i][j+1]) == 0:
                visited.append((maze[i][j],pathLength))
                pathLength += 1
                findShortestPath(maze,i,j+1, pathLength)
            
            elif maze[i][j-1] == 1 and visited.count(maze[i][j-1]) == 0:
                visited.append((maze[i][j],pathLength))
                pathLength += 1
                findShortestPath(maze,i,j-1, pathLength)

            elif maze[i+1][j] == 1 and visited.count(maze[i+1][j]) == 0:
                visited.append((i, j, pathLength))
                pathLength += 1
                findShortestPath(maze,i+1,j, pathLength)

            elif maze[i-1][j] == 1 and visited.count(maze[i-1][j]) == 0:
                visited.append((maze[i][j],pathLength))
                pathLength += 1
                findShortestPath(maze,i-1,j, pathLength)
            else:
                i, j, pathLength = visited[-1]
                findShortestPath(maze, i, j, pathLength)


maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

startR = 1
startC = 1
pathLength = 0
visited = []

print(findShortestPath(maze, startR, startC, pathLength))