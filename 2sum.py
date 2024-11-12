def twosum(numbers, target): 

    if numbers == []: return 

    starting_pointer = 0 
    second_pointer = 1 

    while second_pointer < len(numbers) and starting_pointer < second_pointer: 
        if numbers[starting_pointer] + numbers[second_pointer] == target:
            return [starting_pointer + 1, second_pointer + 1] 
        elif numbers[starting_pointer] + numbers[second_pointer] > target:
            return []
        if second_pointer >= len(numbers) or numbers[second_pointer] > (target - numbers[starting_pointer]): 
            starting_pointer += 1
        if numbers[second_pointer] < target: 
            second_pointer += 1
        else: 
            starting_pointer += 1
        if second_pointer >= len(numbers): 
            starting_pointer + 1
    
print(twosum([5,25,75], 100))
#6 out of 24

#correct one 
def two2sum(numbers, target): 
    if not numbers:
        return None

    starting_pointer = 0
    second_pointer = 1

    while starting_pointer < len(numbers) - 1:
        if numbers[starting_pointer] + numbers[second_pointer] == target:
            return [starting_pointer + 1, second_pointer + 1]
        elif numbers[starting_pointer] + numbers[second_pointer] < target:
            second_pointer += 1
        else:
            starting_pointer += 1
            second_pointer = starting_pointer + 1

        if second_pointer >= len(numbers):
            starting_pointer += 1
            second_pointer = starting_pointer + 1

    return []

print(two2sum([5, 25, 75], 100))

#passed 19 out of 24 


def twosum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

# Test case
print(twosum([5, 25, 75], 100))
