# First implementation
class Queue:
    def __init__(self):
        self.queue: list = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)

    def print_queue(self):
        print(self.queue)

# Second implementation
# from queue import Queue
# q = Queue(maxsize=5)
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# print("dequeued element is ", q.get())
# print(q)


q = Queue()
q.enqueue(1)
q.enqueue(2)
print("dequeued element is ", q.dequeue())
q.print_queue()