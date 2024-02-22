palindrome = input()

if palindrome[::1] == palindrome[::-1]: # 문자열 슬라이싱
    print(1)
else:
    print(0)