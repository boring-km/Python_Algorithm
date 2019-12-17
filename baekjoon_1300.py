import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

left, right = 1, k
mid, res, j = 0, 0, 0

while right - left >= 0:
    j = 0
    mid = int((left+right)/2) # 4
    for i in range(1, n+1):
        # j += int(min(mid / i, n))
        if mid / i < n:
            j += int(mid / i)
        else: # mid를 i로 나눠도 n보다 더 커지면 곤란 (탐색범위를 넘지 않으려고)
            j += n # 다음 줄로 넘어가기
    if j < k:
        left = mid + 1
    else:
        res = mid
        right = mid - 1
print(int(res))
