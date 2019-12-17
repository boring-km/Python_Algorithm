import sys

input = sys.stdin.readline

test = []

n, need = input().split()
n, need = int(n), int(need)
a, b = [], []
for i in range(n):
    a.append(int(input()))
a.sort()

# 최대 최소 중간 결과
left, right, mid, res = 1, a[-1]-a[0], 0, 0
last = right
#while right-left >= 0:
#    mid = int((left+right)/2)
    # 간격이 mid이면서 가장 인접한 간격을 구하면서, need(공유기) 갯수를 맞출수 있도록


def solution(s):
    n, a = len(s), []
    for i in range(1, n):
        st, temp, temp_s, num = s, "", "", 1
        for j in range(n+1):
            if temp == st[:i]:
                num += 1
            elif j != 0 and temp != st[:i] and num != 0:
                if num == 1:
                    temp_s += temp
                else:
                    temp_s += str(num) + temp
                num = 1
            temp = st[:i]
            st = st[i:]
            if j == n:
                temp += '-'
        a.append(len(temp_s))
    a = sorted(a)
    if n == 1:
        return 1
    else:
        return a[0]