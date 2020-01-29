import sys

input = sys.stdin.readline

data = input().split()
N, M = int(data[0]), int(data[1])
a = []
for i in range(1,N+1):
    a.append(i)

# 순열
def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    # 2.
    def generate(chosen, used):

        if len(chosen) == r:
            # 출력만 다르게
            for i in range(len(chosen)):
                print(str(chosen[i]) + " ", end="")
            print("")
            return
    	# 3. 순열을 중복없이
        for i in range(len(arr)):
            if not used[i] and (i == 0 or arr[i-1] != arr[i] or used[i-1]):
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used) # 재귀
                used[i] = 0
                chosen.pop()
    generate([], used) # 시작

permutation(a, M)
