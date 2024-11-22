import json


def validSudoku(nums_rows): 
    n = len(nums_rows)

    if n != 9:
        return False
    
    soduku_dict = {}
    for i in range(len(nums_rows)): 
        for j in range(len(nums_rows[i])):
            if len(nums_rows[i]) != 9: 
                   return False 
            if (i + 1) % 3 == 0:
                if (j + 1) % 3 == 0:
                    soduku_dict[i-2, j-2] =[]
                    soduku_dict[i-2, j-2].extend([
                        nums_rows[i-2][j-2],nums_rows[i-2][j-1], nums_rows[i-2][j], 
                        nums_rows[i-1][j-2],nums_rows[i-1][j-1], nums_rows[i-1][j], 
                        nums_rows[i][j-2],nums_rows[i][j-1], nums_rows[i][j]
                    ]
                    )

    for element in soduku_dict: 
        validator = []
        for each_num in soduku_dict[element]:
            if each_num.isnumeric():
                if each_num in validator:
                    return False
                else: 
                    validator.append(each_num)

    return True 
    
#tests_passed 368 / 507


print(validSudoku(
[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))


#correctVersion

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Helper function to validate if a list contains duplicates (ignoring '.')
        def is_valid_unit(unit):
            nums = [num for num in unit if num != '.']
            return len(nums) == len(set(nums))

        # Validate rows
        for row in board:
            if not is_valid_unit(row):
                return False

        # Validate columns
        for col in zip(*board):  # Transpose rows to columns
            if not is_valid_unit(col):
                return False

        # Validate 3x3 subgrids
        for i in range(0, 9, 3):  # Top-left corner of each subgrid
            for j in range(0, 9, 3):
                subgrid = [
                    board[x][y]
                    for x in range(i, i + 3)
                    for y in range(j, j + 3)
                ]
                if not is_valid_unit(subgrid):
                    return False

        return True
