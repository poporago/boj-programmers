num = int(input())

for i in range(1,2*num):
    if i < num:
        print(' '*(num-i)+ '*'*(2*i-1))
    elif i == num:
        print('*'* (2*i-1))
    else :
        print(' '*(i-num) + '*'*((2*num-1) -2*(i-num)))

#2

for i in range(1, num):
    print(' '*(num-i) + '*'*(2*i-1))
for i in range(num, 0, -1):
    print(' '*(num-i) + '*'*(2*i-1))