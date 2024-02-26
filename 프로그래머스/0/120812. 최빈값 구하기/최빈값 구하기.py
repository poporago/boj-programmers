def solution(array):
    asnwer = 0
    
    count_dict = {}
    
    for element in array:
        if element in count_dict:
            count_dict[element] += 1
        else :
            count_dict[element] = 1
            
    max_count = max(count_dict.values())
    mode = [element for element,value in count_dict.items() if value == max_count]
    if len(mode) >=2:
        return -1
    else : 
        return mode[0]