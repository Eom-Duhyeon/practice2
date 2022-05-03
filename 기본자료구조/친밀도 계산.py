from collections import deque
def find_familiar(group, start):
    qu = deque()
    done = set()

    qu.append((start,0))
    done.add(start)

    while qu:
        (p, d) = qu.popleft()
        print(p,d) #print(p,d)면 elements 가 출력, print((p,d)) 면 튜플이 출력 즉 ('John', 1)
        for i in group[p]:
            if i not in done:
                qu.append((i, d+1)) #튜플이라 append(i, d+1) 이 아니라 append((i, d+1))
                done.add(i)



friend = {
    'Summer' : ['John', 'Justin', 'Mike'],
    'John' : ['Summer', 'Justin'],
    'Justin' : ['John', 'Summer', 'Mike', 'May'],
    'Mike' : ['Summer', 'Justin'],
    'May' : ['Justin', 'Kim'],
    'Kim' : ['May'],
    'Tom' : ['Jerry'],
    'Jerry' : ['Tom']
}

find_familiar(friend, 'Summer')
print()
find_familiar(friend, 'Jerry')