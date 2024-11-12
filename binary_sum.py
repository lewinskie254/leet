def binary_sum(number, additional): 
    number = number[::-1]
    additional = additional[::-1]
    
    max_len = max(len(number), len(additional))
    number = number.ljust(max_len, '0')
    additional = additional.ljust(max_len, '0')
    
    carry = 0
    output_string = ""
    
    for i in range(max_len):
        bit_sum = int(number[i]) + int(additional[i]) + carry
        if bit_sum == 2:
            output_string += '0'
            carry = 1
        elif bit_sum == 3:
            output_string += '1'
            carry = 1
        else:
            output_string += str(bit_sum)
            carry = 0

    if carry:
        output_string += '1'
    
    return output_string[::-1]

print(binary_sum("11001101", "10110"))
print(5**(-2), 1/25)
