a = [1, 2, 3, 4, [5, 6, 7, [8, 9, [20, 30, 40]]], [10, 11]]

op = list()


def print_flat_list(a):
    for val in a:
        if type(val) != list:
            op.append(val)
        else:
            print_flat_list(val)


print_flat_list(a)
print(op)
