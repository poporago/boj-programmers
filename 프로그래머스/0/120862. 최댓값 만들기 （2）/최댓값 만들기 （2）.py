def solution(numbers):
    # 완전 탐색 or 절댓값 순으로 정렬해서 곱
    plus = []
    minus = []
    for num in numbers:
        if num < 0 :
            minus.append(num)
        else : 
            plus.append(num)
    
    minus.sort()
    plus.sort()
    if len(minus)>=2 and len(plus)>=2:
        answer = minus[-1] * minus[-2] , plus[-1] * plus[-2]
        answer = max(answer) 
    elif len(minus)>=2:
        answer = minus[-1] * minus[-2]
    elif len(plus)>=2:
        answer = plus[-1] * plus[-2]
    else :
        answer = numbers[0] * numbers[1]
    
    return answer