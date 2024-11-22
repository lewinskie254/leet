def spiralMatrix(matrix):
    output_array = []
    for i in range(len(matrix)):
        if i == 0:
            for j in range(len(matrix[i])):
                output_array.append(matrix[i][j])

    for i in range(len(matrix)): 
        if i > 0:
            output_array.append(matrix[i][len(matrix[i])-1])

    for i in range(len(matrix)): 
        if i == len(matrix) -1 and i != 0: 
            for j in range(len(matrix[i])-2, -1, -1): 
                output_array.append(matrix[i][j])
    
    for i in range(len(matrix)-1, -1, -1): 
        if i > 1 and i % 2 == 1: 
            for j in range(len(matrix[i])-1): 
                output_array.append(matrix[i][j])
        if i > 1 and i % 2 == 0 and i < len(matrix)-1: 
            for j in range(len(matrix[i])-1, -1, -1): 
                output_array.append(matrix[i][j])

    return output_array

print(spiralMatrix([[1,2],[3,4]]))
#passed 11 out of 26 tests 


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []  # Handle empty matrix
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []
        
        while top <= bottom and left <= right:
            # Traverse from left to right along the top boundary
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1  # Move top boundary down
            
            # Traverse from top to bottom along the right boundary
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Move right boundary left
            
            if top <= bottom:
                # Traverse from right to left along the bottom boundary
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1  # Move bottom boundary up
            
            if left <= right:
                # Traverse from bottom to top along the left boundary
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Move left boundary right
        
        return result

