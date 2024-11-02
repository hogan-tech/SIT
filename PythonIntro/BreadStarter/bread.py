from collections import defaultdict

def readImage(filePath):
    with open(filePath, 'r') as file:
        matrix = []
        for line in file:
            row = [int(x) for x in line.strip().split()]
            matrix.append(row)
    return matrix

def outputGrid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def firstPass(grid):
    rows, cols = len(grid), len(grid[0])
    label = 2
    labelRelationships = defaultdict(int)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                top = grid[r-1][c] if r > 0 else 0
                left = grid[r][c-1] if c > 0 else 0

                if top == 0 and left == 0:
                    grid[r][c] = label
                    label += 1
                elif top != 0 and left == 0:
                    grid[r][c] = top
                elif top == 0 and left != 0:
                    grid[r][c] = left
                else:
                    if top < left:
                        grid[r][c] = top
                        labelRelationships[left] = top
                    elif left < top:
                        grid[r][c] = left
                        labelRelationships[top] = left
                    else:
                        grid[r][c] = top
    
    return grid, labelRelationships


def secondPass(grid, labelRelationships):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            label = grid[r][c]
            while label in labelRelationships:
                label = labelRelationships[label]
            grid[r][c] = label
    return grid


def thirdPass(grid):
    uniqueLabels = set()
    for row in grid:
        for label in row:
            if label > 1:  
                uniqueLabels.add(label)
    return len(uniqueLabels)
