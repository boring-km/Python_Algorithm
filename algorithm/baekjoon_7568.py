import sys
input = sys.stdin.readline

n = int(input())
a = [0] * n
b = [0] * n
x, y = 0, 0

for k in range(n):
    a[k], b[k] = [int(i) for i in input().split()]

for i in range(n):
    tx, ty = a[i], b[i]
    rank = n
    for j in range(n):
        if tx < a[j] and ty < b[j]:
            rank -= 1
    print(n+1-rank, end=' ')
