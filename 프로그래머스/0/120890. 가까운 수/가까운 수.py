def solution(array,n):
    array.sort()
    diff_dict = {}
    
    for element in array:
        diff_dict[element] = abs(element-n)
    minimum = min(diff_dict.values())
    
    answer = [key for key,value in  diff_dict.items() if value == minimum]
    
    return answer[0]