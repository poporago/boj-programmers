def solution(sides):
    min_side = min(sides)
    max_side = max(sides)
    
    count = 0
    i = 0
    while True:
        i += 1
        max_value = max(i,max_side)
        second_value = min(i,max_side)
        
        if max_value < second_value + min_side : 
            count +=1
            continue
            
        elif max_value == i :
            break

    return count