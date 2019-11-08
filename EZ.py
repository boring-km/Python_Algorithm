import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

data = input()
a = [-1]*26
for i in range(len(data)-1):
    if a[int(ord(data[i]))-97] == -1:
        a[int(ord(data[i]))-97] = i

for i in range(26):
    print(a[i], end=' ')