"""
"aabbaccc"	7
"ababcdcdababcdcd"	9
"abcabcdede"	8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd" 17


"""
s = "abcabcabcabcdededededede"


def solution(s):
    s = list(s)
    n = len(s)
    if n < 3:
        return n
    answer = n

    for i in range(1, n // 2 + 1):
        count = 0
        prev = []
        overlap = s[:i]
        for j in range(i, n, i):
            search = s[j:j + i]
            if overlap == search:
                count += 1
            else:
                if count == 0:
                    prev += overlap
                    overlap = search
                else:
                    prev += list(str(count + 1)) + overlap
                    count = 0
                    overlap = search

        if count == 0:
            prev += overlap
        elif count != 0:
            prev += list(str(count + 1)) + overlap

        answer = min(answer, len(prev))
    return answer


print(solution(s))