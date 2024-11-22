def minWindow(s, t): 

    if len(s) == len(t):
        if s == t: 
            return s 
        else: 
            return ""

    t_list = [char for char in t]
    dict_of_chars = {}

    for t in t_list: 
        dict_of_chars[t] = []

    for c in t_list: 
        for i in range(len(s)):
            if c == s[i]:
                dict_of_chars[c].append(i)

    min_vals = {}
    max_vals = {}
    for t in t_list: 
        if dict_of_chars[t] == []:
            return ""
        else: 
            min_vals[t] = min(dict_of_chars[t]) 
            max_vals[t] = max(dict_of_chars[t])
    
    min_length = max(min_vals.values()) - min(min_vals.values())
    max_length = max(max_vals.values()) - min(max_vals.values())

    if max_length < min_length: 
        return s[min(max_vals.values()):]
    else: 
        return s[min(min_vals.values()):max(min_vals.values())]


print(minWindow("ab", "a"))
#passed 73 out of 268 
