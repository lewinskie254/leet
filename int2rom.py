def checkCorrectNumber(amount, output, number, letter): 
         if number == 0: 
              return (output, number)
         while number >= 0: 
            if number // amount: 
                output += letter
                number = number - amount
            else: 
                return (output, number)

def int2rom(number): 
    output = ""
    roman_map = {
        'M': 1000,
        'CM': 900, 
        'D': 500,
        'CD': 400, 
        'C': 100,
        'XC': 90, 
        'L': 50,
        'XL': 40, 
        'X': 10,
        'IX': 9, 
        'V': 5,
        'IV': 4, 
        'I': 1
    }
    for n in roman_map: 
        output, number = checkCorrectNumber(roman_map[n], output, number, n)

    return output 


#MMMDCCXLIX

print(int2rom(3749))
