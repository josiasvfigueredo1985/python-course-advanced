def somar():
    print('somar')


def multi():
    print('multiplicar')


def find_index(item_list, item):
    for i, val in enumerate(item_list):
        if val == item:
            return i
    return 404
