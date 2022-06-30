import itertools

fuel = 19
powers = [40, 30, 20, 10]
distances = [1000, 2000, 3000, 4000]

def get_times(p, m, dist):
    if dist > 0.5*p*(m**2):
        return (dist - 0.5*p*(m**2))/p*m + m
    else:
        return (dist/0.5*p)**0.5


def solution(fuel, powers, distances):
    n = len(distances)
    answer = [0]*n
    if fuel == n:
        m_boxes = [1] * n #연료의 분배를 나타내는 리스트
        for i in range(n):
            answer[i] = get_times(powers[i], m_boxes[i], distances[i])
        return(int(max(answer)))

    m_boxes = [1]*n
    m_boxes[n-1] = fuel-(n-1)
    min_coplete = 1e9
    for i in range(1, fuel-n):
        for possible in itertools.product(range(n-1), repeat = i):
            print(possible)




print(solution(fuel, powers, distances))

"""
import math

def get_times(p, m, dist):
    if dist > 0.5*p*(m**2):
        return (dist - 0.5*p*(m**2))/p*m + m
    else:
        return (dist/0.5*p)**0.5

def solution(fuel, powers, distances):
    """
    P(n,k)를 이용해 fuel을 분배하는 경우의 수를 나눠준다. 비효율적일 것으로 예상된다.
    for문을 이용해 나눠줄 수 있는 0부터 fuel-n 까지 나눠줄 수 있는 연료의 양을 i로 표현하고
    itertools의 product를 이용해 i만큼 나눠줄 때의 경우의 수를 구한다. 이렇게 2중for문에
    powers의 길이만큼 다시 for문을 돌려 2중 for문마다 우주선이 도착하는 시간들을 구한 후
    그 중 가장 큰 값을 min_complete와 비교하여 더 작은 것을 대입한다. 모든 경우의 수가 끝나고
    나온 min_complete를 result로 반환한다.
    """
    n = len(distances)
    answer = [0]*n
    if fuel == n:
        m_box = [1] * n
        for i in range(n):
            answer[i] = get_times(powers[i], m_box[i], distances[i])
        return(math.ceil(max(answer)))
"""