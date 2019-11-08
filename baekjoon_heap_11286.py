import sys, heapq

## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline
## 입력받을 갯수
number = int(input())
heap = []
for i in range(number):
    temp = int(input())
    if len(heap) == 0 and temp == 0:
            heapq.heappush(heap, (temp*temp, temp))
    elif temp != 0:
            heapq.heappush(heap, (temp*temp, temp))
    if temp == 0:
        print(heapq.heappop(heap)[1])