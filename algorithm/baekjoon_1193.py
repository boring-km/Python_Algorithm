import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

n = int(input())
cur = 1
count = 1

for i in range(2, 10000):
    cur += i
    count += 1
    if cur >= n:
        break

if count % 2 == 0:
    print(str(count+1 - (count-(n-(cur-(count-1))))) + '/' + str(count-(n-(cur-(count-1)))))
else:
    print(str(count-(n-(cur-(count-1)))) + '/' + str(count+1 - (count-(n-(cur-(count-1))))))