num1, num2 = input().split()

num1 = ''.join(list(reversed(num1)))
num2 = ''.join(list(reversed(num2)))

if int(num1) > int(num2):
    print(int(num1))
else :
    print(int(num2))