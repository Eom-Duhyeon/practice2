n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

left = sorted(array[:], reverse=True)

right=[]
answer=[]
for i in range(len(array)):
    while True:
        if not right:
            right.append(left.pop())
            answer.append("+")
        if right[-1] > array[i]:
            print("NO")
            exit()
        elif right[-1] == array[i]:
            right.pop()
            answer.append("-")
            break
        else:
            right.append((left.pop()))
            answer.append("+")

for i in answer:
    print(i)
