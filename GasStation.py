def canCompleteCircuit(gas, cost): 
    n = len(gas)
    truth_checker = [0] * n 

    for i in range(len(gas)): 
        if gas[i] >= cost[i]: 
            truth_checker[i] = 1
        else: 
            truth_checker[i] = 0

    start_count = truth_checker.index(1)
    fresh_tank = 0


    for i in range(start_count, n): 
        fresh_tank += gas[i]
        fresh_tank -= cost[i]
        if fresh_tank > 0: 
            if truth_checker[i] == 0:
                truth_checker[i] = 1

    for i in range(0, start_count):
        fresh_tank += gas[i]
        fresh_tank -= cost[i]
        if fresh_tank > 0: 
            if truth_checker[i] == 0:
                truth_checker[i] = 1
    
    total_misses = truth_checker.count(0)
    first_miss = truth_checker.index(0)
    print(truth_checker, first_miss, start_count)
    if total_misses > 1: 
        return - 1 
    else: 
        if first_miss > start_count:
            return - 1
        return start_count


print(canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))

#got 9 out of 38 tests: 

#correct answer 
def canCompleteCircuit(gas, cost):
    n = len(gas)
    total_tank = 0
    current_tank = 0
    start_index = 0

    for i in range(n):
        total_tank += gas[i] - cost[i]
        current_tank += gas[i] - cost[i]
        
        if current_tank < 0:
            start_index = i + 1
            current_tank = 0

    return start_index if total_tank >= 0 else -1

# Test with the given example
print(canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))  # Output: 4
