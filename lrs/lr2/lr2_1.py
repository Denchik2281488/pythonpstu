class Queue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.data[0]

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.data.pop(0)
    def show(self):
        for i in self.data:
            print(i)
    
a = Queue()
sw = "wdawd"
sw1 = "wdawd1"
sw2 = "wdawd2"
sw3 = "wdawd3"

a.enqueue(sw)
a.enqueue(sw1)
a.enqueue(sw2)
a.enqueue(sw3)
a.show()
print(a.peek())
a.dequeue()
a.show()
