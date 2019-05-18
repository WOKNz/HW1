#  Heap
#  public functions: insert,check,pull
#  private functions: __swap, __up, __down

class Heap:
    def default_key(x):  # default key: use the value as-is
        return x

    def __init__(self, objects, a="min", key=default_key):
        self.heap = []
        self.type = a
        for object in objects:
            self.heap.append(object)
            self.__up(len(self.heap)-1, key=key)

    def insert(self, object, key=default_key):
        self.heap.append(object)
        self.__up(len(self.heap)-1, key=key)

    def check(self):
        if self.heap[0]:
            return self.heap[0]
        else:
            return False

    def pull(self, key=default_key):
        if len(self.heap) > 1:
            self.__swap(0, len(self.heap)-1)
            root = self.heap.pop()
            self.__down(0, key=key)
        elif len(self.heap) == 1:
            root = self.heap.pop()
        else:
            root = False
        return root

    def __swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def __up(self, i, key=default_key):
        parent = ((i-1)//2)
        if i <= 0:
            return
        if self.type == "min":
            if key(self.heap[i]) < key(self.heap[parent]):
                self.__swap(i, parent)
                self.__up(parent, key=key)
        elif self.type == "max":
            if key(self.heap[i]) > key(self.heap[parent]):
                self.__swap(i, parent)
                self.__up(parent, key=key)

    def __down(self, i, key=default_key):
        left = (i+1)*2 - 1
        right = (i+1)*2
        compared = i
        if self.type == "min":
            if len(self.heap) > left and key(self.heap[compared]) > key(self.heap[left]):
                compared = left
            if len(self.heap) > right and key(self.heap[compared]) > key(self.heap[right]):
                compared = right
            if compared != i:
                self.__swap(i, compared)
                self.__down(compared, key=key)
        elif self.type == "max":
            if len(self.heap) > left and key(self.heap[compared]) < key(self.heap[left]):
                compared = left
            if len(self.heap) > right and key(self.heap[compared]) < key(self.heap[right]):
                compared = right
            if compared != i:
                self.__swap(i, compared)
                self.__down(compared, key=key)

    def sort(self, key=default_key):
        k = []
        heap_copy = self.heap.copy()
        while len(self.heap) > 0:
            k.append(self.pull(key=key))
        self.heap = heap_copy.copy()
        return k







