import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

n, m = input().split()
n, m = int(n), int(m)

parent = list(range(n+1))
def find(x):
    # 부모를 찾으면
    if x == parent[x]:
        return x
    else:
        # 부모가 아니면 찾을 때까지 재귀
        y = find(parent[x])
        parent[x] = y
        return y

def union(x, y):
    # 합집합
    x = find(x) # x의 부모
    y = find(y) # y의 부모
    if x != y: # x의 부모와 y의 부모가 같지 않으면?
        parent[x] = y # x의 부모를 y로
        # parent[y] = x # 반대로 해도 맞았습니다 나옴

for i in range(m):
    check, a, b = input().split()
    check, a, b = int(check), int(a), int(b)
    if check == 0:
        union(a, b)
        print("parent: ", parent, " a: ", a, " b: ", b)
    elif check == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
