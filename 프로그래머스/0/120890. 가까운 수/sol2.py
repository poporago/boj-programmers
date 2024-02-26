def solution(array, n):
    array.sort(key=lambda x: (abs(x - n), x))   # 정렬 키의 첫번째 조건과 두번째 조건
    return array[0]