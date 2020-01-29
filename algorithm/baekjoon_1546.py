import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

n = int(input())
pre = ''
score = []
for i in range(n):
    data = input()
    tmp_score = []
    sc = 0
    for j in range(len(data)):
        if pre == 'O':
            if data[j] == 'O':
                sc += 1
                tmp_score.append(sc)
                pre = 'O'
            elif data[j] == 'X':
                tmp_score.append(0)
                pre = 'X'
                sc = 0
        else:
            if data[j] == 'X':
                tmp_score.append(0)
                pre = 'X'
                sc = 0
            elif data[j] == 'O':
                tmp_score.append(1)
                pre = 'O'
                sc = 1
    score.append(tmp_score)
for i in range(n):
    print(sum(score[i]))
