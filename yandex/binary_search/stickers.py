
# Разместить квадратные стикеры на доске

def checkstickers(size, params):
    n, w, h = params
    return (w // size) * (h // size) >= n

def rbinsearch(l, r, check, checkparams):

    while l != r:
        m = (l + r + 1) // 2
        
        if check(m, checkparams):
            l = m
        else:
            r = m - 1

    return l

n, w, h = list(map(int, input().split()))

print(rbinsearch(1, max(w, h), checkstickers, (n, w, h)))