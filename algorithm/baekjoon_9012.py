import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    data = list(input())[0:-1]
    cur = []
    for j in range(len(data)):
        if data[j] == '(':
            cur.append(0)
        else:
            if cur != [] and cur[-1] != -1:
                cur.pop()
            else:
                cur.append(-1)
    if cur == []:
        print("YES")
    else:
        print("NO")