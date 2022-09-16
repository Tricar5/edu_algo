# Задача о ежемесячном проценте

def checkmonthlyperc(mperc, yperc):
    msum = 1 + mperc / 100
    ysym = 1 + yperc / 100
    return msum ** 12 >= ysym

def fbinsearch(l, r, eps, check, checkparams):

    while l + eps < r:
        m = (l + r) / 2
        if check(m, checkparams):
            r = m
        else:
            l = m
    return l

x = 12
eps = 0.0001
mperc = fbinsearch(0, x, eps, checkmonthlyperc, x)


def checkcredit(mpay, params):
    periods, creditsum, mperc = params
    for i in range(periods):
        percpay = creditsum * (mperc / 100)
        creditsum -= mpay - percpay
    return creditsum <= 0

def fbinsearch(l, r, eps, check, checkparams):

    while l + eps < r:
        m = (l + r) / 2
        if check(m, checkparams):
            r = m
        else:
            l = m
    return l


eps = 0.01
m = 10 ** 7
n = 300
monthlypay = fbinsearch(0, m, eps, checkcredit, (n, m, mperc))
print(monthlypay)