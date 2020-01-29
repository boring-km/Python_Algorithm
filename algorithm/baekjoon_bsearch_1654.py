import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

n, need = input().split(" ")
n, need = int(n), int(need)
a = []

for i in range(n):
    a.append(int(input()))
a.sort() # [457, 539, 743, 802]
# 랜선의 길이가 될 수 있는 범위 -> 구하려는 건 최댓값
left, right, res, size = 1, a[-1], 0, len(a) # 1, 802, 0, 4
mid = int((left+right)/2) # 401
while right - left >= 0:
    mid = int((left + right) / 2)  # 2
    count = 0
    for i in range(size):
        count += int(a[i] / mid) # 몇 개나 들어가는지(만들어지는지?_
    if count < need:
        right = mid - 1 # 갯수 안나오면 크기 줄임
    elif count >= need: # 갯수가 같거나 그 이상
        if res < mid: # 랜선 갯수도 맞고 이전 값보다 구하려는 값이 더 큰 상황
            res = mid # 최댓값 갱신
        left = mid + 1 # 어쨌든 더 크니까 탐색범위도 큰 범위로
print(res)