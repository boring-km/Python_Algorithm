import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

n, m = input().split(" ")
n, m = int(n), int(m)
d = input().split(" ")
a = []

for i in d:
    a.append(int(i))
a.sort()
# 최소: a[0], 최대: a[-1]
left = 0
right = n - 1
mid = int((left+right)/2)
#for i in range(a[right],0,-1):