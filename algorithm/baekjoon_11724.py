import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
MAX = 1001
N, M = [int(i) for i in input().split()]

graph = []
visited = [0] * MAX

## 전형적인 DFS 라고 하는데 왜이리 어렵지
def dfs(node):
    visited[node] = 1 # 이 노드를 방문함
    for i in range(len(graph[node])): # 그 노드에 연결된 모든 선을 찾아서
        next = graph[node][i] # 어차피 graph에 들어있는 노드는 모두 연결된 녀석들만 존재한다.
        if visited[next] == 0: # 방문하지 않은 노드가 있다면?
            dfs(next) # 탐색함

# 빈 리스트 생성
for i in range(MAX):
    graph.append([])

for i in range(M):
    a, b = [int(j) for j in input().split()]
    # 방향이 없는 그래프
    # 값이 있을 때만 들어가는 리스트
    graph[a].append(b)
    graph[b].append(a)
count = 0
for i in range(1, N+1):
    if visited[i] == 0: # 방문하지 않은 노드라면
        dfs(i)
        count += 1
print(count)