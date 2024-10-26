import math


def roman2int(s): 
    s = s.lower()
    amount = 0 
    for i, element in enumerate(s):
        if element == "m":
            if i > 0: 
                if s[i - 1] != "c":
                   amount += 1000 
                else: 
                    amount += 900 
            else: 
                amount += 1000 
        elif element == "d": 
            if i > 0: 
                if s[i - 1] != "c":
                   amount += 500 
                else: 
                    amount += 400 
            else: 
                amount += 500 
            amount += 500
        elif element == "c":
            if i < len(s)-1 and (s[i+1] != "m" or s[i+1] != "d"):
                amount += 100
            else: 
                amount += 100
        elif element == "l":
            amount += 50 
        elif element == "x":
            amount += 10
        elif element == "v" and s[i-1] != "i": 
            amount += 5
        elif element == "v" and s[i-1] == "i": 
            amount += 4
        elif element == "i": 
                amount += 1
            
    
    return amount

print(roman2int("MCMXCIV"))


#correct version 
def roman2int(s):
    s = s.lower()
    amount = 0
    roman_map = {
        'm': 1000,
        'd': 500,
        'c': 100,
        'l': 50,
        'x': 10,
        'v': 5,
        'i': 1
    }

    for item in roman_map:
        print(item, roman_map[item])
    
    for i in range(len(s)):
        if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
            amount -= roman_map[s[i]]
        else:
            amount += roman_map[s[i]]
    
    return amount

print(roman2int("MCMXCIV"))