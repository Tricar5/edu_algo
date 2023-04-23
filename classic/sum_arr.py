def sum_list(X):
    if X == []:
        return 0

    else:
        return X[0] + sum_list(X[1:])


def count_list(X):
    if X == []:
        return 0

    else:
        return 1 + sum_list(X[1:])


def fact(n):
    if n == 1:
        return 1

    return n * fact(n - 1)