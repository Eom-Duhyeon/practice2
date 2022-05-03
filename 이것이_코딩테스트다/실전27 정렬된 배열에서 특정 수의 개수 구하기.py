"""
7 2
1 1 2 2 2 2 3
"""

a, x = map(int, input().split())

data = list(map(int, input().split()))
n = len(data)


start = 0
end = n-1
while start <= end:
    s_mid = (start+end)//2

    if data[s_mid] == x and (data[s_mid-1] != x or s_mid == 0):
        break

    if data[s_mid] >= x:
        end = s_mid-1
    else:
        start = s_mid+1

if start > end:
    print(-1)
    exit()

start = 0
end = n-1

while start <= end:
    e_mid = (start + end) // 2

    if data[e_mid] == x and (data[e_mid + 1] != x or e_mid == n-1):
        break

    if data[e_mid] > x:
        end = e_mid - 1
    else:
        start = e_mid + 1

print(e_mid - s_mid + 1)
