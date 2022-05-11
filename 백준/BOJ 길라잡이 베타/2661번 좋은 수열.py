# n = int(input())
# good = [1]
# #check 함수는 이상이 있으면 True 반환
#
# if n == 1:
#     print(1)
#     exit()
#
# def check(i):
#     k = (i+1)//2
#     for j in range(1, k+1):
#         start_1 = i - 2*j + 1
#         start_2 = i - j + 1
#         left = good[start_1:start_2]
#         right = good[start_2:]
#         if left == right:
#             return True
#     return False
#
# for i in range(1,n):
#     good.append(1)
#     while check(i):
#         good[i] += 1
#
# print(int(''.join(map(str, good))))

#
# #매우 중요 int 형 리스트는 당연히 join으로 못 합친다 ''.join(map(str,good)) 으로 합칠 수 있다.
#위의 알고리즘은 작동하지 않는데 만약 3까지 올려도 답을 찾지 못하면 4로 넘어갈 수 없기 때문이다 이전 수열을 고쳐야 한다.
#~~~~23 에서 3이 맞지 않으면 4로 올릴 수 없다.2를 고친 후 3이 있는 자리를 결정해야 한다.
# 또한 인덱스 접근법이 좋지 못하다. 그냥 음수 인덱스를 쓰면 더 계산하기 편하다.

def check(arr):
    l = len(arr)
    for idx in range(1, l//2 +1):
        if arr[-(idx*2):-idx] == arr[-idx:]:
            return False
    return True

def rec(arr):
    global  n
    if len(arr) == n:
        print(arr)
        exit()
    for i in '123':
        if check(arr + str(i)):
            rec(arr + str(i))
    return

n = int(input())
rec('1')














