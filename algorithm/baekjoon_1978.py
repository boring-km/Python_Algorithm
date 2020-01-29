import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

N = int(input())
data = input().split()
for i in range(N):
    data[i] = int(data[i])
MAX = 1001
a = [0,0]
for i in range(2, MAX): # 미리 리스트 채워넣기
    a.append(i)
for i in range(2, MAX):
    if a[i] == 0:       # 0이면 소수가 아니다
        continue
    for j in range(i*2, MAX, i): # i배수 체크 (MAX까지) (소수가 아닌 수 = i배수)
        a[j] = 0
a = set(a)
res = 0
for i in range(N):
    before = len(a)
    a.add(data[i])
    after = len(a)
    if before == after:
        res += 1
print(res)

#for i in range(m, n+1):
#    if a[i] != 0:
#        print(a[i])