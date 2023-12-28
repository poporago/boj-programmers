# 보트 탑승 인원이 2명이 아니라 제한이 없을때의 풀이

def solution(people, limit):
    people.sort()
    boat = 0
    start,end = 0, len(people) - 1

    while start <= end:
        weight = people[end]  # 가장 무거운 사람의 무게 기준 탑승 준비
        end -= 1  
        # limit제한에 걸리기전까지 가벼운 사람을 보트에 더함
        while start <= end and weight + people[start] <= limit:
            weight += people[start]
            start += 1
        boat += 1

    return boat

