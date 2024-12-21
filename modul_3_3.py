def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [True, 'start', 25]
values_dict = {'a': 25, 'b': 1, 'c': 11}
values_list_2 = ['Phone', 36]

print_params()
print_params(b = 25, c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, c = 42)
