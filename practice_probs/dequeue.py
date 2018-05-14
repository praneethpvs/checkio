class Queue:
    def __init__(self):
        self.list_in = list()

    def enqueue(self, val):
        self.list_in.append(val)
        print(self.list_in)

    def dequeue(self):
        if not self.q_empty():
            self.list_in.pop(0)
            print(self.list_in)
        else:
            print("Queue is empty.")

    def q_empty(self):
        if len(self.list_in) == 0:
            return True
        else:
            return False

    def q_size(self):
        size = len(self.list_in)
        return size


if __name__ == "__main__":
    q = Queue()
    q.enqueue(3)
    q.enqueue(4)
    print(q.q_size())
    q.enqueue(5)
    q.enqueue(6)
    if q.q_empty():
        print("Queue is empty")
    else:
        print("Queue is not empty")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    if q.q_empty():
        print("Queue is empty")
    else:
        print("Queue is not empty")
