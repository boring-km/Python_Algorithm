import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

#n = int(input())
for n in range(3,5000):
    shadow = n
    current, current2 = 0, 0
    answer, answer2 = 0, 0
    if n >= 5:
        answer += int(n / 5)
        current = n % 5
        answer2 += int(n / 3)
        current2 = n % 3
    elif n == 3:
        answer = 1
    elif n == 4 or n < 3:
        answer = -1

    if current == 0:
        print("cureent: ", current, " , input: ", str(n), ", answer: ", str(answer))
    else:
        answer += int(current / 3)
        answer2 += int(current2 / 5)
        tcurrent = current % 3
        tcurrent2 = current2 % 5
        arr = []
        flag = False
        print("current: ", current, end=' , ')
        if tcurrent == 0:
            arr.append(answer)
            flag = True
        else:
            for i in range(1, 5):
                shadow -= 3
                if shadow % 5 == 0 and shadow > 0:
                    answer = int(shadow / 5) + i
                    arr.append(answer)
                    flag = True
                    break
        if tcurrent2 == 0:
            arr.append(answer2)
        elif tcurrent2 != 0 and flag == False:
            arr.append(-1)
        shadow = n
        #print(arr)
        print("input: ", str(n), ", answer: ", min(arr))