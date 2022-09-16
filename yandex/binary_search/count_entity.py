def checkisgt(index, params):
    seq, x = params
    return seq[index] > x

def checkisge(index, params):
    seq, x = params
    return seq[index] >= x


def lbinsearch(l, r, check, checkparams):

    while l < r:
        m = (l + r) // 2
        # параметризация условия
        if check(m, checkparams):
            r = m
        else:
            l = m + 1

    return l

def findfirst(seq, x, check):
    ans = lbinsearch(0, len(seq) - 1, check, (seq, x))
    if not check(ans, (seq, x)):
        return len(seq)
    return ans

def count_x(seq, x):
    indexgt = findfirst(seq, x, checkisgt)
    indexge = findfirst(seq, x, checkisge)
    return indexgt - indexge


seq = list(map(int, input().split()))
x = int(input())

print(count_x(seq, x))