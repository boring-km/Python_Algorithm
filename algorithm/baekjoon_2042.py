import sys
import math

input = sys.stdin.readline

# 세그먼트 트리
# 출처: https://www.acmicpc.net/blog/view/9
#
# init
def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
        return tree[node]
    else:
        mid = int((start + end) / 2)
        # 재귀
        tree[node] = init(a, tree, node * 2, start, mid) + init(a, tree, node * 2 + 1, mid + 1, end)
        return tree[node]

# 문제에서 원하는 합 구하기
def summ(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = int((start + end) / 2)
    # 재귀
    return summ(tree, node * 2, start, mid, left, right) + summ(tree, node * 2 + 1, mid + 1, end, left, right)


def update(tree, node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] = tree[node] + diff
    if start != end:
        mid = int((start + end) / 2)
        # 재귀
        update(tree, node * 2, start, mid, index, diff)
        update(tree, node * 2 + 1, mid + 1, end, index, diff)


# input
data = input().split()
N, M, K = int(data[0]), int(data[1]), int(data[2])
a = [0] * N
h = math.ceil(math.log2(N))
tree_size = 1 << (h + 1)
tree = [0] * tree_size
M += K
for i in range(N):
    a[i] = int(input())
init(a, tree, 1, 0, N - 1)
print(tree)
while M > 0:
    M -= 1
    d = input().split()
    t1, t2, t3 = int(d[0]), int(d[1]), int(d[2])
    if t1 == 1:
        t2 -= 1
        diff = t3 - a[t2]
        a[t2] = t3
        update(tree, 1, 0, N - 1, t2, diff)
    elif t1 == 2:
        print(summ(tree, 1, 0, N - 1, t2 - 1, t3 - 1))
