def jump(nums):
    length = len(nums)
    count = 1
    i = 1
    j = 0
    index = 0
    x = 0 
    if length < 2: 
        count = 0
    while i < length: 
        if nums[i] < length: 
            j = nums[i]
            if j < length: 
                index = i + j
                if index < length:
                    x = length - (index  + 1)
                    count += 1
                    if x <= 0: 
                        break
                else: 
                    count += 1
        i += 1
    return count 

print(jump([1,2,3]))


def jumper(nums):
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= len(nums) - 1:
                break
    
    return jumps

print(jumper([2,3,1,1,4]))