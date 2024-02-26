def solution(s):
    s = s.split() #input 문자열을 공백 기준으로 나눠 리스트로 저장합니다.
    temp = []  #더할 요소를 리스트로 받습니다.
    for num in s : 
        temp.append(int(num)) if num != 'Z' else temp.pop()
    return sum(temp)