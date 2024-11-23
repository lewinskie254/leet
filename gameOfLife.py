import json 
def gameOfLife(board): 

    n = len(board)
    m = len(board[0])

    #create a dictionary of list of all elements for each entry 
    dict_of_all_entries = {}

    if m > 1 and n > 1: 
        for i in range(n):
            for j in range(m): 
                dict_of_all_entries[(i,j)] = []

        #first populate the first element of each list with the list item 
        for i in range(n):
            for j in range(m): 
                dict_of_all_entries[(i,j)].append(board[i][j])
                
        for i in range(n):
            for j in range(m): 
                if i > 0 and i < n-1:
                    if j > 0 and j < m-1: 
                        list_of_elements = [board[i][j-1], board[i][j+1], board[i-1][j], board[i+1][j], board[i-1][j-1], board[i-1][j+1], board[i+1][j-1], board[i+1][j+1]]
                    elif j > 0 and j >= m-1: 
                        list_of_elements = [board[i][j-1], board[i-1][j], board[i+1][j], board[i-1][j-1], board[i+1][j-1]]
                    elif j == 0 and j < m-1: 
                        list_of_elements = [board[i][j+1], board[i-1][j], board[i+1][j], board[i-1][j+1], board[i+1][j+1]]
                elif i > 0 and i >= n-1:
                    if j > 0 and j < m-1: 
                        list_of_elements = [board[i][j-1], board[i][j+1], board[i-1][j], board[i-1][j-1], board[i-1][j+1]]
                    elif j > 0 and j >= m-1: 
                        list_of_elements = [board[i][j-1], board[i-1][j], board[i-1][j-1]]
                    elif j == 0 and j < m-1: 
                        list_of_elements = [board[i][j+1], board[i-1][j], board[i-1][j+1]]
                elif i == 0 and i < n-1: 
                    if j > 0 and j < m-1: 
                        list_of_elements = [board[i][j-1], board[i][j+1], board[i+1][j], board[i-1][j+1], board[i+1][j-1], board[i+1][j+1]]
                    elif j > 0 and j >= m-1: 
                        list_of_elements = [board[i][j-1], board[i+1][j], board[i+1][j-1]]
                    elif j == 0 and j < m-1: 
                        list_of_elements = [board[i][j+1], board[i+1][j], board[i+1][j+1]]
                dict_of_all_entries[(i,j)].extend(list_of_elements)

        for element in board:
            print(element)
        print("---------------")
        for i in range(n):
            for j in range(m):
                if dict_of_all_entries[(i, j)][0] == 0:
                    if dict_of_all_entries[(i, j)][1:].count(1) == 3: 
                        board[i][j] = 1 
                elif dict_of_all_entries[(i, j)][0] == 1: 
                    if dict_of_all_entries[(i, j)][1:].count(1) == 2 or dict_of_all_entries[(i, j)][1:].count(1) == 3: 
                        board[i][j] = 1 
                    elif dict_of_all_entries[(i, j)][1:].count(1) < 2: 
                        board[i][j] = 0
                    elif dict_of_all_entries[(i, j)][1:].count(1) > 3:
                        board[i][j] = 0
    
        for element in board:
            print(element)
        print("---------------")
    

print(gameOfLife([[0,1,1,0,1,1,1,0],[1,1,0,1,1,0,0,0],[0,0,0,0,0,1,1,1],[1,1,1,1,0,0,0,0],[0,1,0,0,1,1,1,0]]))