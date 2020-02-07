import sys

input = sys.stdin.readline

n = int(input())

t = [0]
p = [0]
d = [0] * (n+2)
result = 0

for i in range(n):
    a, b = map(int, input().split()) # 정수로 입력받음
    t.append(a)
    p.append(b)

for i in range(1, n+2):
    for j in range(1, i):
        d[i] = max(d[i], d[j]) # 앞에 있는 값이 더 크면 뒤에다 복사
        if j + t[j] == i: # 지나간 시간 + 걸리는 시간 == 현재 시간 ?
            d[i] = max(d[i], d[j] + p[j]) # 기록된 이익과 이번의 이익을 합한 계산
                                            # 굳이 max가 있어야하나 싶을 정도
    result = max(result, d[i])

print(result)