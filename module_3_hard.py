nested_data = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


# print(1 + 2 + 3 + 1 + 4 + 1 + 5 + 6 + 4 + 7 + 4 + 8 + 5 + 2 + 5 + 6 + 35)


def calculate_nested_sum(*args):
    total_sum = 0

    for arg in args:
        if isinstance(arg, (list, tuple, set)):
            total_sum += calculate_nested_sum(*arg)
        elif isinstance(arg, dict):
            total_sum += calculate_nested_sum(*arg.items())
        elif isinstance(arg, str):
            total_sum += len(arg)
        elif isinstance(arg, (int, float)):
            total_sum += arg
        elif arg is None:
            pass

    return total_sum


print(calculate_nested_sum(nested_data))