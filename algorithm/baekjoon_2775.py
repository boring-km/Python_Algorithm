import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

count = int(input())

def recur(a, b):
    s = 0
    if a == 0:
        return b
    else:
        for j in range(1,b+1):
            s += recur(a-1, j)
    return s

for i in range(count):
    K = int(input())
    N = int(input())
    print(recur(K, N))
