import random
import math


def prepare_test10():
    file = open('test10.txt')
    text = file.read()
    file.close()
    input_list_int = map(int, text.splitlines())

    assert (input_list_int[0] == 3)
    assert (input_list_int[-1] == 1)
    assert (len(input_list_int) == 10)

    return input_list_int


def prepare_data():
    file = open('quicksort.txt')
    text = file.read()
    file.close()
    input_list_int = map(int, text.splitlines())

    assert(input_list_int[0] == 2148)
    assert(input_list_int[-1] == 9269)
    assert(len(input_list_int) == 10000)

    return input_list_int


# Better implementation of mine
def quick_sort(original_input, pivot_algorithm):
    input = original_input[:]

    if len(original_input) < 2:
        return input, 0

    pivot, new_input = pivot_algorithm(input)
    left_list = []
    right_list = []

    for elm in new_input:
        if elm < pivot:
            left_list.append(elm)
        else:
            right_list.append(elm)

    left_sorted_list, left_comparison = quick_sort(left_list, pivot_algorithm)
    left_sorted_list.append(pivot)
    right_sorted_list, right_comparison = quick_sort(right_list, pivot_algorithm)
    left_sorted_list.extend(right_sorted_list)
    return left_sorted_list, left_comparison + right_comparison + len(original_input) - 1


# Shitty implementation just for the shitty quiz
def shitty_quick_sort(original_input, pivot_algorithm, merge_pivot):
    input = original_input[:]

    if len(original_input) < 2:
        return input, 0

    pivot, new_input = pivot_algorithm(input)
    left_list = []
    right_list = []

    for elm in new_input:
        if elm < pivot:
            left_list.append(elm)
            if len(right_list) > 1:
                tmp = right_list.pop(0)
                right_list.append(tmp)
        else:
            right_list.append(elm)

    left_sorted_list, left_comparison = quick_sort(left_list, pivot_algorithm)
    right_sorted_list, right_comparison = quick_sort(right_list, pivot_algorithm)
    merge_pivot(left_list, right_list, pivot)
    left_sorted_list.extend(right_sorted_list)
    return left_sorted_list, left_comparison + right_comparison + len(original_input) - 1


def random_test(pivot_algorithm):
    while True:
        random_list = [random.randint(1, 10000) for i in range(1000)]
        sorted_list, count = quick_sort(random_list, pivot_algorithm)

        print(random_list)
        print(sorted_list)
        print(count)

        if sorted_list == sorted(random_list):
            print('Great Job!!!!!!')
        else:
            raise Exception('Wrong!!!!!!')


# Pivot First
first_pivot = lambda l: (l.pop(0), l)


def first_merge_pivot(left_list, right_list, pivot):
    tmp = left_list[-1]
    left_list[-1] = pivot
    left_list.insert(0, tmp)

# Pivot Last
last_pivot = lambda l: (l.pop(-1), l)


def last_merge_pivot(left_list, right_list, pivot):
    tmp = right_list[0]
    right_list[0] = pivot
    right_list.append(tmp)


# Pivot median
def median_of_three_pivot(l):
    middle_idx = int(math.ceil(len(l)/2.0))
    vals = [l[0], l[middle_idx], l[-1]]
    sorted_vals = sorted(vals)
    median = sorted_vals[1]
    median_position = vals.index(median)
    if median_position == 0:
        return l.pop(0), l
    elif median_position == 1:
        return l.pop(middle_idx), l
    else:
        return l.pop(-1), l


# test10
test10 = prepare_test10()

# first
f_test10_list, f_test10_count = shitty_quick_sort(test10, first_pivot, first_merge_pivot)
print(f_test10_count)
print(f_test10_list)

# last
l_test10_list, l_test10_count = shitty_quick_sort(test10, last_pivot, last_merge_pivot)
print(l_test10_count)
print(l_test10_list)

# median
# m_test10_list, m_test10_count = quick_sort(test10, median_of_three_pivot)
# print(m_test10_count)

# # Prepare Data
# input = prepare_data()
#
#
#
#
# f_list, count = quick_sort(input, first_pivot)
# print(count)
#
#
# # Pivot Last
#
#
# # random_test(last_pivot)
#
# l_list, count = quick_sort(input, last_pivot)
# print(count)
#
# # Pivot Median
#
#
#
#
# # random_test(median_of_three_pivot)
# m_list, count = quick_sort(input, median_of_three_pivot)
# print(count)








