import random
import copy



def prepare_data(name):
    file = open(name)
    text = file.read()
    file.close()

    lines = map(lambda l: map(int, l.split(' ')), text.splitlines())
    return {l[0]: l[1:] for l in lines}


def random_contraction(original_data):
    data = copy.deepcopy(original_data)
    v1, v2 = random.sample(data.keys(), 2)
    return contraction(v1, v2, data)


def contraction(v1, v2, original_data):
    data = copy.deepcopy(original_data)

    for v2_value in data[v2]:
        data[v2_value] = [v1 if v == v2 else v for v in data[v2_value]]

    # delete self loops
    values = data[v1] + data[v2]
    filtered = filter(lambda v: v != v1 and v != v2, values)

    del data[v2]
    data[v1] = filtered

    return data


def execute_random_contraction(file_name):

    output = prepare_data(file_name)

    while len(output) != 2:
        output = random_contraction(output)

    return len(output[output.keys()[0]])

# test1
print('test1')
print(min([execute_random_contraction('test1.txt') for i in range(1000)]))

# Question
print('Question')
print(min([execute_random_contraction('adjacency_list.txt') for i in range(200 * 200)]))

