import sys

input = sys.stdin.readline
n = int(input())
data = input().split()

dp = [0] * 1001
res = 0
for i in range(n):
    data[i] = int(data[i])
    here = 0
    for j in range(i): # 여기가 핵심일지도 i 번 반복
        if data[i] > data[j]: # 현재 값이 이전 값보다 큰 게 나온것이 있다면
            here = max(here, dp[j]) # here는 현재 최대, dp[j] 는 기억되어있는 그 자리의 최대
    dp[i] = here + 1 # 최댓값 + 1
    res = max(res, dp[i]) # 최댓값 갱신 (값이 입력될때마다 갱신해야하니깐)
print(res)