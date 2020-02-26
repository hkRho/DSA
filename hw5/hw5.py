import pytest
import math
# from hypothesis import given
# import hypothesis.strategies as st

class Heap:
    def __init__(self, oglist=[]):
        ''' Initialize heap from a (possibly empty) list. '''
        self.heap = []

    def parent(self, idx):
        return (idx-1)//2

    def length(self):
        ''' Return length of the heap. '''
        return len(self.heap)

    def insert(self, value):
        ''' Insert value into the heap. '''
        if self.length() == 0:
            self.heap.append(value)

        elif self.length() != 0:
            self.heap.append(value)
            heap_depth = math.floor(math.log2(self.length())) + 1

            while heap_depth != 0:
                val_idx = self.length()-1
                # print("heap_depth: ", heap_depth)
                # print("val_idx: ", val_idx)
                # print("parent_val_idx: ", self.parent(val_idx))

                # compare with parent value
                if self.heap[val_idx] < self.heap[self.parent(val_idx)]:
                    # swap new value and parent value
                    temp = self.heap[self.parent(val_idx)]
                    self.heap[self.parent(val_idx)] = self.heap[val_idx]
                    self.heap[val_idx] = temp
                    heap_depth -= 1
                else:
                    break

    def delete_min(self):
        ''' Remove the min (root) from heap. '''
        self.heap[0] = self.heap[self.length()-1]
        del self.heap[self.length()-1]

        heap_depth = math.floor(math.log2(self.length())) + 1
        while heap_depth != 0:
            # compare between left and right child
            # push the smaller one higher
            if self.heap[left_child] < self.heap[0]:
                #change
            elif self.heap[right_child] < self.heap[0]:

    def find_min(self):
        ''' Return min value in the heap. '''
        return self.heap[0]

    def sorted_list(self):
        ''' Return a sorted list of all heap elements. '''

min_heap = Heap()
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(1)
min_heap.insert(6)
min_heap.insert(7)
print(min_heap.heap)
# print(math.floor(math.log2(5)))
