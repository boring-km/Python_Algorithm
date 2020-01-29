import sys
import math

input = sys.stdin.readline
# 세그먼트 트리
# 출처: https://jason9319.tistory.com/37
# https://2youngjae.tistory.com/103

def init(a, tree, node, start, end, mode):
    if start == end:
        tree[node] = a[start]
        return tree[node]
    mid = (start+end) >> 1
    if mode == 2: # 최대
        tree[node] = max(init(a, tree, node << 1, start, mid, mode),
                         init(a, tree, (node << 1) + 1, mid + 1, end, mode))
    else: # 최소
        tree[node] = min(init(a, tree, node << 1, start, mid, mode),
                         init(a, tree, (node << 1) + 1, mid + 1, end, mode))
    return tree[node]

# mintree, maxtree, 1, 0, 9, 2, 4
def getMinMax(tree_min, tree_max, node, start, end, left, right):
    global mm, MM
    if left > end or right < start:
        return
    if left <= start and end <= right:
        if tree_min[node] < mm:
            mm = tree_min[node]
        if tree_max[node] > MM:
            MM = tree_max[node]
        return
    # 이도 저도 아닌경우
    mid = (start+end) >> 1
    getMinMax(tree_min, tree_max, node << 1, start, mid, left, right)
    getMinMax(tree_min, tree_max, (node << 1) + 1, mid + 1, end, left, right)

first = input().split()
N, M = int(first[0]), int(first[1])
h = int(math.ceil(math.log2(N)))
a = [0] * (N)
maxtree = [0] * (1 << (h+1))
mintree = [0] * (1 << (h+1))

for i in range(N):
    a[i] = int(input())

mm, MM = 0, 0
mini, maxi = 1, 2
init(a, maxtree, 1, 0, N - 1, maxi)
init(a, mintree, 1, 0, N - 1, mini)

for i in range(M):
    mm = 987987654321
    MM = 0
    temp = input().split()
    left, right = int(temp[0]), int(temp[1])

    getMinMax(mintree, maxtree, 1, 0, N-1, left-1, right-1)
    print(mm, MM)