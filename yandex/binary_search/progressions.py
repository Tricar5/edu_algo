def checkproblemcount(days, params):
    n, k = params
    return (k + (k + days - 1)) * days // 2 >= n


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

print(lbinsearch(0, n, checkproblemcount, (n, k)))