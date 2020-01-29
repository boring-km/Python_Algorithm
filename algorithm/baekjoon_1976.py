import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

## 도시의 수
n = int(input())
## 여행 계획에 속한 도시들의 수
m = int(input())
datas = []
for i in range(n):
    datas.append(input().split())
plan = input().split()
datas.append([])
for i in range(n):
    datas[i][i] = '1'
for k in range(0, n):
    for i in range(0, n):
        for j in range(0, n):
            if datas[i][k] == '1' and datas[k][j] == '1':
                datas[i][j] = '1'

v1 = int(plan[0]) - 1
ans = 1
for i in range(m):
    p_d = int(plan[i])-1
    if not int(datas[v1][p_d]) and not int(datas[p_d][v1]):
        ans = 0
    v1 = p_d
if(ans):
    print("YES")
else:
    print("NO")