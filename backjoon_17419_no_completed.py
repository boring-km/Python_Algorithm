import sys, heapq
## 입력을 빠르게 하기 위한 함수
input = sys.stdin.readline
'''
data = '123'
data += '4'
print(data)
'''

num = input()
data = input()
numbers = 0
def reverse(data):
    temp = ""
    for s in data:
        if s == '1':
            temp += '0'
        elif s == '0':
            temp += '1'
    return temp
while True:
    temp = reverse(data)
    temp2 = temp
    print(temp)

    while True:
        if temp[-1] == '0':
            if len(temp2) != len(temp):
                temp = temp[:-1] + '1' + '0' * (len(temp2) - len(temp))
            else:
                temp = temp[:-1] + '1'
            break
        else:
            temp = temp[:-1]
    temp2 = ""
    print(temp)
    for i in range(int(num)):
        if data[i] == temp[i]:
            temp2 += "1"
        else:
            temp2 += "0"
    print(temp2)
    # 1의 보수
    temp3 = reverse(temp2)
    print(temp3)

    count = "0"
    temp4 = "0"
    cur = -1
    for k in range(int(num) - 1):

        if data[cur] == temp3[cur]:
            if count == "0":
                if data[cur] == "1":
                    count = "1"
                else:
                    count = "0"
                temp4 += "0"
            elif count == "1":
                if data[cur] == "1":
                    count = "1"
                else:
                    count = "0"
                temp4 += "1"
        elif data[cur] != temp3[cur]:
            if count == "1":
                temp4 += "0"
            elif count == "0":
                temp4 += "1"
                count = "0"
        cur -= 1
    temp4 = ''.join(reversed(temp4))
    print(temp4)
    temp5 = temp4
    while True:
        if temp[-1] == '0':
            if len(temp4) != len(temp5):
                temp5 = temp5[:-1] + '1' + '0' * (len(temp4) - len(temp5))
            else:
                temp5 = temp5[:-1] + '1'
            break
        else:
            temp5 = temp5[:-1]
    print(temp5)
    numbers += 1
    data = temp5
    if temp5 == "00000":
        print(temp5)
        print("end", numbers)
        break
    ##temp[:-1]

# print(temp)

# K = K-(K&((~K)+1))
# K = K-temp2

