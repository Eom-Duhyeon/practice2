n = int(input())
answer = []

for i in range(n):
    answer.append(int(input()))

def find(li, target):
    answer = 0
    def csum(target):
        if target < 0:
            return
        if target == 0:
            nonlocal answer
            answer += 1
        for i in li:
            csum(target - i)
    csum(target)
    return answer

num=[1,2,3]

for i in answer:
    print(find(num,i))

