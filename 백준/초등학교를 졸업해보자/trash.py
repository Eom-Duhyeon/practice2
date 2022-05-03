import sys
input=sys.stdin.readline #으로 input처럼 간편하게
arr = [int(x) for x in sys.stdin.readline().split()]
stk1 = list(stdin.readline().strip()) #문자열 입력
list.sort(key=len) # list의 정렬을 문자 길이순으로.
#리스트를 출력할 때 리스트 변수명 앞에 * 쓰면 리스트 요소만 출력 ex) print(*arr)
여러 줄 입력
arr = [[0 for j in range(cols)] for i in range(rows)] # cols개 짜리 배열 rows개 생성