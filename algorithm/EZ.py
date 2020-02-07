import sys
input = sys.stdin.readline

n = int(input())
data = list(input())
res = 0
M = 1234567891
for i in range(n):
    res += (ord(data[i])-96) * (31**i)

print(res % M)