def solution(babbling):
    answer = 0
    check_list = ['aya', 'ye', 'woo', 'ma']

    for chunk in babbling:
        i = 0
        while i < len(chunk):
            found = False
            for word in check_list:
                if chunk[i:].startswith(word):
                    i += len(word)
                    found = True
                    break
            if not found:
                break
        if i == len(chunk):
            answer += 1

    return answer
