def elements(N):
    element_index: list =[]

    for i in range(1,len(N)):
        if N[i] != N[i-1] + 1:
            element_index.append(i)
            break


    if element_index:
        return element_index
    else:
        return "Не найдено"
    
    
print(elements([1, 2, 3, 4]))