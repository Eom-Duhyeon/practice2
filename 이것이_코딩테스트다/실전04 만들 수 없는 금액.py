# """
# 입력 예시1
# 5
# 3 2 1 1 9
# 출력 예시1
# 8
# """
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
#
# """
# 만약 가장 작은 화폐 단위가 1보다 크면 당연히 1을 만들 수 없다. 1을 반환
# 또, data의 숫자들은 확인할 필요가 없다. 이 때 data의 i번째 원소들의 합+1을 만들 수 있는지 확인한다. 예를 들어 화폐 단위가 2라면 3을 만들 수 있는지
# 확인한다.예를 들어 3, 4, 9가 주어졌다면  7은 확인할 필요가 없고(어차피 3,4로 만들 수 있으니까) 8이 만들어질 수 있는지 확인하면 되는 것이다.
# 1이 포함되지 않았다면 당연히 1을 반환하면 된다.
# 1이 포함된다면 i번째 원소+1에 대해 일일히 검사할 필요가 없다 그냥 1을 더하면 되니까.
# 그 1을 이미 써버린 i번째 원소까지의 합에 1을 더해 검사해본다
# """
# target = 1
# for i in data:
#     if target < i:
#         break
#     target += i
# print(target)

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for i in coins:
    if target < i:
        print(target)
        break
    target += i