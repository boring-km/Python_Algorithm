import sys, heapq

## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline
## 입력받을 갯수
number = int(input())
datas, heap = [], []
for i in range(number):
    temp = int(input())
    datas.append(temp)
    ## heap에 추가
    # 기본 heap은 최소 힙이라서 (-num, num)으로 값을 주어서 우선순위를 반대로
    heapq.heappush(heap, (-temp, temp))
    if temp == 0:
        print(heapq.heappop(heap)[1])