number = int(input())

cnt = 0
for _ in range(number):
    word = input()
    char_dict = {}
    for char in word: #'happy'
        if char in char_dict:
            char_dict[char] +=1
            if late_char != char:
                cnt +=1
                break
        else : 
            char_dict[char] = 1
        late_char = char

print(number - cnt)
