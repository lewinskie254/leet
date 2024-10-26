def reverser(string): 
    string = string.strip()
    array = string.split(" ")
    array.reverse()
    output_string = ""

    for element in array: 
        if element[:1].isalnum(): 
            output_string += element + " "
    
    return output_string

print(reverser("a good   example"))