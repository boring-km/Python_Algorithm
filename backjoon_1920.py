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
flag = False
left = 0
right = N-1
mid = int((left+right)/2)

for i in range(M):
    while right-left>=0:
        if A[mid] == B[i]:
            print(1)
            flag = True
            break
        if B[i] < A[mid]:
            right = mid-1
        elif B[i] > A[mid]:
            left = mid+1
        mid = int((left + right) / 2)
    if not flag:
        print(0)
    flag = False
    left = 0
    right = N-1
    mid = int((left+right)/2)
