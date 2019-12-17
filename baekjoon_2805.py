import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

n, need = input().split(" ")
n, need = int(n), int(need)

a = []
data = input().split(" ")
for i in range(n):
    a.append(int(data[i]))
a.sort() # [10, 15, 17, 20]
# 절단기를 설치할 높이의 범위 -> 구하려는 건 최댓값
left, right, res, size = 0, a[-1], 0, len(a)
while right - left >= 0:
    want = 0
    mid = int((left+right)/2)
    for i in range(size):
        temp = a[i] - mid
        if temp > 0:
            want += temp
    if want < need: # 자르고 보니 길이가 너무 짧으면
        right = mid - 1
    elif want >= need: # 자르고 보니 원하는 길이나 그 이상 나무가 나올때
        if res < mid:
            res = mid
        left = mid + 1
print(res)