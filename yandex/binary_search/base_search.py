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

def binary_search(seq, x):
    ans = lbinsearch(0, len(seq)-1, checkisge, (seq, x))
    if seq[ans] < x:
        return len(seq)
    return ans


seq = list(map(int, input().split()))
x = int(input())

print(binary_search(seq, x))