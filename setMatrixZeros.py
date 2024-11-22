def setZeros(matrix): 
    n = len(matrix)
    m = len(matrix[0])
    changer = {}

    for i in range(n):
        changer[i] = []

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                changer[i].append(j)
    
    for element in changer:
        element_length = len(changer[element])
        for i in range(element_length): 
            for j in range(m): 
                matrix[element][j] = 0
            for j in range(n): 
                matrix[j][changer[element][i]] = 0



print(setZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
#worked all 