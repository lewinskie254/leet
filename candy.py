def candy(ratings): 

    if len(ratings) < 1: 
        return 1
    
    if ratings == []: 
        return 0 

    total_candies = [1] * len(ratings)
    for i, num in enumerate(ratings): 
        if i > 0: 
            if num < ratings[i - 1]:
                total_candies[i] = min(total_candies[i] + 1, total_candies[i] + (ratings[i-1]- ratings[i]))
        if i < len(ratings)-1: 
            if num < ratings[i + 1]:
                total_candies[i] = min(total_candies[i] + 1, total_candies[i] + (ratings[i+1]- ratings[i]))
    
    return sum(total_candies)

# got 17 out of 48 
print(candy([1,3,2,2,1]))

#correct one  
def candy(ratings):
    n = len(ratings)
    if n == 0:
        return 0

    # Initialize each child with 1 candy
    total_candies = [1] * n

    # First pass (left to right)
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            total_candies[i] = total_candies[i - 1] + 1

    # Second pass (right to left)
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            total_candies[i] = max(total_candies[i], total_candies[i + 1] + 1)

    return sum(total_candies)
