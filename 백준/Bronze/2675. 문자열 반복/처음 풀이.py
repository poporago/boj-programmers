num = int(input())

for i in range(num):
    repeat, word = input().split()
    repeat = int(repeat)
    for k in word:
        for j in range(repeat):
            print(k, end='')
    print()