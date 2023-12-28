def solution(people, limit):
    boat = 0
    people.sort()
    start = 0
    end = len(people) - 1 

    while start <= end:        
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        boat += 1 

    return boat
