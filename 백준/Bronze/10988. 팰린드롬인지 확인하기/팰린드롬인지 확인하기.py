word = input()

i = 0
while i <len(word):
    # 펠렌드럼 체크
    if word[i] != word[-(i+1)] :
        answer=0
        break
    answer = 1
    i +=1 
    
print(answer)