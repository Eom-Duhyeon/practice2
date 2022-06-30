import math

logs = ["morgan string_compare", "felix string_compare", "morgan reverse", "rohan sort", "andy reverse", "morgan sqrt"]

def solution(logs):
    dic = dict()
    men = set()
    answer = []
    for log in logs:
        log = log.split()
        men.add(log[0])
        if log[1] in dic:
            dic[log[1]] += 1
        else:
            dic[log[1]] = 1
    n = len(men)
    for i in dic:
        if dic[i] >= math.ceil(n//2):
            answer.append(i)
    answer.sort()
    return answer

print(solution(logs))