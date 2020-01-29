import sys

input = sys.stdin.readline
test = []
n, need = input().split()
n, need = int(n), int(need)
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
left = 1
right = a[-1] - a[0]    # 9 - 1 = 8
res, d = 0, 0
# 두 공유기 사이의 인접할 거리를 탐색해가자 (1부터)
while right - left >= 0:
    mid = int((left+right)/2)   # 4
    start = a[0]
    count = 1
    # 간격 d 를 기준으로 공유기 설치 (start를 제외한 모든 점에서 start까지의 거리 d)
    for i in range(1,n):
        d = a[i] - start
        if mid <= d:
            count += 1
            start = a[i]
    if count >= need:
        res = mid
        left = mid + 1
    else:
        right = mid - 1
print(res)