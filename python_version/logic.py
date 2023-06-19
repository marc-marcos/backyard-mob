import random

def update_cells(matrix):
    ROW_COUNT = len(matrix)
    cell_matrix = matrix

    for i in range(ROW_COUNT):
        for j in range(ROW_COUNT):
            if matrix[i][j] == 1: # Team A
                my_own = count_around(matrix, (i, j), 1)
                enemy = count_around(matrix, (i, j), 2)

                if (2*enemy > my_own):
                    cell_matrix[i][j] = 2
                
                elif (enemy > my_own): 
                    cell_matrix[i][j] = 0

                else:
                    if (random.randint(0, 100) > 95):
                        cell_matrix[i][j] = 0
                
            elif matrix[i][j] == 2: # Team B
                my_own = count_around(matrix, (i, j), 2)
                enemy = count_around(matrix, (i, j), 1)

                if (2*enemy > my_own):
                    cell_matrix[i][j] = 1
                
                elif (enemy > my_own): 
                    cell_matrix[i][j] = 0

                else:
                    if (random.randint(0, 100) > 95):
                        cell_matrix[i][j] = 0
        
            else: # Empty
                team_a = count_around(matrix, (i, j), 1)
                team_b = count_around(matrix, (i, j), 2)

                if (team_a > team_b):
                    cell_matrix[i][j] = 1
                
                elif (team_b > team_a):
                    cell_matrix[i][j] = 2


    return cell_matrix

def count_around(matrix, item, element):
    total = 0
    ROW_COUNT = len(matrix)

    # count how many of the item are around the element

    # top left
    if item[0] > 0 and item[1] > 0 and matrix[item[0]-1][item[1]-1] == element:
        total += 1

    # top
    if item[0] > 0 and matrix[item[0]-1][item[1]] == element:
        total += 1

    # top right
    if item[0] > 0 and item[1] < ROW_COUNT-1 and matrix[item[0]-1][item[1]+1] == element:
        total += 1

    # right
    if item[1] < ROW_COUNT-1 and matrix[item[0]][item[1]+1] == element:
        total += 1

    # bottom right
    if item[0] < ROW_COUNT-1 and item[1] < ROW_COUNT-1 and matrix[item[0]+1][item[1]+1] == element:
        total += 1

    # bottom
    if item[0] < ROW_COUNT-1 and matrix[item[0]+1][item[1]] == element:
        total += 1

    # bottom left
    if item[0] < ROW_COUNT-1 and item[1] > 0 and matrix[item[0]+1][item[1]-1] == element:
        total += 1

    # left
    if item[1] > 0 and matrix[item[0]][item[1]-1] == element:
        total += 1

    return total

def check_winnage(matrix):
    ROW_COUNT = len(matrix)
    team_a = True
    team_b = True

    for i in range(ROW_COUNT):
        for j in range(ROW_COUNT):
            if matrix[i][j] == 1:
                team_b = False

            elif matrix[i][j] == 2:
                team_a = False
            
    if (team_a == False and team_b == False): 
        return 0
    
    else:
        return 1 if team_a else 2