def isPalindrome(s): 
    s = s.lower()
    first_copy = []
    
    for letter in s: 
        if letter.isalnum(): 
            first_copy.append(letter)

    second_copy = []
    for i in range(len(first_copy)-1, -1, -1):
        second_copy.append(first_copy[i])

    return first_copy == second_copy 

print(isPalindrome("A man, a plan, a canal: Panama"))