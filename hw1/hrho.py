# -----------------------------------------------------------
# Data Structures and Algorithms
# Homework 1 - Problem 3
#
# @Author: HK Rho
# -----------------------------------------------------------
import pytest

def increasing_seq(list):
    """
    Function that returns the longest increasing sequence of integers from a given list of integers

    Parameters:
    list: list of integer values
    """
    current = []
    output = []

    for i in range(len(list)-1):
        # always add the first item of the sequence to the currently storing list
        if len(current) == 0:
            current.append(list[i])

        # if the next item is greater than the current item, add the next item to currently storing list
        if list[i+1] > list[i]:
            current.append(list[i+1])

        # if the next item is not greater than the current item, execute below
        else:
            # if the currently storing list is longer than the final output list, store the current list into the output list
            if len(current) > len(output):
                output = current
                current = []
            # if the currently storing list is not longer than the final output list, keep the output list
            if len(current) < len(output):
                output = output
                current = []
    return output

def tests():
    """
    Function that contains the four pytests to check whether the function passes all the conditions.
    """
    assert [] == increasing_seq([]), "test failed"
    assert [3] == increasing_seq([3,2,1]), "test failed"
    assert [0,4,8,9] == increasing_seq([1,2,0,4,8,9,3]), "test failed"
    assert [1,2,3] == increasing_seq([1,2,3,3]), "test failed" # add more context to the comments here instead of test failed


tests()
