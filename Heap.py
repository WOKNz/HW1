#  Heap
#  public functions: insert,check,pull
# private functions: __swap, __up, __down

class Heap:
    def __init__(self, objects, a="min"):
        self.heap = []
        self.type = a
        for object in objects:
            self.heap.append(object)
            self.__up(len(self.heap)-1)

    def insert(self, object):
        self.heap.append(object)
        self.__up(len(self.heap)-1)

    def check(self):
        if self.heap[0]:
            return self.heap[0]
        else:
            return False

    def pull(self):
        if len(self.heap) > 1:
            self.__swap(0, len(self.heap)-1)
            root = self.heap.pop()
            self.__down(0)
        elif len(self.heap) == 1:
            root = self.heap.pop()
        else:
            root = False
        return root

    def __swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def __up(self, i):
        parent = ((i-1)//2)
        if i <= 0:
            return
        if self.type == "min":
            if self.heap[i] < self.heap[parent]:
                self.__swap(i, parent)
                self.__up(parent)
        elif self.type == "max":
            if self.heap[i] > self.heap[parent]:
                self.__swap(i, parent)
                self.__up(parent)

    def __down(self, i):
        left = (i+1)*2 - 1
        right = (i+1)*2
        compared = i
        if self.type == "min":
            if len(self.heap) > left and self.heap[compared] > self.heap[left]:
                compared = left
            if len(self.heap) > right and self.heap[compared] > self.heap[right]:
                compared = right
            if compared != i:
                self.__swap(i, compared)
                self.__down(compared)
        elif self.type == "max":
            if len(self.heap) > left and self.heap[compared] < self.heap[left]:
                compared = left
            if len(self.heap) > right and self.heap[compared] < self.heap[right]:
                compared = right
            if compared != i:
                self.__swap(i, compared)
                self.__down(compared)








