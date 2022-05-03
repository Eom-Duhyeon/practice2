n = int(input())
tree = []
term = 0
def gcd(a, b):
    if a%b ==0:
        return b
    else:
        return gcd(b, a%b)

for i in range(n):
    tree.append(int(input()))

tree.sort()

term = tree[1] - tree[0]
for i in range(1,n-1):
    inter = tree[i+1] - tree[i]
    term = gcd(max(term, inter),min(term, inter))

print(int((tree[-1]-tree[0])/term -(n-1)))