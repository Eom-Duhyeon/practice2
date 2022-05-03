"""
N	stages	result
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
4	[4,4,4,4,4]	[4,1,2,3]

# """
# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 4
stages = [4, 4, 4, 4, 4]

def solution(N, stages):
    answer = []
    length = len(stages)
    count = [0]*(N+2)
    for stage in stages:
        if stage > N:
            count[N+1] += 1
        else:
            count[stage] += 1

    for i in range(N):
        if length ==0:
            failure = 0
        else:
            failure = count[i + 1] / length
            length -= count[i + 1]
        answer.append((failure, i+1))

    answer.sort(key=lambda x: (-x[0], x[1]))
    answer1 = []
    for i in answer:
        answer1.append(i[1])
    return answer1


print(solution(N,stages))