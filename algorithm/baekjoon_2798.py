import sys

input = sys.stdin.readline

data = input().split()
N, M = int(data[0]), int(data[1])
data = input().split()
res = M
for i in range(N):
    data[i] = int(data[i])

def combination(arr, r):
    # 1.
    arr = sorted(arr)
    # 2.
    def generate(chosen):
        global res
        if len(chosen) == r:
            # print(chosen)
            temp = M - sum(chosen)
            if res > temp and temp >= 0:
                res = temp # 최소 값
            return
    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(int(arr[nxt]))
            generate(chosen)
            chosen.pop()
    return generate([])

combination(data, 3)
print(M - res)
