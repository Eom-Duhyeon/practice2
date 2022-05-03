def solution(answers):
    answer = []
    ans1 = [1, 2, 3, 4, 5]
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == ans1[i % len(ans1)]:
            count[0] += 1
        if answers[i] == ans2[i % len(ans2)]:
            count[1] += 1
        if answers[i] == ans3[i % len(ans3)]:
            count[2] += 1

    maxi = max(count)
    for i in range(len(count)):
        if count[i] == maxi:
            answer.append(i + 1)

    return answer