def checkendowment(m, params):
    n, k = params
    return (k + m) * 3 >= n + m


def lbinsearch(l, r, check, checkparams):

    while l < r:
        m = (l + r) // 2
        # параметризация условия
        if check(m, checkparams):
            r = m
        else:
            l = m + 1

    return l


n, k = list(map(int, input().split()))

print(lbinsearch(0, n, checkendowment, (n, k)))