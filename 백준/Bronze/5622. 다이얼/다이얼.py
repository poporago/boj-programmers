alphabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
words = input()

answer = 0
for alpha in alphabet_list: # 'ABC'
    for word in words:
        if word in alpha:
            answer += alphabet_list.index(alpha) +3
            
print(answer)    