def isSubsequence(s, t):
    s_array = []
    t_array = []
    result_array = []
    for char in s: 
        s_array.append(char)
    
    for char in t: 
        t_array.append(char)
    
    letter_tracker = 0
    position_tracker = 0
    while position_tracker < len(t_array):
        if letter_tracker < len(s): 
            if t_array[position_tracker] == s[letter_tracker]:
                result_array.append(1)
                letter_tracker += 1
            else: 
                result_array.append(0)
            position_tracker += 1
        else: 
            break 
    return result_array.count(1) == len(s)
    

print(isSubsequence("abc", "ahbgdc"))