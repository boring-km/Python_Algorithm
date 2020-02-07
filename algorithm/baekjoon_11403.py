import sys

input = sys.stdin.readline

n = int(input())
a = []
visited = [0] * n


def dfs(i):
    global visited, a, n
    for j in range(n): # i에서 모든 j번째 탐색
        if a[i][j] == 1 and visited[j] == 0: # 그곳이 1이고 방문은 하지 않았다면
            visited[j] += 1 # 그곳을 방문하고
            dfs(j) # 그 자리에서 탐색

for i in range(n):
    temp = [ int(j) for j in input().split()]
    a.append(temp)

for i in range(n):
    visited = [0] * n
    dfs(i) # i번째 n번 dfs
    for j in range(n):
        if visited[j] > 0: # 새롭게 가능해진 간선의 값을 1로 갱신
            a[i][j] = 1

for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print("")