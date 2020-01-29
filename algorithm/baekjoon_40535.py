# 숨바꼭질
# https://www.acmicpc.net/board/view/40535
class Queue(list):
    # enqueue == > insert 관용적인 이름
    add = list.append

    # poll == > delete, dequeue

    def poll(self):
        return self.pop(0)

    def is_empty(self):
        if not self:
            return True
        else:
            return False


input_text = input().split(" ")
start = int(input_text[0])
end = int(input_text[1])
count = [0] * 100001
check = [False] * 100001
count[start] = 1
check[start] = True

dx = [1, -1, 0]

q = Queue()
q.add(start)

while not q.is_empty():
    cur = q.poll()
    dx[2] = cur
    for i in range(3):
        nx = cur + dx[i]
        if 100000 >= nx >= 0:
            if check[nx] == False and count[nx] == 0:
                q.add(nx)
                count[nx] = count[cur] + 1

print(count[end] - 1)
