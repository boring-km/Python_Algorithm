import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

data = int(input())
ar = [0] * 4001
ar2 = [0] * 4001

b = []
max = 0
for i in range(data):
    d = int(input())
    b.append(d)
    if d < 0:
        ar[-d] += 1
        if max < ar[-d]:
            max = ar[-d]
    else:
        ar2[d] += 1
        if max < ar2[d]:
            max = ar2[d]
s = 0
res = []
for i in range(4001):
    if ar[i] != 0:
        s -= i * ar[i]
        print(s)
    elif ar2[i] != 0:
        s += i * ar2[i]
    if max == ar[i]:
        res.append(-i)
    elif max == ar2[i]:
        res.append(i)
b.sort()
res.sort()

avg = int(s / data)
#print("평균: ", avg, s / data, s)
if avg < 0:
    if s / data <= avg - 0.5:
        avg -= 1
else:
    if s / data >= avg + 0.5:
        avg += 1
mid = b[int(data/2)]
print(avg) # 산술평균
print(mid) # 중앙값
# 최빈값
if len(res) == 1:
    print(res[0])
else:
    print(res[1])
print(b[-1] - b[0]) # 범위
