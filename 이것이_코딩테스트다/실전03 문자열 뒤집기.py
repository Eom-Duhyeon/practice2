# n = list(map(int, input()))
# result = 0
#
# # 모두 0으로 바꾸는 게 더 적을 때 또는 모두 1으로 바꾸는 게 더 적을 때
# count_0 = 0
# count_1 = 0
# i = 0
#
# for i in range(len(n)-1):
#     if n[i] != n[i+1]:
#         if n[i + 1] == 1:
#             count_0 += 1
#         else:
#             count_1 += 1
#
# result = min(count_0, count_1)
# print(result)

data = list(input())
change_0, change_1 = 0, 0

if data[0] == "0":
    change_1 += 1
else:
    change_0 += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == "1":
            change_0 += 1
        else:
            change_1 += 1

print(min(change_0, change_1))
