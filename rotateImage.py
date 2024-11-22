def rotate(matrix): 
    n = len(matrix)

    dict_of_elements = {}

    for i in range(n):
        dict_of_elements[i] = matrix[i]
    
    output_dictionary = {}

    for i in range(len(dict_of_elements)):
        output_dictionary[i] = []

    i = len(matrix[0])-1
    
    while i >= 0: 
        for j in range(len(dict_of_elements), 0, -1): 
            output_dictionary[i].append(dict_of_elements[j-1][i])
        i -= 1
    
    output_list = []
    for i in range(len(output_dictionary)):
        output_list.append(output_dictionary[i])
        

    for i in range(len(output_list)):
        for j in range(len(output_list[i])):
            matrix[i][j] = output_list[i][j]

    return matrix 
#passed all the tests 