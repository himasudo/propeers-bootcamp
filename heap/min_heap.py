class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)

        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent] <= self.heap[i]:
                break

            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]

            i = parent

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]

        self.heap[0] = self.heap.pop()

        i = 0

        while(True):
            left = 2*i + 1
            right = 2*i + 2
            smallest = i

            if (left < len(self.heap)) and (self.heap[left] < self.heap[smallest]):
                smallest = left

            if (right < len(self.heap)) and (self.heap[right] < self.heap[smallest]):
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]

            i = smallest

        return root

h = MinHeap()

h.push(5)
h.push(3)
h.push(8)
h.push(1)
h.push(6)
h.push(2)

print("heap:", h.heap)

print("pop:", h.pop())
print("heap:", h.heap)

print("pop:", h.pop())
print("heap:", h.heap)

print("pop:", h.pop())
print("heap:", h.heap)