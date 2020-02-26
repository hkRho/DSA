# -----------------------------------------------------------
# Data Structures and Algorithms
# Homework 2
#
# @Author: HK Rho
# -----------------------------------------------------------
import pytest
import timeit
import random
import matplotlib.pyplot as plt
# coding: utf-8

class Node:
    def __init__(self,val=None,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self):
        ''' Constructor for an empty list '''
        self.head = None
        self.tail = None
        self.length = 0
        self.store_dll = []

    def length(self):
        ''' Returns the number of nodes in the list '''
        return self.length


    def push(self, val):
        ''' Adds a node with value equal to val to the front of the list '''
        # make a new node with the given value
        new_node = Node(val)

        # case when the node is the first node - there are no other nodes existing
        if self.head == None:
            new_node.prev = None
            new_node.next = None
            self.head = new_node
            self.tail = new_node
            self.store_dll.insert(0,val)

        # case when the node is not the first node - there are preexisting nodes
        if self.head != None:
            new_node.prev = None
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.store_dll.insert(0,val)

        # update the length
        self.length += 1


    def insert_after(self, prev_node, val):
        ''' Adds a node with value equal to val in the list after prev_node '''
        # print(prev_node.val)
        # make a new node with the given value
        new_node = Node(val)

        # case when inserting before head
        if prev_node == None:
            self.push(val)
            return

        # case when inserting after tail
        if prev_node == self.tail:
            prev_node.next = new_node
            new_node.prev = prev_node
            self.tail = new_node
            return

        # case when inserting between two nodes
        else:
            new_node.next = prev_node.next
            new_node.prev = prev_node
            prev_node.next = new_node
            new_node.next.prev = new_node

        # update the length
        self.length += 1
        return


    def delete(self, node):
        ''' Removes node from the list '''

        # case when deleting node that is the head
        if node.prev == None:
            self.head = node.next
            self.head.prev = None
            self.length -= 1

        # case when deleting node that is the tail
        if node.next == None:
            self.tail = node.prev
            self.tail.next = None
            self.length -= 1

        # case when deleting a node in between other nodes
        if node.prev != None and node.next != None:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1


    def index(self, i):
        ''' Returns the node at position i (i<n) '''
        current = self.head
        idx = 0

        while i < self.length:
            if i == idx:
                return current.val
            else:
                idx += 1
                current = current.next

    def print_dll(self):
        print(self.store_dll)

    def multiply_all_pairs(self):
        ''' Multiplies all unique pairs of nodes values for nodes i, j (i != j)
        and returns the sum '''
        list = []
        sum = 0
        for i in range(self.length):
            list.append(self.index(i))
        print(list)

        for i in range(self.length):
            for j in range(self.length):
                if i != j:
                    sum += list[i] * list[j]
                    # print(list[i] * list[j])
        print(type(sum/2))
        print(sum/2)
        return (sum/2)


# TESTS
def test_push():
    dll.push(1)
    assert dll.head.val == 1, "push method not working"

    dll.push(2)
    assert dll.head.val == 2, "push method not working"

    dll.push(3)
    assert dll.head.val == 3, "push method not working"

    dll.push(4)
    assert dll.head.val == 4, "push method not working"

def test_insert_after():
    dll.insert_after(dll.head.next,100)
    assert dll.head.next.next.val == 100, "insert_after method not working - add between nodes"

    dll.insert_after(dll.head.prev, 200)
    print(dll.head.val)

    dll.insert_after(dll.tail, 300)
    assert dll.tail.val == 300, "insert_after method not working - add after tail"


def test_delete():
    dll.delete(dll.head)
    # print(dll.head.val)
    assert dll.head.val == 4, "delete method not working - delete head"

    dll.delete(dll.head)
    # print(dll.head.val)
    assert dll.head.val == 3, "delete method not working - delete head"

    dll.delete(dll.tail)
    # print(dll.tail.val)
    assert dll.tail.val == 1, "delete method not working - delete tail"

    dll.delete(dll.head.next)
    assert dll.head.next.val == 2, "delete method not working - delete node between nodes"


def test_index():
    assert dll.index(1) == 2, "index method not working"

def test_multiply_all_pairs():
    new = DLL()
    new.push(1)
    new.push(2)
    new.push(3) #investigate why??? data being overwritten
    # print(dll.multiply_all_pairs())
    var = new.multiply_all_pairs()
    print(var)
    assert var == 11 # , "multiply_all_pairs method not working"
    # assert dll.multiply_all_pairs() == 11

def test_all_cases():
    test_push()
    test_insert_after()
    test_delete()
    test_index()
    test_multiply_all_pairs()

def get_runtime_dll_index(start, end, step):
    runtime_list = []
    for n in range(start, end, step):
        l = DLL()
        for i in range(n):
            l.push(i)
        t = timeit.Timer('l.index(random.randrange(n))', 'import random', globals=locals())
        runtime_list.append(t.timeit(50))
    print(runtime_list)
    return runtime_list


def get_runtime_python_index(start, end, step):
    runtime_list = []
    for n in range(start, end, step):
        p_list = []
        for i in range(n):
            p_list.append(i)
        t = timeit.Timer('p_list.index(random.randrange(n))', 'import random', globals=locals())
        runtime_list.append(t.timeit(50))
    return runtime_list


def get_runtime_dll_multiply(start, end, step):
    runtime_list = []
    for n in range(start, end, step):
        l = DLL()
        for i in range(n):
            l.push(i)
        t = timeit.Timer('l.multiply_all_pairs()', 'import random', globals=locals())
        runtime_list.append(t.timeit(50))
    return runtime_list


def plot_runtimes(start, end, step):
    dll_index = get_runtime_dll_index(start, end, step)
    python_index = get_runtime_python_index(start, end, step)
    dll_multiply = get_runtime_dll_multiply(start,end,step)
    n_list = []
    for i in range(start, end, step):
        n_list.append(i)

    print("n_list length: ", len(n_list))
    print("dll_multiply: ", len(dll_multiply))
    print("dll_index: ", len(dll_index))
    print("python_index: ", len(python_index))

    plt.plot(n_list, dll_index, 'r', label="dll_index")
    plt.plot(n_list, python_index, 'g', label ="python_index")
    plt.plot(n_list, dll_multiply, 'b', label="dll_multiply")
    plt.xlabel("Number of elements (n)")
    plt.ylabel("Runtime (s)")
    plt.title("Runtime Analysis Depending on Number of Elements")
    plt.legend()
    plt.show()


dll = DLL()
# test_all_cases()
plot_runtimes(10, 1000, 10)



# print(dll.head.val)
# print(dll.head.next.val)
# print(dll.head.next.next.val)
# print(dll.head.next.next.next.val)
# print(dll.head.next.next.next.next.val)
# print(dll.head.next.next.next.next.next.val)

# print("tail:", dll.tail.val)
