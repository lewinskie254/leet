
# def trap(heights): 
#     n = len(heights)
#     i = 0
#     potential_walls = set()
#     processed_pairs = []

#     while i < n-1: 
#         if heights[i] > 0: 
#             to_append = max(heights[i], heights[i+1])
#             if to_append == heights[i]:
#                 index = i 
#             else: 
#                 index = i + 1
            
#             processed_pairs.append([to_append, index])
#         i += 1
    
#     for i in range(len(processed_pairs)): 
#         potential_walls.add(processed_pairs[i][1])

#     total_area = 0
#     a = 0 
#     b = 1 
#     potential_walls = list(potential_walls)
#     while a < len(potential_walls) and b < len(potential_walls):
#         print(a, b, total_area)
#         total_area += min(heights[potential_walls[a]], heights[potential_walls[b]]) * ((b) - a)
#         a +=1 
#         b +=1
    

#     return total_area



#completely wrong 
def trapper(heights):
    if not heights:  # If the list is empty, return 0
        return 0
    
    n = len(heights)
    left, right = 0, n - 1  # Pointers at the leftmost and rightmost positions
    left_max, right_max = heights[left], heights[right]  # Max heights seen so far from left and right
    total_area = 0
    
    while left < right:
        if left_max < right_max:
            # If the left_max is smaller, the trapped water depends on left_max
            left += 1
            left_max = max(left_max, heights[left])
            total_area += left_max - heights[left]
            print(left_max, heights[left], total_area, "left")
        else:
            # If the right_max is smaller, trapped water depends on right_max
            right -= 1
            right_max = max(right_max, heights[right])
            total_area += right_max - heights[right]
            print(right_max, heights[right], total_area, "right")
    return total_area