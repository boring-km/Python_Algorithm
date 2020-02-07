import sys

input = sys.stdin.readline

# https://wootool.tistory.com/90
n = int(input())
mod = 1000000000
dp = []
for i in range(101):
    dp.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
sum = 0
for i in range(10):
    dp[1][i] = 1        # 갯수를 위한 초기화
for i in range(2,n+1):
    for j in range(10): # 0에서 9까지
        if j == 0:
            dp[i][0] = dp[i-1][1] % mod # 0일 때는 1이랑만 계단
        elif j == 9:
            dp[i][9] = dp[i-1][8] % mod # 9일 때는 8이랑만 계단
        else: # 나머지는 -1, +1 모두 가능
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod
for i in range(1, 10): # 전부 합산
    sum = int((sum + dp[n][i]) % mod)
print(sum % mod)