"""
4
5 1 7 9

"""


n = int(input())
house = list(map(int, input().split()))
house.sort()
print(house[(n-1)//2])