def convert(s: str, numRows: int) -> str:
    # Edge case: if only one row, return the original string
    if numRows == 1 or numRows >= len(s):
        return s
    
    # Initialize an empty list for each row
    rows = [''] * numRows
    current_row = 0
    going_down = False

    # Traverse the string and populate rows
    for char in s:
        rows[current_row] += char
        # Change direction at the top or bottom row
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        # Update the row index based on direction
        current_row += 1 if going_down else -1

    # Join all rows to form the final string
    return ''.join(rows)
