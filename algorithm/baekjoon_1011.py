import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

n = int(input())

for i in range(n):
    data = input().split()
    a, b = int(data[0]), int(data[1])
    dist = b - a
    cur = a
    result = 0
    for j in range(1, dist):
        cur += j * 2
        result += 2
        if cur > b:
            cur -= j * 2
            result -= 2
            # 도착지점과 현재지점 간 거리
            # 이 거리를 잘 나눠서 쓰면 결과
            d = b - cur
            for k in range(j, -1, -1):
                d = d - k
                result += 1
                if d <= 0:
                    break
            break
        elif cur == b:
            break
    if dist == 1:
        result = 1
    print(result)