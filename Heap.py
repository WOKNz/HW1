#  Heap
#  public functions: insert,check,pull
#  private functions: __swap, __up, __down


class Heap:
    def default_key(x):  # default key:, key used to sort on different fields
        return x

    def __init__(self, objects, a="min", key=default_key):  # Building heap
        self.heap = []
        self.type = a
        for object in objects:
            self.heap.append(object)  # adding object to list (heap)
            self.__up(len(self.heap)-1, key=key)  # reordering list (heap)

    def insert(self, object, key=default_key):  # adding object at the end
        self.heap.append(object)
        self.__up(len(self.heap)-1, key=key)  # Fixing heap

    def check(self):
        if self.heap[0]:
            return self.heap[0]
        else:
            return False

    def pull(self, key=default_key):  # Pulling the root
        if len(self.heap) > 1:  # Healty tree
            self.__swap(0, len(self.heap)-1)
            root = self.heap.pop()
            self.__down(0, key=key)  # Fixing heap after pull
        elif len(self.heap) == 1:  # One object tree
            root = self.heap.pop()
        else:
            root = False
        return root

    def __swap(self, a, b):  # Simple swap
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def __up(self, i, key=default_key):  # Comparing to parent and rising up on tree
        parent = ((i-1)//2)
        if i <= 0:
            return
        if self.type == "min":  # case for min heap
            if key(self.heap[i]) < key(self.heap[parent]):
                self.__swap(i, parent)
                self.__up(parent, key=key)  # recursive call
        elif self.type == "max":  # case for max heap
            if key(self.heap[i]) > key(self.heap[parent]):
                self.__swap(i, parent)
                self.__up(parent, key=key)  # recursive call

    def __down(self, i, key=default_key):  # Moving down new root
        left = (i+1)*2 - 1
        right = (i+1)*2
        compared = i
        if self.type == "min":  # case for min heap (default case)
            if len(self.heap) > left and key(self.heap[compared]) > key(self.heap[left]):
                compared = left
            if len(self.heap) > right and key(self.heap[compared]) > key(self.heap[right]):
                compared = right
            if compared != i:
                self.__swap(i, compared)
                self.__down(compared, key=key)  # recursive call
        elif self.type == "max":  # case for max heap
            if len(self.heap) > left and key(self.heap[compared]) < key(self.heap[left]):
                compared = left
            if len(self.heap) > right and key(self.heap[compared]) < key(self.heap[right]):
                compared = right
            if compared != i:
                self.__swap(i, compared)
                self.__down(compared, key=key)  # recursive call

    def sort(self, key=default_key):  # Creating new list of sorted objects
        k = []
        heap_copy = self.heap.copy()
        while len(self.heap) > 0:  # Adding object by pulling from heap
            k.append(self.pull(key=key))
        self.heap = heap_copy.copy()
        return k


def hs(listofobj, field: int, order: int):  # Unified call for sort
    if field == 0 and order == 0:  # from small to large, on x
        a = Heap(listofobj, "min", key=lambda point: point.x)
        return a.sort(key=lambda point: point.x)
    elif field == 0 and order == 1:  # from small to large, on y
        a = Heap(listofobj, "min", key=lambda point: point.y)
        return a.sort(key=lambda point: point.y)
    elif field == 1 and order == 0:  # from large to small, on x
        a = Heap(listofobj, "max", key=lambda point: point.x)
        return a.sort(key=lambda point: point.x)
    elif field == 1 and order == 1:  # from large to small, on y
        a = Heap(listofobj, "max", key=lambda point: point.y)
        return a.sort(key=lambda point: point.y)
    else:  # Illegal input case
        print("One of the input parameters is illegal")
        return
