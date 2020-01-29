import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

N = int(input())
temp_A = input().split(" ")
A = []
for i in range(N):
    A.append(int(temp_A[i]))
M = int(input())
temp_B = input().split(" ")
B = []
for i in range(M):
    B.append(int(temp_B[i]))

A.sort()
left = 0
right = N-1
res = [0]*M
mid = int((left+right)/2)

for i in range(M):
    while right-left>=0:
        if A[mid] == B[i]:
            res[i] += 1
            temp_mid = mid
            while True:
                if mid > 0:
                    mid -= 1
                else:
                    break
                if A[mid] == B[i]:
                    res[i] += 1
                else:
                    break
            mid = temp_mid
            while True:
                if mid < N-1:
                    mid += 1
                else:
                    break
                if A[mid] == B[i]:
                    res[i] += 1
                else:
                    break
            mid = temp_mid
            break
        elif B[i] < A[mid]:
            right = mid-1
        elif B[i] > A[mid]:
            left = mid+1
        mid = int((left + right) / 2)
    left = 0
    right = N-1
    mid = int((left+right)/2)
for i in range(M):
    print(res[i], end=' ')
