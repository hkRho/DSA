import pytest
import math
from hypothesis import given
import hypothesis.strategies as st

class Heap:
    def __init__(self, oglist=[]):
        ''' Initialize heap from a (possibly empty) list. '''
        self.heap = oglist.copy()


        if self.length() != 0:
            heap_depth = math.floor(math.log2(self.length())) + 1

            for i in range(len(self.heap)):
                root_idx = 0
                start_depth = 1

                while start_depth != heap_depth:
                    # check if there is a left_child and if left_child of parent < parent
                    # print("root_idx: ", root_idx)
                    if self.left_child(root_idx) <= self.length()-1 and self.heap[self.left_child(root_idx)] < self.heap[root_idx]:
                        temp = self.heap[self.left_child(root_idx)]
                        self.heap[self.left_child(root_idx)] = self.heap[root_idx]
                        self.heap[root_idx] = temp

                        start_depth += 1
                        root_idx = self.left_child(root_idx)
                        print(self.heap)

                    # check if there is a right_child and if right_child of parent < parent
                    elif self.right_child(root_idx) <= self.length()-1 and self.heap[self.right_child(root_idx)] < self.heap[root_idx]:
                            temp = self.heap[self.right_child(root_idx)]
                            self.heap[self.right_child(root_idx)] = self.heap[root_idx]
                            self.heap[root_idx] = temp

                            start_depth += 1
                            root_idx = self.right_child(root_idx)
                            print(self.heap)
                    else:
                        print("-----")
                        break
        else:
            self.heap = []

    # def swap(self, idx):
    #     temp = self.heap[self.parent(idx)]
    #     self.heap[self.parent(idx)] = self.heap[idx]
    #     self.heap[idx] = temp
    #
    #     return

    def parent(self, idx):
        ''' Return the parent of the 'idx' node given. '''
        return (idx-1)//2

    def left_child(self, idx):
        ''' Return the left child of the 'idx' node given. '''
        return (idx*2)+1

    def right_child(self, idx):
        ''' Return the right child of the 'idx' node given. '''
        return (idx*2)+2

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
                    temp = self.heap[self.parent(val_idx)]
                    self.heap[self.parent(val_idx)] = self.heap[val_idx]
                    self.heap[val_idx] = temp

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

        if self.length() != 0:
            while start_depth != heap_depth:
                # print("root: ", self.length()-1)
                # print("chid: ", self.right_child(root_idx))
                # check if there is a left_child and if left_child of parent < parent

                # if self.heap[self.left_child(root_idx)] < self.heap[self.right_child(root_idx)]:
                # check if there is a right_child and if right_child of parent < parent
                if self.right_child(root_idx) <= self.length()-1 and self.heap[self.right_child(root_idx)] < self.heap[root_idx]:
                        print("child: ", self.heap[self.right_child(root_idx)])
                        print("root: ",  self.heap[root_idx])
                        temp = self.heap[self.right_child(root_idx)]
                        self.heap[self.right_child(root_idx)] = self.heap[root_idx]
                        self.heap[root_idx] = temp

                        start_depth += 1
                        root_idx = self.right_child(root_idx)
                        print(self.heap)

                elif self.left_child(root_idx) < self.length()-1 and self.heap[self.left_child(root_idx)] < self.heap[root_idx]:
                    temp = self.heap[self.left_child(root_idx)]
                    self.heap[self.left_child(root_idx)] = self.heap[root_idx]
                    self.heap[root_idx] = temp

                    start_depth += 1
                    root_idx = self.left_child(root_idx)
                    print(self.heap)

                else:
                    print(self.heap)
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
        temp_heap = self.heap.copy()

        for i in range(self.length()):
            new_heap.append(self.find_min())
            self.delete_min()
        self.heap = temp_heap
        return new_heap


@given(st.lists(st.integers()))
def test_heap_a(l):
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
        prev_min = next_min

    assert h.length() == 0

@given(st.lists(st.integers()))
def test_heap_b(l):
    h = Heap(l)
    for i in range(len(l)):
        if len(l) == 0:
            break
        h.delete_min()
    assert h.length() == 0


@given(st.lists(st.integers()))
def test_heap_c(l):
    h = Heap(l)
    cpy = l
    cpy.sort()
    # if h.length() == 0:
    #     h.heap.append(0)
    #     cpy.append(0)
    print(cpy)
    print(h.sorted_list())
    assert cpy == h.sorted_list()
    # assert [0] == [0]


if __name__ == "__main__":
    test_heap_c()

# min_heap = Heap([3,2,1])
# min_heap.insert(5)
# min_heap.insert(3)
# min_heap.insert(6)
# min_heap.insert(8)
# min_heap.insert(1)
# print(min_heap.heap)
# print("------------")
# min_heap.delete_min()
# min_heap.sorted_list()
# print(min_heap.sorted_list())
# print(min_heap.length())
# print(math.floor(math.log2(5)))
