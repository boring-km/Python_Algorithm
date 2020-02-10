import sys
input = sys.stdin.readline
import math

n = int(input())
a = [] # 마치 큐처럼 구현함
cur = 0
for i in range(n):
    temp = input()[0:-1]
    if temp[0:4] == "push":
        temp = temp.split()
        a.append(int(temp[1]))
    elif temp == "front":
        if len(a) - cur != 0:
            print(a[cur])
        else:
            print(-1)
    elif temp == "pop":
        if len(a) - cur == 0:
            print(-1)
        else:
            # pop 하기
            cur += 1
            print(a[cur-1])

    elif temp == "size":
        print(len(a) - cur)
    elif temp == "empty":
        if len(a) - cur == 0:
            print(1)
        else:
            print(0)
    elif temp == "back":
        if len(a) - cur == 0:
            print(-1)
        else:
            print(a[-1])