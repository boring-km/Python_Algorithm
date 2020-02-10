import sys
input = sys.stdin.readline

n, m = [int(i) for i in input().split()]

wf = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]
bf = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]
result = 987987987
a = []
for i in range(50):
    a.append("0"*50)

def blackFirst(y, x):
    global a
    cnt = 0
    for i in range(y, y+8):
        for j in range(x, x+8):
            if a[i][j] != bf[i - y][j - x]:
                cnt += 1
    return cnt


def whiteFirst(y, x):
    global a
    cnt = 0
    for i in range(y, y + 8):
        for j in range(x, x + 8):
            if a[i][j] != wf[i - y][j - x]:
                cnt += 1
    return cnt

for i in range(n):
    a[i] = input()[0:-1]

for i in range(n-7):
    for j in range(m-7):
        result = min(result, min(whiteFirst(i,j),blackFirst(i,j)))

print(result)
