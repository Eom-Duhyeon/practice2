from collections import deque
def find_friends(group, start):
    qu = deque()
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.popleft()
        print(p)
        for i in group[p]:
            if i not in done:
                qu.append(i)
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

find_friends(friend, 'Summer')
print()
find_friends(friend, 'Jerry')