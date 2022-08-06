class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        

    def pop(self):


    def put(self, value):



pila = MyQueue()

t=int(raw_input())

for line in xrange(t):
    values = map(int,raw_input().split())

    if values[0] == 1:
        pila.put[values[1]]
    elif values[0] == 2:
        pila.pop()
    else:
        print pila.peek()
