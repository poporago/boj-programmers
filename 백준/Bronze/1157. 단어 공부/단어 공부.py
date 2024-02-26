word = input().upper()
char_count = {}  # 문자를 키로, 빈도수를 값으로 하는 딕셔너리

for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

max_count = max(char_count.values())
most_frequent = [char for char, count in char_count.items() if count == max_count]

if len(most_frequent) > 1:
    print("?")
else:
    print(most_frequent[0])
