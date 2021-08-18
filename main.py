# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/6_Queue/6_queue_exercise.md

# Logic: https://www.youtube.com/watch?v=kL9KgvZs4e0

# enqueue 1
# -----loop ------
# front = 1 --print--
# enqueue "1"+"0" => 10
# enqueue "1"+"1" => 11
# dequeue => removing 1
# front = 10 --print--
# enqueue "10"+"0" => 100
# enqueue "10"+"1" => 101
# dequeue => removing 10
# front = 11 --print--
# enqueue "11"+"0" => 110
# enqueue "11"+"1" => 111
# dequeue => removing 11


from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def front(self):
        return self.buffer[0]

    def enqueue(self, order):
        self.buffer.append(order)

    def dequeue(self):
        self.buffer.popleft()

    def is_empty(self):
        if len(self.buffer) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.buffer)


def generate_binary(N):
    q = Queue()
    q.enqueue(1)

    for i in range(N):
        front = q.front()
        print(front)
        q.enqueue(str(front) + "0")
        q.enqueue(str(front) + "1")
        q.dequeue()


if __name__ == '__main__':
    generate_binary(10)
