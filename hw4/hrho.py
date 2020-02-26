import numpy as np


# for holding sub-arrays with maximum sum
larray = []
larray_temp = []
rarray = []
rarray_temp = []


def max_sum_crossarray(arr, left, right, mid):
    '''
    Function for getting the maximum sum of sub-array crossing the middle

    arr = find maximum sum and sub-array that produces that sum from this array
    left = the leftmost index of the arr
    right = the rightmost index of the arr
    mid = the middle index of the arr
    '''
    ## the initial left_sum is a big negative value in case of getting a
    ## negative value as a result of the maximum sum for a sub-array
    left_sum = -1000000
    sum = 0

    # clear temporary left sub-array holder
    if larray_temp:
        larray_temp.clear()

    ## go leftward because it is a sub-array that crosses the middle
    ## elements must be analyzed outward from the middle
    for i in range(mid, left-1, -1):
        larray_temp.append(arr[i])
        sum = sum + arr[i]

        if sum > left_sum:
            larray = larray_temp
            left_sum = sum

    ## the initial right_sum is a big negative value in case of getting a
    ## negative value as a result of the maximum sum for a sub-array
    right_sum = -1000000
    sum = 0

    # clear temporary right sub-array holder
    if rarray_temp:
        rarray_temp.clear()

    for i in range(mid+1, right+1):
        rarray_temp.append(arr[i])
        sum = sum + arr[i]

        if sum > right_sum:
            rarray = rarray_temp
            right_sum = sum

    # return the sum of left and right because it has to be a combination of both
    return left_sum + right_sum, larray + rarray



def max_sum_subarray(arr, left, right):
    '''
    Function that returns the maximum sum and the sub-array that outputs the
    maximum sub-array.

    arr = find maximum sum and sub-array that produces that sum from this array
    left = the leftmost index of the arr
    right = the rightmost index of the arr
    '''
    # base case: when there is only one element
    if left == right:
        base_arr = []
        base_arr.append(arr[left])
        return arr[left], base_arr

    middle = (left+right) // 2  # floor division

    # find the max in the subarray in the left part
    max_sum_leftarray = max_sum_subarray(arr, left, middle)

    # find the max in the subarray in the right part
    max_sum_rightarray = max_sum_subarray(arr, middle+1, right)

    # find the max in the subarray crossing the midpoint
    max_sum_middlearray = max_sum_crossarray(arr, left, right, middle)

    return max(max_sum_leftarray, max_sum_rightarray, max_sum_middlearray)



def avg_over_n(n):
    '''
    Function that takes the average maximum sum and the average length of the
    sub-array that produces the maximum sum over n iterations. Generates an
    random array of 100 integers in the range (-10,10) each iteration.

    n = number of iterations
    '''
    tot_val = 0
    tot_len = 0
    for i in range(n):
        ar = np.random.random_integers(-10, 10, 100)
        res = max_sum_subarray(ar, 0, len(ar)-1)
        tot_val += res[0]
        tot_len += len(res[1])

    avg_val = tot_val / n
    avg_len = tot_len / n
    return avg_val, avg_len

print("AVG-100")
print(avg_over_n(100))



def avg_over_n_with_diff_prob(n):
    '''
    Function that takes the average maximum sum and the average length of the
    sub-array that produces the maximum sum over n iterations. Generates an
    random array of 100 integers with different probability distribution in
    each iteration.

    n = number of iterations
    '''
    tot_val = 0
    tot_len = 0

    for i in range(n):
        final_arr = []
        for j in range(n):
            happy_val = np.random.normal(6, 1, 1)
            sad_val = np.random.normal(-7, 0.5, 1)
            happy_sad = [happy_val[0], sad_val[0]]

            arr_val = np.random.choice(happy_sad, p=[0.5, 0.5])
            final_arr.append(arr_val)

        res = max_sum_subarray(final_arr, 0, len(final_arr)-1)
        tot_val += res[0]
        tot_len += len(res[1])

    avg_val = tot_val / n
    avg_len = tot_len / n
    return avg_val, avg_len

print("AVG-100 WITH PROBABILITY DISTRIBUTION")
print(avg_over_n_with_diff_prob(100))
