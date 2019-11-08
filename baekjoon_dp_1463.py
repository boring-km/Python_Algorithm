import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

n = int(input())
count = 0
arr = [0] * (n+1)
for i in range(2,n+1):
    arr[i] = arr[i-1]+1 # 1을 뺀다
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[int(i/2)]+1) # 2로 나누어 떨어지는 경우
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[int(i/3)]+1) # 3으로 나누어 떨어지는 경우
print(arr[n])