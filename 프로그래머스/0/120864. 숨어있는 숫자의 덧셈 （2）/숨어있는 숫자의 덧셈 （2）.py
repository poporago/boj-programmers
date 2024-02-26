def solution(my_string):
    num = ""
    num_list = []
    
    for element in my_string:
        if element.isalpha():
            if num:  # 숫자가 존재하면 리스트에 추가
                num_list.append(num)
                num = ""  # 숫자를 추가한 후 초기화
        else:
            num += element
    if num:  # 마지막에 남은 숫자 처리
        num_list.append(num)
    
    answer = sum(map(int, num_list))
    
    return answer
