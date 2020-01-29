import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

a, b, v = input().split(" ")
a, b, v = int(a), int(b), int(v)

b = a - b # 하루 동안 오를 거리
c = v - a # 전체 길이에서 하루 오른거리 뺀 거
d = int(c / b) # 오.. 이렇게 하면 나누기 해도 되겠네, 오르는 일수

if c % b != 0: # 오를 거리랑 하루동안 오를 거리가 나누어 떨어지냐 안떨어지냐
    d += 2
else:
    d += 1
print(d)