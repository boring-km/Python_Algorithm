data = input().split("-")
temp_str = ""
flag = False

for i in range(len(data)):
    if flag == False:
        temp_str += data[i] + "-("
        flag = True
    else:
        temp_str += data[i] + ")-"
        flag = False
if temp_str[len(temp_str)-1:] == "(":
    temp_str = temp_str[:len(temp_str)-2]
elif temp_str[len(temp_str)-1:] == "-":
    temp_str = temp_str[:len(temp_str)-1]
print(temp_str)
print(eval(temp_str))