
def findMax(arr):
    if len(arr) > 0:
        i_max = 0

        for i in range(1, len(arr)):
            i_max = i if arr[i] > arr[i_max] else i_max
        return arr[i_max]
    else:
        return None

tests = [
        [[0,1,2,3,1,50], 50],
        [[], None],
        [[1], 1],
    ]

for t in tests:
    res = findMax(t[0])
    assert t[1] == res, AssertionError(t[0],res)

print('All tests passed')