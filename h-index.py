def hIndex(citations): 
    citations = sorted(citations)
    array_of_items = {}

    h_index = 0
    if len(citations) < 2: 
        if citations[0] < 1: 
            return 0 
        return 1 

    for element in citations: 
        array_of_items[element] = 0
    
    for element in citations: 
        for item in array_of_items: 
            if element >= item: 
                array_of_items[item] = array_of_items[item] + 1
    
    for item in array_of_items: 
        if item <= array_of_items[item]: 
            h_index = item 
    if h_index < 1: 
        h_index = max(array_of_items.values())
    
    return h_index

print(hIndex([11,15])) #score 58 / 82


def h_index(citations):
    
    citations.sort(reverse=True)
    sorted(citations, reverse=True)
    h_index = 0
    for i, citation in enumerate(citations):
        if citation >= i + 1:
            h_index = i + 1
        else:
            break
    
    return h_index
