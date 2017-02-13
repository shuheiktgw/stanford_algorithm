import random


def prepare_data(name):
    file = open(name)
    text = file.read()
    file.close()

    lines = list(map(lambda l: list(map(int, l.split(' '))), text.splitlines()))

    return {l[0]: l[1:] for l in lines}


def random_contraction(data):
    v1, v2 = select_random_node(data)
    return contraction(v1, v2, data)


def select_random_node(data):
    v1 = random.choice(data.keys())
    v2 = random.choice(data[v1])

    return v1, v2


def contraction(v1, v2, data):
    for v2_value in set(data[v2]):
        data[v2_value] = [v1 if v == v2 else v for v in data[v2_value]]

    # delete self loops
    data[v1] = [v for v in data[v1] + data[v2] if v != v1 and v != v2]
    del data[v2]

    return data


def execute_random_contraction(file_name):
    data = prepare_data(file_name)

    while len(data) != 2:
        data = random_contraction(data)

    return len(data[list(data.keys())[1]])



# Question
print('Question')
length = min([execute_random_contraction('adjacency_list.txt') for i in range(40000)])
print(length)
