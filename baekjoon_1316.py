import sys
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline

test, count, length, i, j = int(input()),0,0,0,0
data, letter = "", []

for i in range(test):
    letter = [0]*26
    data = input()[:-1]
    length = len(data)
    # 문자를 코드화해서 숫자로 저장하면, 중복된 값이 와도 1로 같아짐
    letter[ord(data[0])-97] = 1
    flag = True
    for j in range(1, length):
        if data[j - 1] != data[j]:
            if letter[ord(data[j])-97] != 0:
                flag = False
                break
            else:
                letter[ord(data[j]) - 97] = 1
    if flag == True:
        count += 1
print(count)