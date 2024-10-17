
def product(array): 
    output_array = []

    temp_array = array

    for i, num in enumerate(array): 
        temp_array.remove(num)
        temp_item = 1
        for item in temp_array: 
            temp_item *= item 
        output_array.append(temp_item)
        temp_array.insert(i, num)
        temp_item = 1 
    return output_array

#18 out of 20 


def product(array):
    n = len(array)
    if n == 0:
        return []

    # Initialize two arrays for left and right products
    left_products = [1] * n
    right_products = [1] * n
    output_array = [1] * n

    # Fill left_products where left_products[i] contains the product of all elements to the left of index i
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * array[i - 1]

    # Fill right_products where right_products[i] contains the product of all elements to the right of index i
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * array[i + 1]

    # Fill the output array with the product of left and right products
    for i in range(n):
        output_array[i] = left_products[i] * right_products[i]

    return output_array
