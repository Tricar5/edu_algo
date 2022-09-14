def textHistogram(text):

    # init stage

    d = dict()
    maxsymcount = 0
    for l in text:
        if l not in d.keys():
            d[l] = 0
        d[l] += 1
        maxsymcount = max(maxsymcount, d[l])

    # sort
    sortedletters = sorted(d.keys())

    #output
    for row in range(maxsymcount, 0, -1):
        for l in sortedletters:
            if d[l] >= row:
                print('#', end='')
            if d[l] < row:
                print(' ', end='')
        print()
    print(' '.join(sortedletters))
