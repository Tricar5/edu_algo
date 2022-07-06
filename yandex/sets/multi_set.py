setsize = 10

myset = [[] for _ in range(setsize)]

def add(x):
    myset[x%10].append(x)

def search(x):
    for now in myset[x%10]:
        if x == now:
            return True
    return False

def remove(x):

    xlist = myset[x % 10]
    for i in range(len(xlist)):

        if x == xlist[i]:

            xlist[i], xlist[len(xlist) - 1] = xlist[len(xlist) - 1], xlist[i]
            xlist.pop()
            return