def solution(spell, dic):
    num = len(spell)
    answer = 0
    for word in dic:
        cnt = 0
        for char in spell: 
            if char in word : 
                cnt +=1
        if cnt == num:
            return 1
    return 2
 