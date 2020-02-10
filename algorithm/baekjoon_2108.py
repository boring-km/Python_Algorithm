import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

# result 1 : 산술평균
print(round(sum(a) / n))

# result 2 : 중앙값
a.sort()
print(a[int(n/2)])

# result 4 : 범위
ran = a[-1] - a[0]

# result 3 : 최빈값
b = [0] * 10000
maxi = 0
for i in range(n):
    cur = 0
    if a[i] < 0:
        cur += 5000 + a[i]*(-1)
    else:
        cur += a[i]
    b[cur] += 1
    if maxi < b[cur]:
        maxi = b[cur]
c = []
for i in range(10000):
    if b[i] != 0:
        if b[i] == maxi:
            if i >= 5000:
                c.append((i-5000)*(-1))
            else:
                c.append(i)
c = list(set(c))
c.sort()
if len(c) == 1:
    print(c[0])
else:
    print(c[1])

# result 4 : 범위
print(ran)