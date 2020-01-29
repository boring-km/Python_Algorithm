import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

n = int(input())
for i in range(n):
    data = input().split()
    H, W, N = int(data[0]), int(data[1]), int(data[2])
    mok, nam = 0, 0

    if N != H:
        if N/H == int(N/H):
            mok = int(N/H)
        else:
            mok = int(N/H) + 1
    else:
        mok = 1

    if N == H:
        nam = 100 * N
    elif N % H == 0:
        nam = H * 100
    else:
        nam = (N % H) * 100
    print(mok + nam)