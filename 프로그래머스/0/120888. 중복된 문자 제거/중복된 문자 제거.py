def solution(my_string):
    count_dict = {}

    for string in my_string:
        count_dict[string] = 1  # 문자가 등장하면 1로 설정 (중복 제거)
    
    answer = ''.join(count_dict.keys())  # 딕셔너리 키들을 문자열로 결합
    return answer