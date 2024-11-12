def total_length(array, maxLength):
    strings = []
    current_string = ""

    for word in array:
        # If adding the next word exceeds maxLength, start a new string
        if len(current_string) + len(word) + (1 if current_string else 0) > maxLength:
            strings.append(current_string.strip())
            current_string = word
        else:
            if current_string:  # If current_string is not empty, add a space
                current_string += " "
            current_string += word

    # Add the last string if it's not empty
    if current_string:
        strings.append(current_string.strip())

    # Print lengths and the strings
    for string in strings:
        temp_string = string.split(" ")
        target = maxLength + len(string) 
        print(target)
        if len(string) < maxLength and target > maxLength: 
            temp_string.insert(1, " ")
            target += 1
            temp_string.insert(-2, " ")
            target += 1
        string = ""
        for element in temp_string: 
            string += element

    return strings

# Example usage
print(total_length(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))
