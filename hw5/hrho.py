import pytest
import math
from hypothesis import given
import hypothesis.strategies as st

class Heap:
    def __init__(self, oglist=[]):
        ''' Initialize heap from a (possibly empty) list. '''
        self.heap = oglist

        # check if the heap is empty
        if self.length() != 0:
            heap_depth = math.floor(math.log2(self.length())) + 1

            # loop through n times given that n is the number of elements in the heap
            for i in range(len(self.heap)):
                root_idx = 0
                start_depth = 1

                while start_depth != heap_depth:
                    # check if the right child is in the range of the heap (there is a right child)
                    if self.right_child(root_idx) <= self.length()-1:
                        if self.heap[self.right_child(root_idx)] <= self.heap[root_idx] or self.heap[self.left_child(root_idx)] < self.heap[root_idx]:

                            if self.heap[self.left_child(root_idx)] < self.heap[self.right_child(root_idx)]:
                                self.swap_left_child(root_idx)
                                start_depth += 1
                                root_idx = self.left_child(root_idx)

                            else:
                                self.swap_right_child(root_idx)
                                start_depth += 1
                                root_idx = self.right_child(root_idx)
                        else:
                            print(self.heap)
                            break

                    # check if the left child is in the range of the heap (there only is a left child)
                    elif self.left_child(root_idx) <= self.length()-1:
                        if self.heap[self.left_child(root_idx)] < self.heap[root_idx]:
                            self.swap_left_child(root_idx)
                            start_depth += 1
                            root_idx = self.left_child(root_idx)

                        else:
                            break
                    # there are no children
                    else:
                        break
        else:
            self.heap = []

    def parent(self, idx):
        ''' Return the parent of the 'idx' node given. '''
        return (idx-1)//2

    def left_child(self, idx):
        ''' Return the left child of the 'idx' node given. '''
        return (idx*2)+1

    def right_child(self, idx):
        ''' Return the right child of the 'idx' node given. '''
        return (idx*2)+2

    def swap_parent(self, idx):
        ''' Change value of idx with the parent of idx '''
        temp = self.heap[self.parent(idx)]
        self.heap[self.parent(idx)] = self.heap[idx]
        self.heap[idx] = temp

    def swap_left_child(self, idx):
        ''' Change value of the heap[idx] with the left child of the idx '''
        temp = self.heap[self.left_child(idx)]
        self.heap[self.left_child(idx)] = self.heap[idx]
        self.heap[idx] = temp

    def swap_right_child(self, idx):
        ''' Change value of the heap[idx] with the right child of the idx '''
        temp = self.heap[self.right_child(idx)]
        self.heap[self.right_child(idx)] = self.heap[idx]
        self.heap[idx] = temp

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
            val_idx = self.length()-1

            while heap_depth != 1:
                # swap inserted and parent value if inserted < parent
                if self.heap[val_idx] < self.heap[self.parent(val_idx)]:
                    self.swap_parent(val_idx)

                    # update the heap_deapth and val_idx
                    heap_depth -= 1
                    val_idx = self.parent(val_idx)

                # exit while if inserted !< parent
                else:
                    break


    def delete_min(self):
        ''' Remove the min (root) from heap. '''
        root_idx = 0
        start_depth = 1
        heap_depth = math.floor(math.log2(self.length())) + 1

        # replace the last element with the root and delete the last
        self.heap[root_idx] = self.heap[self.length()-1]
        del self.heap[self.length()-1]

        # check if the heap is empty
        if self.length() != 0:
            while start_depth != heap_depth:
                # check if the right child is in the range of the heap (there is a right child)
                if self.right_child(root_idx) <= self.length()-1:
                    if self.heap[self.right_child(root_idx)] <= self.heap[root_idx] or self.heap[self.left_child(root_idx)] < self.heap[root_idx]:

                        if self.heap[self.left_child(root_idx)] < self.heap[self.right_child(root_idx)]:
                            self.swap_left_child(root_idx)
                            start_depth += 1
                            root_idx = self.left_child(root_idx)

                        else:
                            self.swap_right_child(root_idx)
                            start_depth += 1
                            root_idx = self.right_child(root_idx)
                    else:
                        print(self.heap)
                        break

                # check if the left child is in the range of the heap (there only is a left child)
                elif self.left_child(root_idx) <= self.length()-1:
                    if self.heap[self.left_child(root_idx)] < self.heap[root_idx]:
                        self.swap_left_child(root_idx)
                        start_depth += 1
                        root_idx = self.left_child(root_idx)

                    else:
                        break
                else:
                    break
        else:
            return None

    def find_min(self):
        ''' Return min value in the heap. '''
        if self.length() == 0:
            return None
        return self.heap[0]


    def sorted_list(self):
        ''' Return a sorted list of all heap elements. '''
        new_heap = []

        for i in range(self.length()):
            new_heap.append(self.find_min())
            self.delete_min()

        return new_heap


@given(st.lists(st.integers()))
def test_heap_a(l):
    ''' Test sequentially inserting -> sequentially deleting '''
    h = Heap()
    for i in range(len(l)):
        if len(l) == 0:
            break
        h.insert(l[i])
    print(h.heap)

    prev_min = h.find_min()
    for j in range(len(l)):
        if prev_min == None:
            break

        h.delete_min()
        next_min = h.find_min()

        if next_min == None:
            break
        assert min(h.heap) == h.find_min()
        prev_min = next_min

    assert h.length() == 0


@given(st.lists(st.integers()))
def test_heap_b(l):
    ''' Test initializing given l -> sequentially deleting '''
    h = Heap(l)
    for i in range(len(l)):
        if len(l) == 0:
            break
        h.delete_min()
        # include the extra assert
    assert h.length() == 0


@given(st.lists(st.integers()))
def test_heap_c(l):
    ''' Test initializing given l -> returning a sorted l '''
    h = Heap(l)
    cpy = l
    cpy.sort()
    print(cpy)
    print(h.sorted_list())
    assert cpy == h.sorted_list()
    ## call h.sorted_list()
    ## iterate and if the elements are in ascending order


if __name__ == "__main__":
    test_heap_a()
    test_heap_b()
    test_heap_c()
