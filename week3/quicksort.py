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


def prepare_test100():
    file = open('test100.txt')
    text = file.read()
    file.close()
    input_list_int = map(int, text.splitlines())

    assert (input_list_int[0] == 57)
    assert (input_list_int[-1] == 29)
    assert (len(input_list_int) == 100)

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
    right_sorted_list, right_comparison = quick_sort(right_list, pivot_algorithm)

    left_sorted_list.append(pivot)
    left_sorted_list.extend(right_sorted_list)
    return left_sorted_list, left_comparison + right_comparison + len(original_input) - 1


# Shitty implementation just for the shitty quiz
def shitty_quick_sort(original_input, pivot_algorithm):
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
                f = right_list.pop(0)
                right_list.append(f)
        else:
            right_list.append(elm)

    if len(left_list) > 1:
        tmp = left_list.pop(-1)
        left_list.insert(0, tmp)

    left_sorted_list, left_comparison = shitty_quick_sort(left_list, pivot_algorithm)
    right_sorted_list, right_comparison = shitty_quick_sort(right_list, pivot_algorithm)
    left_sorted_list.append(pivot)
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


def last_pivot(l):
    p = l.pop(-1)
    tmp = l.pop(0)
    l.append(tmp)

    return p, l


# Pivot median
def median_of_three_pivot(l):
    middle_idx = 0
    if len(l) % 2 == 0:
        middle_idx = int(math.floor(len(l) / 2.0)) - 1
    else:
        middle_idx = int(math.floor(len(l) / 2.0))
    vals = [l[0], l[middle_idx], l[-1]]
    sorted_vals = sorted(vals)
    median = sorted_vals[1]
    median_position = vals.index(median)
    if median_position == 0:
        return l.pop(0), l
    elif median_position == 1:
        p = l.pop(middle_idx)
        tmp = l.pop(0)
        l.insert(middle_idx - 1, tmp)
        return p, l
    else:
        p = l.pop(-1)
        tmp = l.pop(0)
        l.append(tmp)
        return p, l

# first
test10_f = prepare_test10()
f_test10_list, f_test10_count = shitty_quick_sort(test10_f, first_pivot)
print(f_test10_count)
print(f_test10_list)

test100_f = prepare_test100()
f_test100_list, f_test100_count = shitty_quick_sort(test100_f, first_pivot)
print(f_test100_count)
print(f_test100_list)

data_f = prepare_data()
f_list, f_count = shitty_quick_sort(data_f, first_pivot)
print(f_count)


# last
test10_l = prepare_test10()
l_test10_list, l_test10_count = shitty_quick_sort(test10_l, last_pivot)
print(l_test10_count)
print(l_test10_list)

test100_l = prepare_test100()
l_test100_list, l_test100_count = shitty_quick_sort(test100_l, last_pivot)
print(l_test100_count)
print(l_test100_list)

data_l = prepare_data()
l_list, l_count = shitty_quick_sort(data_l, last_pivot)
print(l_count)


# median
test10_m = prepare_test10()
m_test10_list, m_test10_count = shitty_quick_sort(test10_m, median_of_three_pivot)
print(m_test10_count)
print(m_test10_list)

test100_m = prepare_test100()
m_test100_list, m_test100_count = shitty_quick_sort(test100_m, median_of_three_pivot)
print(m_test100_count)
print(m_test100_list)

data_m = prepare_data()
m_list, m_count = shitty_quick_sort(data_m, median_of_three_pivot)
print(m_count)








