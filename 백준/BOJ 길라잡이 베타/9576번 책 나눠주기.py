testcases = int(input())
for testcase in range(testcases):
    books = []
    n, m = map(int, input().split())
    for i in range(m):
        a, b = map(int, input().split())
        books.append((a, b))


    count = 0
    books.sort(key=lambda x: (x[1], x[0]))
    possible = [False]+[True]*(n)
    for i in range(m):
        for j in range(books[i][0], books[i][1]+1):
            if possible[j]:
                possible[j] = False
                count += 1
                break

    print(count)

