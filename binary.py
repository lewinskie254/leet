def binary(s):
    s = str(s)
    s_array = []
    
    for element in s:
        s_array.append(element)

    pointer = len(s_array) - 1
    multiplier = 1
    total_value = 0
    while pointer > -1:
        total_value += int(s_array[pointer]) * multiplier
        multiplier *= 2
        pointer -= 1
    
    return total_value


def binary_decimal(s):
    s = str(s)
    s_array = []
    checking_index = 0
    
    for element in s:
        s_array.append(element)
    
    if "." in s_array: 
        checking_index = s_array.index(".")
        integer_array = s_array[:checking_index]
        decimal_array = s_array[checking_index + 1:]
    else: 
        integer_array = s_array
        decimal_array = []
    
    if decimal_array: 
        decimal_string = "".join(decimal_array)  # Start after the decimal point
    else: 
        decimal_string = ""

    integer_string = "".join(integer_array)
   
    if decimal_string:
        decimal_value = decimal_count(decimal_string)
    else: 
        decimal_value = 0
    integer_value = binary(integer_string)

    if decimal_value:
        return integer_value + decimal_value 
    else: 
        return integer_value


def decimal_count(s):
    s = str(s)
    decimal_array = []

    for element in s:
        decimal_array.append(element)

    divisor = 2  # Start with 2^1 for the first digit after the decimal
    total_value = 0
    multiplier = 1 / divisor  # Start with 1/2 for the first digit after the decimal

    for element in decimal_array:
        if element == '.':
            continue  # Skip the decimal point if it exists
        total_value += int(element) * multiplier
        divisor *=2 
        multiplier = 1 / divisor

    return total_value


# Testing the functions
print(binary_decimal("110110110011"))  # Example binary string