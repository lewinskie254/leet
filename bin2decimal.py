def dec_to_binary(bs): 
    bs = int(bs)
    binary_output = ""
    while bs > 0:
        rem = bs%2
        binary_output = str(rem) + binary_output
        bs = bs // 2 
    
    return binary_output 

print(dec_to_binary(3507))