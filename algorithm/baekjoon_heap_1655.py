import sys, heapq
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline
## 입력받을 갯수
number = int(input())
max_heap = []   # 최대 힙
min_heap = []   # 최소 힙

### 최대 힙에 작은 수들을
### 최소 힙에 큰 수들을 넣어서
### 최대 힙의 최댓값이 가운데 값이 나오도록 한 알고리즘
for i in range(number):
    input_num = int(input())    # 현재 입력 값
    # Left Right 힙(최대, 최소 힙)의 크기가 동일할 때
    if len(max_heap) == len(min_heap):
        # 처음 들어온 값이라면! -> 최초 값: mid
        # max_heap에 현재 입력 값 넣음
        if len(min_heap) == 0:
            heapq.heappush(max_heap, (-input_num, input_num))
        else:
            # 최소 힙에서 꺼내어서 현재 값보다 작으면,
            # 현재 값을 최소 힙에 넣고, 꺼낸 값을 최대 힙에 넣음
            # 최소 힙에서 꺼내어서 현재 값보다 크면,
            # 꺼낸 값을 최소 힙에 다시 넣고, 현재 값을 최대 힙에 넣음
            temp = heapq.heappop(min_heap)
            if temp < input_num:
                heapq.heappush(min_heap, input_num) # 오름차순 힙
                heapq.heappush(max_heap, (-temp, temp)) # 내림차순 힙
            else:
                heapq.heappush(min_heap, temp) # 오름차순 힙
                heapq.heappush(max_heap, (-input_num, input_num)) # 내림차순 힙
    elif len(max_heap) > len(min_heap): # 최대 힙의 크기가 더 크면?
        # 최대 힙에서 꺼내어서 현재 값보다 크면,
        # 최대 힙에 현재 값을 넣고, 꺼낸 값을 최소 힙에 넣는다.
        # 최대 힙에서 꺼내어서 현재 값보다 작으면,
        # 최대 힙에 꺼낸 값을 다시 넣고, 현재 값을 최소 힙에 넣는다.
        temp = heapq.heappop(max_heap)[1]
        if temp > input_num:
            heapq.heappush(max_heap, (-input_num, input_num))
            heapq.heappush(min_heap, temp)
        else:
            heapq.heappush(max_heap, (-temp, temp))
            heapq.heappush(min_heap, input_num)
    print("min_heap", min_heap)
    print("max_heap", max_heap)
    # 최대 힙에서 빼서 확인 후 다시 넣기 반복
    # top이 없어서 이짓 반복
    final = heapq.heappop(max_heap)[1]
    print(final)
    heapq.heappush(max_heap, (-final, final))
