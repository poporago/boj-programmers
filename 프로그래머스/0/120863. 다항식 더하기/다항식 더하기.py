def solution(polynomial):
    poly = polynomial.split(' + ')   # '3x', '7'
    x_list = []
    num_list = []
    
    for element in poly:
        if element.isdigit():
            num_list.append(element)
        else :
            x_list.append(element)
    
    num1 = 0        
    for num_x in x_list: #'3x', 'x'
        if num_x == 'x':
            num1 += 1
        else : 
            num1 += int(num_x[:-1]) ## 주의점
        
    num2 = 0
    for num in num_list:
        num2 += int(num)
    
    if num1 ==1:
        num1 = ''
    
    if num1 != 0 and num2 != 0:
        answer = str(num1) + 'x' + ' ' + '+' + ' ' + str(num2)
    elif num1 ==0  :
        answer = str(num2)
    elif num2 ==0 :
        answer = str(num1) + 'x'
    else : 
        answer = 0 
    
    
    return answer