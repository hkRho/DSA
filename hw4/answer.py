import numpy as np


larray = []
larray_temp = []
rarray = []
rarray_temp = []
marray = []
marray_temp = []


def max_sum_crossarray(arr, left, right, mid):
    '''
    The initial left and right sums are a big negative value in case of
    getting a negative value as a result for the maximum sum for a subarray
    '''
    left_sum = -1000000
    sum = 0
    if larray_temp:
        larray_temp.clear()

    # have to go leftward bc it is a crossing subarray
    for i in range(mid, left-1, -1):
        larray_temp.append(arr[i])
        sum = sum + arr[i]

        if sum > left_sum:
            larray = larray_temp
            left_sum = sum
            # print("lsum: ", left_sum)


    right_sum = -1000000
    sum = 0
    if rarray_temp:
        rarray_temp.clear()

    for i in range(mid+1, right+1):
        rarray_temp.append(arr[i])
        sum = sum + arr[i]

        if sum > right_sum:
            rarray = rarray_temp
            right_sum = sum
            # print("rsum: ", right_sum)

    # return the sum of left and right because it has to be a combination of both
    return left_sum + right_sum, larray + rarray


# l = left, r = right, m = middle (index numbers)
def max_sum_subarray(arr, left, right):
    # base case: when there is only one element
    if left == right:
        base_arr = []
        base_arr.append(arr[left])
        return arr[left], base_arr

    middle = (left+right)//2

    # find the max in the subarray in the left part
    max_sum_leftarray = max_sum_subarray(arr, left, middle)

    # find the max in the subarray in the right part
    max_sum_rightarray = max_sum_subarray(arr, middle+1, right)

    # find the max in the subarray crossing the midpoint
    max_sum_middlearray = max_sum_crossarray(arr, left, right, middle)

    return max(max_sum_leftarray, max_sum_rightarray, max_sum_middlearray)


def avg_over_n(n):
    tot_val = 0
    tot_len = 0
    for i in range(n):
        ar = np.random.random_integers(-10, 10, n)
        res = max_sum_subarray(ar, 0, len(ar)-1)
        tot_val += res[0]
        tot_len += len(res[1])

    avg_val = tot_val / n
    avg_len = tot_len / n
    return avg_val, avg_len

print("AVG-100")
print(avg_over_n(100))


def avg_over_n_with_diff_prob(n):
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
