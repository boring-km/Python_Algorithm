import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

n, m = input().split()
n, m = int(n), int(m)
sets = []
for i in range(n+1):
    sets.append({i})
#print(sets)
for i in range(m):
    check, a, b = input().split()
    check, a, b = int(check), int(a), int(b)
    if check == 0:
        sets[a], sets[b] = sets[a].union(sets[b]), sets[a].union(sets[b])
    elif check == 1:
        # 교집합 없음, 포함 X
        if sets[a].intersection({b}) == set():
            print("NO")
        else:
            print("YES")
