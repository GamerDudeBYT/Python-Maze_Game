import random

def load_maze(width, height):
    # create a blank grid
    grid = {}

    for x in range(width):

        for y in range(height):

            nodes = [(i,j) for i,j in [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]
                     if 0 <= i < width and 0 <= j < height ]

            grid[(x, y)] = nodes

    # traverse every node
    current = next(iter(grid))

    visited = {key: False for key in grid}

    stack = [current]

    visited[current] = True

    path = []

    while len(stack) > 0:
        path.append(current)
        unvisited = [n for n in grid[current] if not visited[n]]

        if len(unvisited) == 0:
            current = stack.pop()

        else:
            stack.append(current)
            current = random.choice(unvisited)
            visited[current] = True

    graph = {key: [] for key in grid}

    for i in range(len(path)-1):
        graph[path[i]].append(path[i+1])
        # If you want the path to be bidirectional
        graph[path[i+1]].append((path[i]))

    return graph

       