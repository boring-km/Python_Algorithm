import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

n = int(input())
a = []

def getAVG(arr):
    size = len(arr)
    avg = 0
    cnt = 0
    for i in range(size):
        avg += arr[i]
    avg = avg/size
    for i in range(size):
        if avg < arr[i]:
            cnt += 1
    return cnt / size * 100
for i in range(n):
    t = []
    temp = input().split(" ")
    for j in range(1,int(temp[0])+1):
        t.append(int(temp[j]))
    a.append(t)
for i in range(n):
    print(format(round(getAVG(a[i]), 3),'.3f') + "%")